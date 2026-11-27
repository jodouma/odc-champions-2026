# Construire un bot CodinGame : guide pratique

Pour des étudiants de niveaux mixtes. Valable pour tout jeu de bot ; exemples tirés de nos essais d'entraînement (27 nov 2026) sur le jeu Tron Battle.
**Légende :** **[notre run]** = mesuré par nous, date et heure UTC données · **[source]** = recherche, lien donné · *non vérifié* = pas contrôlé.
Aucun code de compétition n'est publié ici.

---

## Les 10 règles dès la première minute

1. **Lis tout l'énoncé** : entrées, sorties, **temps par tour** (100 ms en Tron), ce qui se passe quand un joueur est éliminé. Le premier tour est parfois plus long (1000 ms en Tron selon un joueur, *non vérifié* par nous) [[forum]](https://forum.codingame.com/t/tron-battle-aka-line-racing-multiplayer-challenge-discussion/49?page=3).
2. **Commence par un bot « jamais illégal »** : un coup autorisé, sans stratégie. Une sortie invalide, un crash ou un temps dépassé = défaite.
3. **Teste en local avant d'utiliser le site** : un petit simulateur contre un bot aléatoire et contre ta version précédente. Gratuit, sans limite.
4. **Tiens un journal de versions** : une ligne par version (quoi, pourquoi, résultat) et garde le code de chacune.
5. **Un seul changement à la fois.** Sinon tu ne sais pas ce qui a aidé ou nui.
6. **Juge sur 100 parties ou plus, avec les départs inversés.** Une victoire ou une défaite isolée ne prouve rien.
7. **Prends la moitié du temps permis, pas plus.** Le serveur est plus lent et irrégulier que ton ordinateur.
8. **Ne soumets que ce qui est mesuré meilleur, et jamais quand ta version live est près de la promotion** : une soumission relance tout le classement.
9. **Lis les défaites par cause**, pas une par une : cherche le tour où la partie a basculé, souvent bien avant la fin.
10. **Chaque bug trouvé devient un test qui échoue d'abord**, puis on le corrige.

---

## Le détail

