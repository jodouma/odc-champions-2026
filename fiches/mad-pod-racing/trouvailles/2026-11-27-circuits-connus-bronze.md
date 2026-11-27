# Bronze : les circuits viennent d'une liste fixe, reconnais-les au tour 1

- **Jeu :** Mad Pod Racing
- **Ligue :** Bronze
- **Date :** 2026-11-27
- **Type :** astuce
- **Source :** notre essai (39 cartes relevées dans nos parties) et la liste classique de Coders Strike Back

## Erreur

Au premier tour, le bot ne connaît que le prochain checkpoint. Pendant tout le tour 1 il ne peut pas tourner en avance vers le checkpoint suivant : il dépasse les checkpoints et perd du temps.

## Correction

Les 39 cartes Bronze relevées n'ont que 9 dessins différents. On les retrouve tournés (le départ change) et décalés d'environ 50 unités. Ce sont ceux de la liste classique de Coders Strike Back (13 dessins). Au tour 1, la position de départ et le premier checkpoint suffisent à reconnaître le circuit, donc à connaître tout l'ordre des checkpoints. Chaque vrai checkpoint qui apparaît est comparé à la prévision ; s'il ne colle pas, on oublie la prévision.

## Règle

En Bronze, reconnais le circuit dès le tour 1 au lieu d'attendre la fin du premier tour pour l'apprendre.

## Preuve

Ce seul changement : 64 % → 82 % de victoires sur 200 parties locales contre un adversaire qui pousse (même simulateur, mêmes cartes, côtés inversés).

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
