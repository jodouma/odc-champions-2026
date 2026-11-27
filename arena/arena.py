#!/usr/bin/env python3
"""Arène locale : fait jouer des bots (n'importe quel langage) les uns contre les autres.

Jeu : « Récolte », un jeu original très simple (règles dans README.md).
Aucune dépendance : Python 3.8+ suffit.

    python3 arena/arena.py match arena/bots/glouton.py arena/bots/depart.py arena/bots/aleatoire.py
    python3 arena/arena.py tournoi arena/bots/glouton.py arena/bots/depart.py arena/bots/aleatoire.py
"""
from __future__ import annotations

import argparse
import itertools
import os
import queue
import random
import shlex
import subprocess
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

WIDTH, HEIGHT = 13, 9
MAX_TURNS = 100
FIRST_TURN_TIMEOUT_MS = 1000  # le 1er tour laisse le temps de démarrer le programme
DEFAULT_TIMEOUT_MS = 100
START_OLIVES = 8
MAX_OLIVES = 16
SPAWN_EVERY = 3  # nouvelles olives tous les 3 tours
CORNERS = [(0, 0), (WIDTH - 1, HEIGHT - 1), (WIDTH - 1, 0), (0, HEIGHT - 1)]
STEPS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0), "WAIT": (0, 0)}


class BotError(Exception):
    """Le bot a perdu : temps dépassé, plantage ou action invalide."""


@dataclass(frozen=True)
class BotSpec:
    name: str
    command: list


def parse_spec(spec: str) -> BotSpec:
    """'glouton.py', './mon_bot', 'python3 x.py' ou 'nom=commande'."""
    name, sep, rest = spec.partition("=")
    if sep and name and not any(c in name for c in " /\\"):
        spec = rest
    else:
        name = ""
    path = Path(spec)
    if path.is_file() and path.suffix == ".py":
        command = [sys.executable, "-u", str(path)]
    elif path.is_file():
        command = [str(path.resolve())]
    else:
        command = shlex.split(spec, posix=os.name != "nt")
    if not name:
        files = [Path(t) for t in command if Path(t).is_file()] or [Path(command[0])]
        name = files[-1].stem if files[-1].stem != "bot" else files[-1].resolve().parent.name
    return BotSpec(name, command)


def unique_names(specs: list) -> list:
    seen = {}
    out = []
    for s in specs:
        seen[s.name] = seen.get(s.name, 0) + 1
        out.append(s if seen[s.name] == 1 else BotSpec(f"{s.name}#{seen[s.name]}", s.command))
    return out


class Bot:
    """Un programme lancé en sous-processus, qui parle par stdin/stdout."""

    def __init__(self, spec: BotSpec, debug: bool = False):
        self.name = spec.name
        self.lines = queue.Queue()
        self.error = ""
        try:
            self.proc = subprocess.Popen(
                spec.command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE if debug else subprocess.DEVNULL,
                text=True,
                encoding="utf-8",
                errors="replace",
                bufsize=1,
            )
        except OSError as e:
            self.proc = None
            self.error = f"impossible de lancer {' '.join(spec.command)!r} : {e}"
            return
        threading.Thread(target=self._read_stdout, daemon=True).start()
        if debug:
            threading.Thread(target=self._print_stderr, daemon=True).start()

    def _read_stdout(self):
        with self.proc.stdout:
            for line in self.proc.stdout:
                self.lines.put(line.strip())
        self.lines.put(None)  # fin du programme

    def _print_stderr(self):
        with self.proc.stderr:
            for line in self.proc.stderr:
                print(f"  [{self.name}] {line.rstrip()}", file=sys.stderr, flush=True)

    def ask(self, text: str, timeout_ms: int) -> str:
        """Envoie l'état du tour et attend UNE ligne de réponse."""
        if self.proc is None:
            raise BotError(self.error)
        try:
            self.proc.stdin.write(text)
            self.proc.stdin.flush()
        except OSError:
            raise BotError("le programme s'est arrêté")
        try:
            line = self.lines.get(timeout=timeout_ms / 1000)
        except queue.Empty:
            raise BotError(f"temps dépassé (> {timeout_ms} ms)")
        if line is None:
            raise BotError("le programme s'est arrêté (plantage ?)")
        return line

    def stop(self):
        if self.proc is None or self.proc.stdin.closed:
            return
        try:
            self.proc.kill()
            self.proc.wait(timeout=2)
            self.proc.stdin.close()
        except (OSError, subprocess.TimeoutExpired):
            pass


