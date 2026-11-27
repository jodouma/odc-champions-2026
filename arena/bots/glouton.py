"""Bot glouton : va vers l'olive qui rapporte le plus par case parcourue."""
nb_players, my_id = map(int, input().split())
width, height, nb_turns = map(int, input().split())

while True:
    try:
        players = [tuple(map(int, input().split())) for _ in range(nb_players)]
    except EOFError:
        break
    olives = [tuple(map(int, input().split())) for _ in range(int(input()))]
    x, y = players[my_id][0], players[my_id][1]
    if not olives:
        print("WAIT", flush=True)
        continue
    ox, oy, _ = max(olives, key=lambda o: o[2] / (abs(o[0] - x) + abs(o[1] - y) + 1))
    print(f"MOVE {ox} {oy}", flush=True)
