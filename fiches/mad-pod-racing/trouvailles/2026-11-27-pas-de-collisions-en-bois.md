# Pas de collisions avant le Bronze : inutile de bloquer en Bois

- **Jeu :** Mad Pod Racing
- **Ligue :** Bois 2 et Bois 1 (collisions vues à partir du Bronze)
- **Date :** 2026-11-27
- **Type :** changement de règles
- **Source :** notre essai (parties de test avec un bot « sonde »)

## Erreur

On voulait bloquer ou pousser l'adversaire dès le Bois 2. L'énoncé ne dit rien des collisions avant le Bronze, et on supposait qu'elles existaient.

## Correction

Un bot sonde qui fonce sur l'adversaire à chaque tour et écrit les deux positions dans la sortie d'erreur. Ensuite on rejoue la partie dans un simulateur, avec et sans collisions, et on compare.

## Règle

En Bois, les pods se traversent : seule la vitesse compte. Le blocage ne sert qu'à partir du Bronze, quand l'énoncé annonce « Les pods peuvent désormais entrer en collision ».

## Preuve

Bois 2 : la sonde passe à 583 unités du boss sans rebond (le contact serait à 800). Les 3 parties (503 tours) se rejouent sans aucune erreur avec les collisions coupées. Bois 1 : passage à 45 unités, toujours sans rebond.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