### Démarrer
- **Bot v1 « jamais illégal ».** Il suffit parfois à gagner : **[notre run, 27 nov 2026 ~13:00 UTC]** en Wood 2 de Tron, nos 4 premiers matchs de test ont été gagnés parce que l'adversaire a joué un coup illégal.
- **Bot v2 : une idée simple et bonne.** Pour Tron : le territoire de Voronoï (les cases où j'arrive avant l'adversaire). Un bot Python de 78 lignes bâti là-dessus a atteint le top 5 % en 2016 [[source]](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/). **[notre run]** notre v2 Python (remplissage + Voronoï) a été promu de Wood 2 à 14:01 UTC, avec un score d'environ 30 contre environ 19 pour le boss.
- **La meilleure évaluation bat la recherche la plus profonde** [[a1k0n]](https://www.a1k0n.net/2010/03/04/google-ai-postmortem.html). Soigne d'abord la façon de noter une position.

### Tester
- **Local d'abord, site ensuite.** Limites du site pour ce compte **[notre run]** : 10 parties de test par minute, 5 soumissions par 5 minutes, 120 requêtes API par minute. Lis `limits` dans chaque réponse.
- **Mesure le pire tour**, pas la moyenne, dans les logs de test.
- **Ton `stderr` n'est visible que dans les parties de test**, pas dans les parties classées.
- **Parties miroir.** Beaucoup de parties se jouent au départ : le même placement gagne dans les deux sens, quel que soit le bot. Compare avec départs inversés ; juge sur 100+ parties.

### Lire une défaite
1. Rejoue les images 10 à 60, pas seulement la dernière : c'est là que la place se perd.
2. Demande : coup illégal ? trop lent ? ou simplement moins bon ?
3. Classe automatiquement toutes les défaites par cause (un petit script suffit).
4. Rejoue la partie avec la nouvelle version (`replay_game_id`, API) **vite** : l'API refuse si l'adversaire a été resoumis.

### Python ou C++ ?
- **Python tant que l'idée prime.** Un joueur est monté en Legend en Python sans recherche [[forum]](https://forum.codingame.com/t/tron-battle-aka-line-racing-multiplayer-challenge-discussion/49?page=2).
- **C++ quand la recherche limite la force.** **[notre run]** : v3 en C++ (alpha-bêta, profondeur 7 à 10 coups) a battu notre v2 Python 159-41 sur 200 parties jumelées (27 nov, ~14:05 UTC) ; avec 55 ms elle bat la même version à 12 ms 15 fois sur 20.
- **Classement actuel de Tron (27 nov 2026, API)** : les 20 premiers utilisent C++, C, Rust, C# ou JavaScript, aucun Python. En Silver, Python domine encore (49 des 100 premiers).

### Travailler avec un agent LLM
- Donne : l'énoncé tel quel, le format d'entrée/sortie, la limite de temps, le fichier actuel.
- Une demande précise à la fois ; fais d'abord écrire un simulateur.
- **Relis le code, relance les tests, mesure le temps.** Un code « qui a l'air bon » peut dépasser la limite.
- **Fais relire le code deux fois** (revue statique) : **[notre run]** elle a trouvé 2 vrais bugs que plus de 1000 parties simulées n'avaient pas montrés.
- Demande des sources, vérifie-les.

### À plusieurs sur un seul emplacement
- **Une seule personne soumet à la fois**, les autres proposent des changements.
- Annonce chaque soumission (version, changement, résultat attendu) : elle remplace la précédente et relance le classement.
- Journal commun ; jamais de jeton ou de mot de passe partagé.

---

## Erreur → correction → règle (nos leçons, Tron, 27 nov 2026)

| Erreur | Correction | Règle |
|---|---|---|
| Premier build C++ local en échec (`bits/stdc++.h` absent sur Mac) ; l'arène a compté 10 « mauvaises sorties » | Un fichier d'en-tête de remplacement local | Un 0/10 veut dire « outil cassé », pas « mauvais bot » : vérifie que ça compile avant de croire un résultat |
| `cmd 2>&1 >/dev/null` dans zsh n'isole pas `stderr` | `cmd >/dev/null 2>fichier ; tail fichier` | Pour déboguer, écris `stderr` dans un fichier |
| Budget 70 ms : le serveur a mesuré 77 à 104 ms (local 72) | Budget 55 ms, puis test 40 ms | Prends environ la moitié du temps permis et lis le pire `t=` de chaque log |
| Un pic isolé de 89,6 ms avec un budget de 50 ms | Regarde le mode du tour lent et son nombre de nœuds : pic isolé = machine, pics répétés = code | Mesure ce que coûte un budget plus bas avant de croire que la profondeur est précieuse (40 ms : 51,0 % contre 50 ms sur 200 parties = aucun coût) |
| Voronoï simple : compte des cases derrière une porte d'une case comme utilisables | Points d'articulation (Tarjan) : seule la meilleure branche sans issue compte | Une bonne évaluation vaut plus que de la vitesse (14 victoires sur 20 contre la version simple) |
| On cherchait les défaites dans la fin de partie | Rejouer les images 10 à 60 | 74 des 88 défaites de la v2 (Wood 2, mesuré 14:00 UTC) étaient une course au territoire perdue **tôt** ; 27 dès les 20 premiers tours, souvent à cause du départ |
| Un tweak d'évaluation jugé sur 20 parties | Plus de parties jumelées | Un terme « mur » a donné 53 %, 56 %, 52,7 % sur 100/100/300 parties : jamais clair seul. Décide sur l'ensemble, ne règle pas sur 20 parties |
| Table de transposition ajoutée « parce que le livre le dit » | Mesure | Neutre ici (51 % sur 200 parties) : ne suppose pas qu'une accélération classique aide |
| Resoumission pendant que la version live finissait son classement | Attendre la promotion, puis soumettre | Une soumission **relance** les parties classées ; ne resoumets jamais près d'une promotion |
| Un bug vu seulement en revue (un survivant marche sur la case d'un joueur mort, 3-4 joueurs ; arrêt anticipé d'une recherche) | Test qui échoue d'abord, puis correction | Chaque trouvaille de revue devient un test |
| Rejeu d'une vieille défaite refusé (`INVALID_OPPONENT`) | — | Rejoue peu après la partie |
| L'API affichait encore l'ancien langage juste après une soumission | Relire `GET /submissions` (`current: true`) | Vérifie ce qui est vraiment en ligne |

**Défaites mesurées (v2, Wood 2, lu 27 nov 2026 14:00 UTC, 212 parties classées, 88 perdues) :** 74 course au territoire, 11 fin de remplissage, 3 coupés au contact, 0 temps dépassé, 0 coup illégal. Classement automatique, pas vérifié partie par partie.
**v3 (C++, Wood 1, lu 14:36 UTC) :** 94 victoires, 4 défaites, toutes des courses au territoire (3 dès le départ).

---

## Par jeu

- **Tron Battle :** [Tron Battle — bonnes pratiques](tron-battle/bonnes-pratiques.md) (stratégie v1 à v4, temps, tests, API).

Quatre autres jeux sont en cours (Mad Pod Racing, Troll Farm, Hypersonic, Ultimate Tic-Tac-Toe). Leurs trouvailles seront ajoutées ici.

---

## Sources
- [a1k0n, Google AI Challenge 2010](https://www.a1k0n.net/2010/03/04/google-ai-postmortem.html) · [vks.ai, 78 lignes](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/) · [forum CodinGame Tron](https://forum.codingame.com/t/tron-battle-aka-line-racing-multiplayer-challenge-discussion/49)
