"""Bot trop lent : joue normalement, puis réfléchit 0,5 s au tour 5 et perd."""
import time

nb_players, my_id = map(int, input().split())
width, height, nb_turns = map(int, input().split())
turn = 0
while True:
    try:
        for _ in range(nb_players):
            input()
        for _ in range(int(input())):
            input()
    except EOFError:
        break
    turn += 1
    if turn == 5:
        time.sleep(0.5)
    print("RIGHT", flush=True)
