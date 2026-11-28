"""Squelette de départ (starters/python/bot.py) adapté au jeu Récolte.

Ont changé : les constantes, read_init, read_turn et legal_moves.
`evaluate` note tous les coups à 0, donc le bot attend (WAIT) :
à toi de l'améliorer.
"""
import sys
import time

VERSION = "depart-v1"
TURN_LIMIT_MS = 100          # limite de l'arène par défaut
FIRST_TURN_LIMIT_MS = 1000
BUDGET_RATIO = 0.5
DEBUG = True


def debug(*args):
    """Les messages de debug vont sur stderr : stdout est réservé aux actions."""
    if DEBUG:
        print(*args, file=sys.stderr, flush=True)


class State:
    def __init__(self):
        self.turn = 0
        self.nb_players = 0
        self.my_id = 0
        self.players = []  # (x, y, score, actif) par joueur
        self.olives = []   # (x, y, valeur)


def read_init(state):
    """Lu une seule fois, au début du 1er tour."""
    state.nb_players, state.my_id = map(int, input().split())
    input()  # largeur hauteur nb_tours : lue même si on ne s'en sert pas


def read_turn(state):
    """Lit les entrées d'un tour : les joueurs, puis les olives."""
    state.players = [tuple(map(int, input().split())) for _ in range(state.nb_players)]
    state.olives = [tuple(map(int, input().split())) for _ in range(int(input()))]


def legal_moves(state):
    return ["WAIT", "UP", "DOWN", "LEFT", "RIGHT"]


def evaluate(state, move):
    """À améliorer : par exemple, la valeur de l'olive la plus proche après ce pas."""
    return 0.0


def pick(state, deadline):
    moves = legal_moves(state)
    best, best_score = moves[0], float("-inf")
    for move in moves:
        if time.perf_counter() >= deadline:
            debug("chrono : arrêt avant la fin de la liste")
            break
        score = evaluate(state, move)
        if score > best_score:
            best, best_score = move, score
    return best


def main():
    state = State()
    try:
        read_init(state)
    except EOFError:
        return
    debug("VERSION", VERSION)
    while True:
        try:
            read_turn(state)
        except EOFError:
            return
        start = time.perf_counter()
        state.turn += 1
        limit_ms = FIRST_TURN_LIMIT_MS if state.turn == 1 else TURN_LIMIT_MS
        deadline = start + limit_ms * BUDGET_RATIO / 1000
        print(pick(state, deadline), flush=True)
        debug(f"T{state.turn} t={(time.perf_counter() - start) * 1000:.1f}ms")


if __name__ == "__main__":
    main()
