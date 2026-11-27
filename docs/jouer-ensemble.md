# Jouer les uns contre les autres, avec l'IA

**En bref :** on s'entraîne sur 5 jeux publics de CodinGame, et on fait s'affronter nos bots de deux façons : sur CodinGame (par pseudo) ou sur notre arène locale.

## Ce que disent les éditions précédentes

Le jeu exact de bots n'a été publié pour aucune édition. On se prépare donc à un **type** d'épreuve, pas à un jeu précis.

| Édition | Épreuve de bots | Autres épreuves |
|---|---|---|
| 2024 | Quart de finale : « AI Contest », 8 h | — |
| 2025 | Quart de finale : jeu de bots classé par TrueSkill, 6 h | Qualifications : un puzzle d'optimisation. Demi-finale : Coding Escape. Finale : Clash of Code |
| 2026 | Qualifications (3 déc) et finale (10 déc) : jeu de bots classé par TrueSkill | Quarts : Coding Escape. Demi-finales : Optimization |

À retenir : un seul jeu de bots, joué pendant plusieurs heures contre toutes les autres équipes. En 2026, c'est la première épreuve.

## Top 5 des jeux pour s'entraîner

Tous sont dans le [catalogue des jeux de bots](https://www.codingame.com/multiplayer/bot-programming).

1. **[Mad Pod Racing](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing)** : le plus simple pour commencer.
2. **[Tron Battle](https://www.codingame.com/multiplayer/bot-programming/tron-battle)** : règles courtes, 100 ms par tour, jusqu'à 4 bots par partie.
3. **Troll Farm** (Spring Challenge 2026) : un énoncé long et récent, proche du style d'un concours.
4. **Hypersonic** : jusqu'à 4 bots par partie.
5. **[Ultimate Tic-Tac-Toe](https://www.codingame.com/multiplayer/bot-programming/tic-tac-toe)** : idéal pour essayer la recherche de coups et comparer Python et C++.

Pour l'équipe qualifiée : [Code vs Zombies](https://www.codingame.com/training/optimization/code-vs-zombies) et [Mars Lander](https://www.codingame.com/multiplayer/optimization/mars-lander).

## Nos pseudos CodinGame

Pour choisir tes adversaires dans l'éditeur. Ajoute le tien dans le groupe WhatsApp.

- `sg0-degodas` (coach)
- `r00tOJ`
- `GhostOfReach`
- `Noussa`
- `YassD`
- `Assoo`
- `A7G`
- `bruhidkuser`

## Les classements

Pour voir ton rang, ta ligue et qui battre ensuite.

| Jeu | Jouer | Classement |
|---|---|---|
| Tron Battle | [jouer](https://www.codingame.com/multiplayer/bot-programming/tron-battle) | [classement](https://www.codingame.com/multiplayer/bot-programming/tron-battle/leaderboard) |
| Mad Pod Racing | [jouer](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing) | [classement](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing/leaderboard) |
| Troll Farm (Spring 2026) | [jouer](https://www.codingame.com/multiplayer/bot-programming/spring-challenge-2026-troll-farm) | [classement](https://www.codingame.com/multiplayer/bot-programming/spring-challenge-2026-troll-farm/leaderboard) |
| Hypersonic | [jouer](https://www.codingame.com/multiplayer/bot-programming/hypersonic) | [classement](https://www.codingame.com/multiplayer/bot-programming/hypersonic/leaderboard) |
| Ultimate Tic-Tac-Toe | [jouer](https://www.codingame.com/multiplayer/bot-programming/tic-tac-toe) | [classement](https://www.codingame.com/multiplayer/bot-programming/tic-tac-toe/leaderboard) |

Dans un classement, tape un pseudo dans la recherche pour retrouver un coéquipier.

Un exemple de bot à battre : [`examples/tron-battle`](../examples/tron-battle/).

## Option 1 : sur CodinGame, par pseudo

1. Tout le monde choisit **le même jeu** (par exemple Tron Battle).
2. Chacun écrit son bot avec son IA et le **soumet**. Sans soumission, personne ne peut jouer contre toi.
3. Chacun partage son **pseudo CodinGame** dans le groupe.
4. Dans l'éditeur du jeu, choisis tes adversaires par pseudo et lance des parties de test.
5. Regarde le replay, demande **une** amélioration à l'IA, resoumets.

Limites à connaître :

- Tu ne peux choisir que des adversaires de **ta ligue ou d'une ligue inférieure**.
- Les premières ligues sont en **1 contre 1**. Les parties à 3 ou 4 se débloquent plus haut, selon le jeu.
- Il n'y a pas de salle privée.

## Option 2 : sur notre arène locale (1v1v1 tout de suite)

1. Clone ce repo et lis [`arena/README.md`](../arena/README.md).
2. Écris ton bot pour le jeu d'entraînement « Récolte », en partant de `arena/bots/depart.py`.
3. Lance une partie, jusqu'à 4 bots :

```bash
python3 arena/arena.py match arena/bots/glouton.py arena/bots/depart.py arena/bots/aleatoire.py
```

4. Lance un tournoi avec classement :

```bash
python3 arena/arena.py tournoi arena/bots/glouton.py arena/bots/depart.py arena/bots/aleatoire.py
```

## La règle entre nos deux équipes

- **Dans une équipe :** on peut s'échanger les fichiers de bots.
- **Entre les deux équipes :** on s'affronte sur CodinGame par pseudo, **sans échanger de code**. On garde ainsi l'habitude que le règlement impose le 3 décembre.
