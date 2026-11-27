# Ultimate Tic-Tac-Toe — bonnes pratiques

**En bref :** ce que `Assoo` a appris sur [Ultimate Tic-Tac-Toe](https://www.codingame.com/multiplayer/bot-programming/tic-tac-toe) (27 nov 2026) : 1er sur 1 325 en Bois, **promu en Bronze**. Ce sont des **idées et des méthodes**, pas du code : écris ton propre bot.

Les règles valables pour tous les jeux sont dans [nos bonnes pratiques](../bonnes-pratiques.md). Les astuces de [Tron Battle](../tron-battle/bonnes-pratiques.md) (méthode de travail, temps, API) valent aussi ici.

**Ligue par ligue :** à chaque promotion, une section avec ce qui a marché et les erreurs à ne plus refaire.

---

## Le jeu selon la ligue

- **Bois : un morpion 3 × 3 classique.**
- **Bronze et au-dessus : les vraies règles « Ultimate ».** Neuf petits morpions dans un grand. La case où tu joues décide du petit plateau où l'adversaire doit jouer. **L'entrée reste la même**, mais il faut un nouveau bot.
- **Lis le code de l'arbitre** (publié sur GitHub) pour les cas limites. Il tranche par exemple :
  - si le petit plateau imposé est **gagné ou plein**, on peut jouer **n'importe où** ;
  - si le grand plateau est **plein sans gagnant**, gagne celui qui a **le plus de petits plateaux**.

---

## Bois → Bronze

**Résultat : promu en Bronze**, 1er sur 1 325 en Bois. Minimax parfait en C++ : **48 parties de classement, 29 V / 19 N / 0 D**, aucun temps dépassé, score **21,67** contre **14,59** pour le boss.

### Ce qui a marché
- **Lire l'arbitre d'abord.** Il règle les cas limites mieux que l'énoncé (voir plus haut).
- **Un arbitre local pour les deux jeux de règles** (3 × 3 et Ultimate). Les parties de test sur le site ne servent qu'à vérifier contre le boss.
- **Le 3 × 3 est résolu.** Minimax complet ; entre coups de même valeur, joue celui qui laisse à l'adversaire **le plus de réponses perdantes**. Contre un bot parfait on fait nul ; contre les autres on gagne.
- **Écrire le bot de la ligue suivante pendant le classement.** Le classement en Bois a pris environ 1 h : le bot Bronze était prêt à la promotion.
- **Une seule boucle de suivi en arrière-plan**, qui lit le champ `limits` des réponses.
- **CodinGame compile le C++ sans `-O`.** Ajouter `#pragma GCC optimize("O3")` en tête du fichier a **doublé** la recherche (7 à 10 k → 15 à 25 k itérations par tour).

### Erreurs à ne plus refaire

| Ce qui s'est passé | La règle |
|---|---|
| On surveillait un PID lu dans `ps` : c'était la boucle d'un autre jeu | Surveille ton propre processus (`$!` juste après le lancement, ou l'identifiant de ta tâche) |
| Un `ps aux` sans filtre montrait les commandes `curl` d'autres sessions avec **le jeton API en clair** | Ne lance jamais `ps` sans filtre. Ne mets **jamais** le jeton dans les arguments d'une commande : passe-le par un fichier d'en-tête (`curl -H @fichier`) |
| Des tests lancés en parallèle écrivaient des lignes sans étiquette : résultats mélangés | Un fichier de sortie par expérience |
| Une position de test écrite à la main était illégale : la réutilisation de l'arbre semblait cassée | Construis les positions de test à partir de vraies parties |
| Des séries de 40 parties ont trompé (20-17, puis 40-40) | Au moins **80 parties** avant de garder un changement |
| Un budget de 85 ms a été mesuré à 93 ms | Garde **au moins 20 ms de marge** (maintenant 80 ms sur 100) |
| Dans l'API, `my_position` vaut 0 aussi en cas de **nul** | Compare avec la position de l'adversaire pour savoir si c'est une victoire ou un nul |
| Une boucle de suivi de 30 tours s'est arrêtée à 80 % (le classement Bois a pris environ 1 h) | Prévois des boucles d'au moins 1 h, qui n'affichent que les changements |

---

## Bronze → Argent

*En cours (27 nov 2026) : le boss Bronze est fort (2e sur 5 452, score 27,23). La v6 (MCTS + solveur de fin de partie + réutilisation de l'arbre d'un tour à l'autre + `O3`) a battu le boss 2 fois sur 2 en test ; soumise à 17:04 (heure de Tunis).*

### Ce qui a marché

### Erreurs à ne plus refaire

---

Une nouvelle section sera ajoutée à chaque promotion.
