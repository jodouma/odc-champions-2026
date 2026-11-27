"""Bot aléatoire : un pas au hasard à chaque tour."""
import random

nb_players, my_id = map(int, input().split())
width, height, nb_turns = map(int, input().split())

while True:
    try:
        for _ in range(nb_players):
            input()
        for _ in range(int(input())):
            input()
    except EOFError:
        break
    print(random.choice(["UP", "DOWN", "LEFT", "RIGHT"]), flush=True)
