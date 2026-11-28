# Or : deux pods, un qui court et un qui gêne

- **Jeu :** Mad Pod Racing
- **Ligue :** Or
- **Date :** 2026-11-27, vers 19:30 UTC
- **Type :** astuce
- **Source :** notre essai (parties locales et parties de test)

## Erreur

En Or, chaque joueur a deux pods. La première idée est de faire courir les deux de la même façon. Mais seul le meilleur pod de chaque équipe compte pour gagner : le deuxième coureur ne sert presque à rien.

## Correction

Le pod le plus avancé court. L'autre va se placer devant le prochain checkpoint du meilleur pod adverse pour le gêner. Avant de choisir un coup, le bot simule les quatre pods sur 6 tours, chocs compris, et garde le coup qui donne la plus grande avance de notre meilleur pod sur leur meilleur pod.

## Règle

Avec deux pods, donne deux rôles : un coureur et un bloqueur. Note chaque coup par « notre meilleur pod moins leur meilleur pod ».

## Preuve

Sur 32 parties locales contre la même version avec deux coureurs et sans bloqueur : 26 victoires. Contre le boss de l'Or en partie de test : victoire en 252 tours. Entrée en Or le 27 nov à 19:26 UTC, promotion en Légende à 23:54 UTC.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
