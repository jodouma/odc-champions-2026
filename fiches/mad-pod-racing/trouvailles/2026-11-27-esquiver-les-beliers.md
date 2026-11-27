# Bronze : certains adversaires foncent sur toi, prévois les chocs

- **Jeu :** Mad Pod Racing
- **Ligue :** Bronze
- **Date :** 2026-11-27
- **Type :** piège
- **Source :** notre essai (6 parties classées contre le même adversaire, puis rejouées)

## Erreur

Notre bot ignorait l'adversaire. Un joueur du Bronze vise notre pod pendant 3 ou 4 tours quand on est devant et à 1 000 à 4 000 unités. Ses chocs du premier tour de circuit nous ont coûté environ 18 tours, et on a perdu les 3 parties où on partait du côté 1.

## Correction

Quand l'adversaire est à moins de 3 000 unités, le bot essaie 7 coups (le coup normal, tourner de 9° ou 18° à gauche ou à droite, freiner, pousser l'adversaire). Il joue chacun 6 tours en avance dans un simulateur avec les vraies collisions, une fois avec un adversaire qui fait la course et une fois avec un adversaire qui fonce sur lui. Il garde le coup qui laisse la meilleure avance dans le pire des deux cas. Le coup normal reste, sauf si un autre fait nettement mieux.

## Règle

À partir du Bronze, quand l'adversaire est proche, regarde quelques tours en avance avec les collisions avant de choisir ton coup.

## Preuve

Les 6 mêmes parties rejouées sur le serveur (même carte, même côté, même adversaire) : 3 victoires sur 6 avant, 6 sur 6 après. En local, 200 parties contre une imitation de cet adversaire : 64 % → 78 % avec ce seul changement, 93 % avec aussi la reconnaissance des circuits.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
