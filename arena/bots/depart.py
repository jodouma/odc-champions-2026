"""Squelette de départ (starters/python/bot.py) adapté au jeu Récolte.

Seule `read_turn` a changé : elle lit l'entrée du jeu. `decide` renvoie
toujours WAIT : à toi de l'améliorer.
"""
import sys
import time

TURN_BUDGET_S = 0.040  # garde une marge sous la limite de l'arène (100 ms par défaut)


def debug(*args):
    """Les messages de debug vont sur stderr : stdout est réservé aux actions."""
    print(*args, file=sys.stderr, flush=True)


def read_init():
    """Lu une seule fois, au début du 1er tour."""
    nb_players, my_id = map(int, input().split())
    width, height, nb_turns = map(int, input().split())
    return nb_players, my_id


def read_turn(nb_players):
    """Lit les entrées d'un tour : les joueurs, puis les olives."""
    players = [tuple(map(int, input().split())) for _ in range(nb_players)]  # x y score actif
    olives = [tuple(map(int, input().split())) for _ in range(int(input()))]  # x y valeur
    return players, olives


def decide(state, my_id, deadline):
    """Renvoie l'action du tour. Commence simple : une action toujours légale."""
    best = "WAIT"
    while time.perf_counter() < deadline:
        # Ici : essayer des actions candidates et garder la meilleure.
        break
    return best


def main():
    try:
        nb_players, my_id = read_init()
    except EOFError:
        return
    while True:
        try:
            state = read_turn(nb_players)
        except EOFError:
            return
        deadline = time.perf_counter() + TURN_BUDGET_S
        print(decide(state, my_id, deadline), flush=True)


if __name__ == "__main__":
    main()
