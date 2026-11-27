import sys
from collections import deque

W, H = 30, 20
DIRS = [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]
trail = {}  # player index -> set of cells (grid keeps ribbons of live players only)


def bfs(blocked, sx, sy):
    """Distance map from (sx, sy) over free cells."""
    dist = {(sx, sy): 0}
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        d = dist[(x, y)] + 1
        for _, dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in blocked and (nx, ny) not in dist:
                dist[(nx, ny)] = d
                q.append((nx, ny))
    return dist


while True:
    n, p = map(int, input().split())
    heads = {}
    for i in range(n):
        x0, y0, x1, y1 = map(int, input().split())
        if x1 < 0:
            trail.pop(i, None)  # lost players' ribbons disappear
            continue
        trail.setdefault(i, set()).update([(x0, y0), (x1, y1)])
        heads[i] = (x1, y1)
    blocked = set().union(*trail.values()) if trail else set()
    mx, my = heads[p]
    foes = [h for i, h in heads.items() if i != p]

    best, best_key = "UP", None
    for name, dx, dy in DIRS:
        nx, ny = mx + dx, my + dy
        if not (0 <= nx < W and 0 <= ny < H) or (nx, ny) in blocked:
            continue
        b2 = blocked | {(nx, ny)}
        mine = bfs(b2, nx, ny)
        room = len(mine)  # reachable free cells after the move (flood fill)
        # tie-break: cells I reach before the opponent (Voronoi)
        vor = room
        if foes:
            fd = bfs(b2, *foes[0])
            inf = 10**9
            vor = sum(1 for c, d in mine.items() if d < fd.get(c, inf)) - sum(
                1 for c, d in fd.items() if d <= mine.get(c, inf))
        key = (room, vor)
        if best_key is None or key > best_key:
            best, best_key = name, key
    print(best, flush=True)
