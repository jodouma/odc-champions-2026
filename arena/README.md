# Arène locale : faire combattre nos bots

Une petite arène pour faire jouer **vos bots les uns contre les autres sur votre PC**, à 2, 3 ou 4 dans le même match. Même principe que CodinGame : le bot lit l'état du jeu sur l'entrée standard et écrit **une action par tour**.

- **Rien à installer à part Python 3.8+.** Pas de Java, pas de Maven.
- **N'importe quel langage :** Python, C++, Java, JS… tant que le bot se lance en ligne de commande.
- **Limite de temps par tour :** 100 ms par défaut (1 s au 1er tour). Un bot trop lent est éliminé.

> Le jeu « Récolte » est un jeu d'entraînement inventé pour ce repo. Ce n'est pas le jeu du concours : il sert à s'habituer au protocole, au temps limité et aux matchs à plusieurs.

## Installation

Il faut seulement Python 3.8 ou plus récent.

| Système | Installer Python | Vérifier |
|---|---|---|
| **macOS** | `brew install python` ou <https://www.python.org/downloads/> | `python3 --version` |
| **Windows** | <https://www.python.org/downloads/> (cocher « Add python.exe to PATH ») | `py --version` |
| **Linux** | déjà installé en général (`sudo apt install python3` sinon) | `python3 --version` |

Puis récupérer le repo :

```bash
git clone https://github.com/jodouma/odc-champions-2026.git
cd odc-champions-2026
```

Sous **Windows**, remplacer `python3` par `py` dans les commandes ci-dessous.

## Lancer un match (2 à 4 bots)

```bash
python3 arena/arena.py match arena/bots/glouton.py arena/bots/depart.py arena/bots/lent.py
```

```text
Résultat (graine 1)
Rang  Bot                  Score  État
1     glouton                 72
2     depart                   0
3     lent                     0  éliminé au tour 5 : temps dépassé (> 100 ms)
```

Options utiles :

- `--voir` : affiche la grille à chaque tour (A, B, C, D = les bots ; 1–3 = les olives).
- `--debug` : affiche ce que vos bots écrivent sur stderr.
- `--graine 7` : une autre partie (même graine = exactement la même partie).
- `--timeout 50` : 50 ms par tour, comme beaucoup de jeux CodinGame.

## Lancer un tournoi (classement)

Chaque groupe de 3 bots joue plusieurs parties, et chaque bot passe par chaque coin de départ.

```bash
python3 arena/arena.py tournoi arena/bots/glouton.py arena/bots/depart.py arena/bots/aleatoire.py
```

```text
Rang  Bot                  Points  1ers  Matchs  Score moy.  Éliminé
1     glouton                  18     9       9        70.3        0
2     aleatoire                 9     0       9         7.3        0
3     depart                    0     0       9         0.0        0
```

Ajoutez votre bot à la liste, par exemple `moi=mon_bot.py`.

- `--joueurs 2` : des duels au lieu de matchs à 3.
- `--parties 5` : plus de graines par groupe (classement plus fiable, plus long).

## Comment donner son bot

| Bot | À écrire |
|---|---|
| Python | `mon_bot.py` (lancé avec le même Python que l'arène) |
| C++ | compiler d'abord : `g++ -O2 -o mon_bot mon_bot.cpp`, puis `./mon_bot` (Windows : `mon_bot.exe`) |
| Java | `"java -cp dossier Main"` (entre guillemets) |
| JavaScript | `"node mon_bot.js"` |
| Un nom au choix | `ali=mon_bot.py` |

Exemple en C++ : `g++ -O2 -o arena/build/glouton arena/bots/glouton.cpp`, puis `cpp=arena/build/glouton`.

## Les règles de « Récolte »

- Grille de **13 × 9**. Chaque bot part d'un coin. **100 tours.**
- Des olives (valeur 1, 2 ou 3) sont sur la grille ; il en apparaît 1 ou 2 tous les 3 tours.
- Tous les bots bougent **en même temps**. Finir son tour sur une olive = gagner sa valeur.
- **Deux bots sur la même olive au même tour : personne ne la gagne**, elle disparaît.
- Sortir de la grille = rester sur place. Plusieurs bots peuvent être sur la même case.
- **Éliminé** si : temps dépassé, action invalide, ou plantage. Un éliminé est classé derrière les autres.
- À la fin, le plus gros score gagne.

### Entrées

Au 1er tour seulement :

```text
<nb_joueurs> <mon_id>
<largeur> <hauteur> <nb_tours>
```

À chaque tour :

```text
x y score actif        (une ligne par joueur, dans l'ordre des id ; actif = 1 ou 0)
k                      (nombre d'olives)
x y valeur             (k lignes)
```

`x` va de 0 à gauche à 12 à droite ; `y` de 0 en haut à 8 en bas.

### Sortie : une ligne par tour

- `UP`, `DOWN`, `LEFT`, `RIGHT` ou `WAIT`
- `MOVE x y` : un pas vers la case (x, y), d'abord horizontalement.

## Les bots d'exemple (`arena/bots/`)

| Bot | Ce qu'il fait |
|---|---|
| `depart.py` | Le squelette `starters/python/bot.py` avec `read_turn` adapté au jeu. Il attend : à vous de l'améliorer. |
| `glouton.py` / `glouton.cpp` | Va vers l'olive qui rapporte le plus par case parcourue. |
| `aleatoire.py` | Un pas au hasard. |
| `lent.py` | Réfléchit 0,5 s au tour 5 : montre l'élimination pour temps dépassé. |

## Pièges classiques

- **Vider le tampon :** `print(..., flush=True)` en Python, `std::endl` en C++. Sinon l'arène ne voit rien → temps dépassé.
- **Lire toutes les lignes du tour**, même celles dont on n'a pas besoin.
- Le squelette `starters/python/bot.py` tel quel lit une seule ligne par tour : adaptez `read_turn` comme dans `depart.py`.
- **Le debug va sur stderr**, jamais sur stdout.
- Deux gloutons identiques visent la même olive et la perdent tous les deux : pensez aux adversaires !

## Vérifier que l'arène marche

```bash
python3 -m unittest discover arena
```
