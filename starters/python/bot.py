"""Squelette générique de bot CodinGame (Python 3).

Le bot lit l'état du jeu sur l'entrée standard et écrit une action par tour.
Adapte `read_turn` et `decide` à l'énoncé du jeu.
"""
import sys
import time

TURN_BUDGET_S = 0.040  # garde une marge sous la limite de l'énoncé (ex. 50 ms)


def debug(*args):
    """Les messages de debug vont sur stderr : stdout est réservé aux actions."""
    print(*args, file=sys.stderr, flush=True)


def read_turn():
    """Lit les entrées d'un tour. À adapter à l'énoncé."""
    return input()


def decide(state, deadline):
    """Renvoie l'action du tour. Commence simple : une action toujours légale."""
    best = "WAIT"
    while time.perf_counter() < deadline:
        # Ici : essayer des actions candidates et garder la meilleure.
        break
    return best


def main():
    while True:
        try:
            state = read_turn()
        except EOFError:
            return
        deadline = time.perf_counter() + TURN_BUDGET_S
        print(decide(state, deadline), flush=True)


if __name__ == "__main__":
    main()