@dataclass
class Player:
    bot: Bot
    x: int
    y: int
    score: int = 0
    out_turn: Optional[int] = None  # tour d'élimination
    reason: str = ""

    @property
    def active(self) -> bool:
        return self.out_turn is None


def sign(v: int) -> int:
    return (v > 0) - (v < 0)


def next_cell(line: str, x: int, y: int) -> tuple:
    """Case atteinte après l'action ; sortir de la grille = rester sur place."""
    parts = line.split()
    word = parts[0].upper() if parts else ""
    if word in STEPS:
        dx, dy = STEPS[word]
    elif word == "MOVE" and len(parts) >= 3:
        try:
            tx, ty = int(parts[1]), int(parts[2])
        except ValueError:
            raise BotError(f"action invalide : {line!r}")
        dx = sign(tx - x)  # d'abord en x, puis en y
        dy = 0 if dx else sign(ty - y)
    else:
        raise BotError(f"action invalide : {line!r}")
    nx, ny = x + dx, y + dy
    if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
        return nx, ny
    return x, y


def ranking(players: list) -> list:
    """[(rang, joueur)] : survivants par score, puis éliminés (le plus tard d'abord)."""
    key = lambda p: (p.active, p.out_turn or 0, p.score)  # noqa: E731
    ordered = sorted(players, key=key, reverse=True)
    out = []
    for i, p in enumerate(ordered):
        rank = out[-1][0] if i and key(p) == key(ordered[i - 1]) else i + 1
        out.append((rank, p))
    return out


def draw(players: list, olives: dict, turn: int) -> str:
    grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for (x, y), v in olives.items():
        grid[y][x] = str(v)
    for i, p in enumerate(players):
        grid[p.y][p.x] = chr(ord("A") + i) if p.active else "x"
    scores = "  ".join(f"{chr(ord('A') + i)}={p.bot.name}:{p.score}" for i, p in enumerate(players))
    return f"Tour {turn}  {scores}\n" + "\n".join(" ".join(r) for r in grid)


def run_match(specs: list, seed: int = 0, timeout_ms: int = DEFAULT_TIMEOUT_MS,
              max_turns: int = MAX_TURNS, show: bool = False, debug: bool = False) -> list:
    """Joue un match ; renvoie [(rang, joueur)]."""
    if not 2 <= len(specs) <= 4:
        raise ValueError("un match se joue à 2, 3 ou 4 bots")
    rng = random.Random(seed)
    players = [Player(Bot(s, debug), *CORNERS[i]) for i, s in enumerate(specs)]
    olives = {}

    def spawn(n: int):
        taken = set(olives) | {(p.x, p.y) for p in players}
        free = [(x, y) for x in range(WIDTH) for y in range(HEIGHT) if (x, y) not in taken]
        for cell in rng.sample(free, min(n, len(free), MAX_OLIVES - len(olives))):
            olives[cell] = rng.choice((1, 1, 2, 3))

    def eliminate(p: Player, turn: int, why: str):
        p.out_turn, p.reason = turn, why
        p.bot.stop()

    spawn(START_OLIVES)
    try:
        for turn in range(1, max_turns + 1):
            if sum(p.active for p in players) <= 1:
                break
            state = "".join(f"{p.x} {p.y} {p.score} {int(p.active)}\n" for p in players)
            state += f"{len(olives)}\n" + "".join(f"{x} {y} {v}\n" for (x, y), v in olives.items())
            moves = {}
            for i, p in enumerate(players):
                if not p.active:
                    continue
                text, limit = state, timeout_ms
                if turn == 1:
                    text = f"{len(players)} {i}\n{WIDTH} {HEIGHT} {max_turns}\n" + state
                    limit = max(FIRST_TURN_TIMEOUT_MS, timeout_ms)
                try:
                    moves[i] = next_cell(p.bot.ask(text, limit), p.x, p.y)
                except BotError as e:
                    eliminate(p, turn, str(e))
            for i, (x, y) in moves.items():
                players[i].x, players[i].y = x, y
            by_cell = {}
            for p in players:
                if p.active:
                    by_cell.setdefault((p.x, p.y), []).append(p)
            for cell, takers in by_cell.items():
                value = olives.pop(cell, 0)
                if len(takers) == 1:  # à plusieurs sur la même olive : elle est perdue
                    takers[0].score += value
            if turn % SPAWN_EVERY == 0:
                spawn(rng.randint(1, 2))
            if show:
                print(draw(players, olives, turn) + "\n", flush=True)
                time.sleep(0.15)
    finally:
        for p in players:
            p.bot.stop()
    return ranking(players)


