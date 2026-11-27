# Budget temps : la moitié de la limite, pas plus

- **Jeu :** Tron Battle
- **Ligue :** Bois 2
- **Date :** 2026-11-27, vers 13:40 UTC
- **Type :** piège
- **Source :** notre essai

## Erreur

Le bot se donnait 70 ms de réflexion par tour pour une limite de 100 ms. Sur le serveur, des tours ont été mesurés entre 77 et 104 ms, donc au-delà de la limite.

## Correction

Budget ramené à 55 ms, puis à 40 ms, avec une vérification de l'horloge plus fréquente.

## Règle

Prends environ la moitié du temps permis et lis le pire tour de chaque journal de test, pas la moyenne.

## Preuve

Avec 40 ms au lieu de 50 ms : 51,0 % de victoires sur 200 parties locales, donc aucune perte de force mesurable.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
