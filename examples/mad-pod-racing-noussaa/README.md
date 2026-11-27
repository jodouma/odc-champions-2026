# Exemple : un bot Mad Pod Racing (ligue Silver)

Un bot d'entraînement écrit avec l'IA, via l'API officielle de CodinGame. Il joue sous le pseudo `Noussaa`.

- Jeu : [Mad Pod Racing](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing) · [classement](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing/leaderboard)
- Code : [`bot.py`](bot.py) (Python 3, 52 lignes). C'est exactement la version en ligne au moment du partage, récupérée avec l'API (`GET /puzzles/mad-pod-racing/submissions/{id}`).

## Comment il joue

1. **Il vise en avance.** Il estime sa vitesse avec la différence de position entre deux tours, puis vise `checkpoint − 3 × vitesse` au lieu du checkpoint lui-même. Le pod garde 85 % de sa vitesse à chaque tour : viser le checkpoint en direct fait décrire un arc, viser en avance annule la dérive.
2. **Il dose la puissance selon l'angle.** Le pod ne tourne que de 18° par tour :
   - angle ≥ 90° : puissance 0, il pivote sur place au lieu de s'éloigner ;
   - angle > 45° : puissance 40 ;
   - près du checkpoint (< 1400) et angle > 15° : puissance 60, pour ne pas déborder ;
   - sinon : 100.
3. Il n'utilise **ni `BOOST` ni `SHIELD`**. Ce sont les deux pistes évidentes pour faire mieux.

## Ce qu'il a donné

**[notre run, 27 nov 2026]** Écrit pour la ligue Wood 2, il n'a plus été modifié et est monté tout seul Wood 2 → Wood 1 → Bronze → Silver : les ligues ajoutent `BOOST`, les collisions puis `SHIELD`, mais l'entrée reste la même.

- Parties classées de cette version : **311 victoires, 51 défaites** (86 %).
- En Silver : 3e de la ligue, score 20,1 contre 15,4 pour le boss (progression du classement 34 %).

## Ce qu'on a appris

- **`input()` vide `stdout` avant de lire, `sys.stdin.readline()` non.** Ce bot fonctionne sans `flush=True` grâce à `input()` ; ajoute-le quand même, c'est ce qui nous a fait perdre un bot Tron au tour 1.
- **Relis l'énoncé à chaque promotion.** Ici l'entrée n'a pas changé de Wood 2 à Silver, mais en Wood 3 elle n'avait que 4 nombres par tour : le bot de Wood 3 plantait en Wood 2.
- **Une version avec `BOOST` sur la plus longue ligne droite** gagnait 4 sur 4 contre le boss Silver, mais l'ancienne aussi : pas de gain mesuré, donc pas soumise (règle 8 des [bonnes pratiques](../../docs/bonnes-pratiques.md)).

## À toi

Ne le copie pas : **bats-le**. Choisis `Noussaa` comme adversaire dans l'éditeur, regarde le replay, et améliore ton bot une idée à la fois.

Ceci est un bot d'entraînement sur un jeu public. Aucun code de compétition n'ira dans ce repo.