def print_result(result: list, seed: int):
    print(f"Résultat (graine {seed})")
    print(f"{'Rang':<6}{'Bot':<20}{'Score':>6}  État")
    for rank, p in result:
        state = "" if p.active else f"éliminé au tour {p.out_turn} : {p.reason}"
        print(f"{rank:<6}{p.bot.name:<20}{p.score:>6}  {state}")


def run_tournament(specs: list, per_match: int, games: int, seed: int,
                   timeout_ms: int, max_turns: int) -> list:
    """Toutes les combinaisons de bots, chaque bot à chaque place de départ."""
    stats = {s.name: {"points": 0.0, "wins": 0, "matches": 0, "score": 0, "out": 0} for s in specs}
    schedule = [(combo[r:] + combo[:r], seed + g)
                for combo in itertools.combinations(specs, per_match)
                for g in range(games) for r in range(per_match)]
    for n, (seats, match_seed) in enumerate(schedule, 1):
        result = run_match(list(seats), match_seed, timeout_ms, max_turns)
        for rank, p in result:
            st = stats[p.bot.name]
            st["matches"] += 1
            st["score"] += p.score
            st["wins"] += rank == 1
            st["out"] += not p.active
            st["points"] += sum(1 if rank < r else 0.5 if rank == r else 0
                                for r, q in result if q is not p)
        summary = ", ".join(f"{r}. {p.bot.name} ({p.score})" for r, p in result)
        print(f"Match {n}/{len(schedule)} graine {match_seed} : {summary}", flush=True)
    table = sorted(stats.items(), key=lambda kv: (kv[1]["points"], kv[1]["wins"]), reverse=True)
    print(f"\n{'Rang':<6}{'Bot':<20}{'Points':>7}{'1ers':>6}{'Matchs':>8}{'Score moy.':>12}{'Éliminé':>9}")
    for i, (name, st) in enumerate(table, 1):
        avg = st["score"] / st["matches"]
        print(f"{i:<6}{name:<20}{st['points']:>7g}{st['wins']:>6}{st['matches']:>8}{avg:>12.1f}{st['out']:>9}")
    print("\nPoints : +1 par adversaire classé derrière toi dans un match, +0,5 en cas d'égalité.")
    return table


def main(argv=None):
    parser = argparse.ArgumentParser(description="Arène locale pour bots (jeu Récolte).")
    sub = parser.add_subparsers(dest="mode", required=True)
    for mode, helptext in (("match", "un match entre 2 à 4 bots"),
                           ("tournoi", "toutes les combinaisons + classement")):
        p = sub.add_parser(mode, help=helptext)
        p.add_argument("bots", nargs="+", help="fichier .py, exécutable, ou commande entre guillemets")
        p.add_argument("--graine", type=int, default=1, help="graine du hasard (même graine = même partie)")
        p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_MS, help="ms par tour (défaut 100)")
        p.add_argument("--tours", type=int, default=MAX_TURNS, help="nombre de tours (défaut 100)")
    sub.choices["match"].add_argument("--voir", action="store_true", help="affiche la grille à chaque tour")
    sub.choices["match"].add_argument("--debug", action="store_true", help="affiche le stderr des bots")
    sub.choices["tournoi"].add_argument("--parties", type=int, default=3, help="graines par groupe (défaut 3)")
    sub.choices["tournoi"].add_argument("--joueurs", type=int, default=0,
                                        help="bots par match (défaut : 3, ou 2 s'il n'y a que 2 bots)")
    args = parser.parse_args(argv)
    specs = unique_names([parse_spec(b) for b in args.bots])

    if args.mode == "match":
        if not 2 <= len(specs) <= 4:
            parser.error("un match se joue à 2, 3 ou 4 bots")
        result = run_match(specs, args.graine, args.timeout, args.tours, args.voir, args.debug)
        print_result(result, args.graine)
    else:
        per_match = args.joueurs or min(3, len(specs))
        if not 2 <= per_match <= min(4, len(specs)):
            parser.error("--joueurs doit être entre 2 et 4, et pas plus que le nombre de bots")
        run_tournament(specs, per_match, args.parties, args.graine, args.timeout, args.tours)


if __name__ == "__main__":
    main()
