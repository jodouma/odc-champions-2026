# Un départage par impasses a prolongé deux replays, sans changer le gagnant

- **Jeu :** Tron Battle
- **Ligue :** Bois 1
- **Date :** 2026-11-27
- **Type :** mesure
- **Source :** tests et replays CodinGame 929715417 et 929715416

## Erreur

Le nombre de cases accessibles ne distingue pas deux régions de taille comparable dont l'une contient davantage de culs-de-sac. Plusieurs parties se sont terminées quand le bot n'avait plus de coup légal.

## Correction

Une variante a conservé les cases accessibles comme critère principal, puis a départagé les choix en pénalisant les cases libres accessibles qui ont au plus un voisin libre.

## Règle

Parmi des choix qui préservent une surface comparable, compter les impasses peut aider à éviter une poche, mais cela reste un départage à vérifier sur plusieurs départs.

## Preuve

- Sur le replay 929715417, la variante de base a perdu au frame 273 (test 929718878); la variante avec départage a perdu au frame 317 (test 929720800), soit 44 frames plus tard. Les deux ont perdu.
- Sur le replay 929715416, les deux variantes ont battu A7G 100-90. La variante de base a terminé au frame 386 (test 929722104); l'autre a survécu jusqu'au frame 513 (test 929721785), soit 127 frames de plus.
- Plus tard, en Bronze, cette variante a perdu contre le bot classé premier au frame 333 (test 929724873). Ces deux comparaisons ne prouvent ni que le départage cause à lui seul les écarts observés, ni qu'il améliore le taux de victoire.

## Confirmé par

- Aucun résultat indépendant pour le moment.
