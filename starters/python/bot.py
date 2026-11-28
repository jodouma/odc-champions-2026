"""Squelette générique de bot CodinGame (Python 3).

Le bot lit l'état du jeu sur l'entrée standard et écrit une action par tour.
Remplis les zones « À ADAPTER », dans cet ordre :
  1. les constantes (recopiées de l'énoncé) ;
  2. read_init et read_turn (le format d'entrée) ;
  3. legal_moves (toujours au moins un coup légal) ;
  4. evaluate (la note d'un coup : plus haut = mieux).
Le reste (chrono, debug, choix du coup) marche déjà.
"""
import sys
import time

# ---- À ADAPTER : recopie ces valeurs de l'énoncé ----
VERSION = "v1"               # change-la à chaque soumission ; affichée sur stderr au tour 1
TURN_LIMIT_MS = 50           # temps permis par tour
FIRST_TURN_LIMIT_MS = 1000   # temps permis au 1er tour (souvent plus long)
BUDGET_RATIO = 0.5           # on n'utilise que la moitié : le serveur est plus lent que ton PC
DEBUG = True                 # affiche l'entrée lue et le temps du tour sur stderr


def debug(*args):
    """Les messages de debug vont sur stderr : stdout est réservé aux actions."""
    if DEBUG:
        print(*args, file=sys.stderr, flush=True)


class State:
    """Tout ce que le bot sait du jeu. Ajoute tes champs ici."""

    def __init__(self):
        self.turn = 0
        self.init_lines = []  # entrée du début de partie, brute
        self.lines = []       # entrée du tour courant, brute


def read_init(state):
    """À ADAPTER : lit l'entrée donnée une seule fois, avant le 1er tour."""
    state.init_lines = [input()]


def read_turn(state):
    """À ADAPTER : lit TOUTES les lignes d'un tour, même celles dont tu n'as pas besoin."""
    state.lines = [input()]


def legal_moves(state):
    """À ADAPTER : la liste des coups autorisés. Jamais vide : garde un coup de secours."""
    return ["WAIT"]


def evaluate(state, move):
    """À ADAPTER : la note d'un coup. Commence simple, améliore une idée à la fois."""
    return 0.0


def pick(state, deadline):
    """Note chaque coup légal tant qu'il reste du temps ; garde le meilleur."""
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
        start = time.perf_counter()  # le chrono part quand l'entrée du tour est lue
        state.turn += 1
        limit_ms = FIRST_TURN_LIMIT_MS if state.turn == 1 else TURN_LIMIT_MS
        deadline = start + limit_ms * BUDGET_RATIO / 1000
        debug(f"T{state.turn} entree={state.lines}")
        print(pick(state, deadline), flush=True)
        debug(f"T{state.turn} t={(time.perf_counter() - start) * 1000:.1f}ms")


if __name__ == "__main__":
    main()
