# Légende : la poussée monte à 200 et le BOOST est commun aux deux pods

- **Jeu :** Mad Pod Racing
- **Ligue :** Légende
- **Date :** 2026-11-28
- **Type :** changement de règles
- **Source :** l'énoncé de la Légende et notre essai

## Erreur

Après la promotion, le bot de l'Or a continué à jouer sans erreur, donc on a cru que rien n'avait changé. En réalité il limitait encore sa poussée à 100 et comptait un BOOST par pod.

## Correction

On a relu l'énoncé de la Légende : « La puissance maximale est maintenant de 200 au lieu de 100 » et le nombre de BOOST est commun entre les deux pods. Le bot pousse maintenant jusqu'à 200 et garde l'unique BOOST de l'équipe pour le pod qui court.

## Règle

Un bot qui tourne encore après une promotion n'est pas un bot à jour : relis l'énoncé ligne par ligne, même quand le format d'entrée n'a pas changé.

## Preuve

Version de l'Or laissée telle quelle : rang 1 977 sur 2 366 en Légende, score 15,8 (lu à 10 % du classement, donc chiffre encore instable). Même bot avec seulement ces deux corrections : rang 270 sur 2 366, score 36,34, classement à 100 %.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
