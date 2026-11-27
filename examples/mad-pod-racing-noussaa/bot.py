import sys, math

# Mad Pod Racing - Wood 2
# Nouveau par rapport a Wood 3 : la distance et l'angle au checkpoint sont
# fournis, et une deuxieme ligne donne la position de l'adversaire.
#
# Entree par tour :
#   x y nextCheckpointX nextCheckpointY nextCheckpointDist nextCheckpointAngle
#   opponentX opponentY
# Sortie par tour : targetX targetY thrust

prev_x = prev_y = None

while True:
    x, y, cx, cy, dist, angle = map(int, input().split())
    ox, oy = map(int, input().split())

    # Vitesse estimee : difference de position entre deux tours.
    if prev_x is None:
        vx = vy = 0.0
    else:
        vx = float(x - prev_x)
        vy = float(y - prev_y)
    prev_x, prev_y = x, y

    a = abs(angle)

    # On vise en avance pour compenser la derive : le pod garde 85% de sa
    # vitesse chaque tour, donc viser cp - k*v recentre la trajectoire au lieu
    # de la laisser decrire un arc. Inutile quand on est deja de dos au
    # checkpoint : il faut d'abord se retourner.
    if a < 90:
        tx = cx - 3.0 * vx
        ty = cy - 3.0 * vy
    else:
        tx, ty = float(cx), float(cy)

    # Puissance. Le pod ne tourne que de 18 degres par tour : au-dela de 90
    # degres, pousser ne fait qu'eloigner, on coupe pour pivoter sur place.
    if a >= 90:
        thrust = 0
    elif a > 45:
        thrust = 40
    elif dist < 1400 and a > 15:
        # Virage serre a l'approche : on ralentit pour ne pas deborder.
        thrust = 60
    else:
        thrust = 100

    print("d=%d a=%d v=%.0f t=%d" % (dist, angle, math.hypot(vx, vy), thrust),
          file=sys.stderr)
    print("%d %d %d" % (round(tx), round(ty), thrust), flush=True)
