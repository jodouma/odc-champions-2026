# Construire un bot CodinGame : guide pratique

Pour des étudiants de niveaux mixtes. Valable pour tout jeu de bot ; exemples tirés de nos essais d'entraînement du 27 nov 2026 sur cinq jeux.
**Légende :** **[notre run]** = mesuré par nous, date et heure UTC données · **[source]** = recherche, lien donné · *non vérifié* = pas contrôlé.
Aucun code de compétition n'est publié ici.

---

## Les 10 règles dès la première minute

1. **Lis tout l'énoncé, et relis-le après chaque promotion.** Entrées, sorties, **temps par tour**, nombre de tours, ce qui se passe quand un joueur est éliminé. Une promotion peut changer les règles ou le format d'entrée : l'ancienne version devient « un nouveau bot ». **[notre run, 27 nov 2026]** Troll Farm : 100 tours codés en dur, la ligue suivante en compte 300 → 5 défaites sur 5. Mad Pod Racing : l'entrée de Wood 2 change, la v1 ne joue plus. Ultimate Tic-Tac-Toe : la ligue Bronze passe du 3×3 au 9×9.
2. **Commence par un bot « jamais illégal »** : un coup autorisé, sans stratégie. Une sortie invalide, un crash ou un temps dépassé = défaite. Lis **un journal de test** avant de concevoir : le jeu a parfois un adversaire que l'API ne montre pas (Mad Pod Racing, Wood 3).
3. **Teste en local avant d'utiliser le site** : un petit simulateur contre un bot aléatoire et contre ta version précédente. Gratuit, sans limite ; les parties de test du site sont comptées par heure.
4. **Tiens un journal de versions** : une ligne par version (quoi, pourquoi, résultat) et garde le code de chacune.
5. **Un seul changement à la fois**, puis vérifie dans le journal que le comportement visé a bien eu lieu (Troll Farm : un réglage « entraîne plus de trolls » n'a rien changé car il n'y avait plus de ressources).
6. **Juge sur 100 parties ou plus, avec les départs inversés.** Une victoire ou une défaite isolée ne prouve rien ; une victoire parce que l'adversaire a dépassé le temps ne dit rien de ta force.
7. **Prends la moitié du temps permis, pas plus.** Le serveur est plus lent et irrégulier que ton ordinateur.
8. **Ne soumets que ce qui est mesuré meilleur, et jamais pendant que ta version live finit son classement** : une soumission relance toutes les parties classées. Lis le rang seulement à 50 % des parties jouées ; avant, il ne veut rien dire (Mad Pod Racing : rang 13 257, puis 515, puis 207, puis 1 pour la même soumission).
9. **Lis les défaites par cause**, pas une par une : cherche le tour où la partie a basculé, souvent bien avant la fin.
10. **Chaque bug devient un test qui échoue d'abord**, puis on le corrige. Un « timeout » alors que les tours précédents étaient rapides est un plantage jusqu'à preuve du contraire : compile avec les vérificateurs (ASan/UBSan) et affiche l'entrée lue sur `stderr`.

---

## Où on en est (27 nov 2026, 16:19 UTC, relevés API ; chaque ligne porte la date de sa lecture, voir « Par jeu »)

| Jeu | Ligue | Langage de la version live | Versions |
|---|---|---|---|
| Tron Battle | Bronze (depuis 16:10 UTC ; rang 1, 14 % du classement) | C++ (Python avant) | 3 écrites, 2 soumises |
| Mad Pod Racing | Wood 1 (depuis 15:00 UTC ; rang 1, 80 % du classement) | C++ | 2 soumises, 1 prête non soumise |
| Troll Farm (Spring Challenge 2026) | Bronze (depuis 14:47 UTC ; rang 1, 51 %) | Python 3 | 3 soumises, 1 candidate non soumise |
| Hypersonic | Wood 1 (depuis 16:07 UTC ; rang 1, 18 %) | C++ | 1 soumise |
| Ultimate Tic-Tac-Toe | Bronze (depuis 15:29 UTC ; rang 1, 31 %) | C++ | 2 soumises, 1 candidate non soumise |

Ligues et classements : relevés API de 16:19 UTC (le score n'est pas final avant 100 %). Les fiches « Par jeu » citent les fichiers d'équipe, lus de 14:37 à 16:12 UTC. Fiches « Objectif Bronze » par jeu : `OBJECTIF_BRONZE.md`.

---

## Le détail

### Démarrer
- **Bot v1 « jamais illégal ».** Il suffit parfois : **[notre run, 27 nov ~13:00 UTC]** en Wood 2 de Tron, nos 4 premiers matchs de test ont été gagnés parce que l'adversaire a joué un coup illégal.
- **Bot v2 : une idée simple et bonne**, comme « la valeur d'un objectif = ce qu'il rapporte par tour de trajet » (Troll Farm) ou le territoire de Voronoï (Tron : un bot Python de 78 lignes bâti là-dessus a atteint le top 5 % en 2016 [[source]](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/)).
- **La meilleure évaluation bat la recherche la plus profonde** [[a1k0n]](https://www.a1k0n.net/2010/03/04/google-ai-postmortem.html). Soigne d'abord la façon de noter une position.

### Tester
- **Local d'abord, site ensuite.** Limites du site pour ce compte **[notre run]** : 10 parties de test par minute, 5 soumissions par 5 minutes, 120 requêtes API par minute. Lis `limits` dans chaque réponse.
- **Mesure le pire tour**, pas la moyenne, dans les logs de test. Ton `stderr` n'est visible que dans les parties de test.
- **Parties miroir.** Beaucoup de parties se jouent au départ ; compare avec départs inversés.
- **Relance les tests quand tu changes le code par script** : un `sed` raté a laissé un budget inchangé (Ultimate Tic-Tac-Toe) ; relis le résultat avec `grep`.

### Lire une défaite
1. Rejoue les images 10 à 60, pas seulement la dernière.
2. Demande : coup illégal ? trop lent ? ou simplement moins bon ?
3. Classe automatiquement toutes les défaites par cause (un petit script suffit).
4. Rejoue vite : l'API refuse le rejeu si l'adversaire a été resoumis.

### Python ou C++ ?
- **Python tant que l'idée prime.** **[notre run]** Troll Farm en Python 3 : 1er de Bronze à 31 % du classement (15:40 UTC) ; en Tron, un joueur est monté en Legend en Python sans recherche [[forum]](https://forum.codingame.com/t/tron-battle-aka-line-racing-multiplayer-challenge-discussion/49?page=2).
- **C++ dès que la recherche limite la force.** **[notre run]** Tron : la v3 en C++ (alpha-bêta) a battu la v2 Python 159-41 sur 200 parties jumelées (27 nov, ~14:05 UTC). Les 20 premiers de Tron (API, 27 nov) utilisent C++, C, Rust, C# ou JavaScript, aucun Python.

### Travailler avec un agent LLM
- Donne : l'énoncé tel quel, le format d'entrée/sortie, la limite de temps, le fichier actuel. Une demande précise à la fois ; fais d'abord écrire un simulateur.
- **Relis le code, relance les tests, mesure le temps.** Fais relire deux fois : **[notre run]** la revue a trouvé 2 vrais bugs que plus de 1000 parties simulées n'avaient pas montrés (Tron).
- Demande des sources, vérifie-les.

### À plusieurs sur un seul emplacement
- **Une seule personne soumet à la fois**, les autres proposent. Annonce chaque soumission (version, changement, résultat attendu) : elle remplace la précédente.
- Journal commun ; jamais de jeton ou de mot de passe partagé.

---

## Erreur → correction → règle (Tron, 27 nov 2026)

| Erreur | Correction | Règle |
|---|---|---|
| Premier build C++ local en échec ; l'arène a compté 10 « mauvaises sorties » | Fichier d'en-tête de remplacement | Un 0/10 veut dire « outil cassé » : vérifie que ça compile |
| Budget 70 ms : le serveur a mesuré 77 à 104 ms | Budget 55 ms, puis 40 ms | Moitié du temps permis ; lis le pire `t=` de chaque log. 40 ms : 51,0 % contre 50 ms sur 200 parties, aucun coût |
| Voronoï simple : compte des cases derrière une porte d'une case | Points d'articulation (Tarjan) | Une bonne évaluation vaut plus que de la vitesse (14 victoires sur 20 contre la version simple) |
| On cherchait les défaites dans la fin de partie | Rejouer les images 10 à 60 | 74 des 88 défaites de la v2 (Wood 2, 14:00 UTC) : course au territoire perdue **tôt** |
| Un terme d'évaluation jugé sur 20 parties | Plus de parties jumelées | 53 %, 56 %, 52,7 % sur 100/100/300 parties : jamais clair seul |
| Table de transposition ajoutée « parce que le livre le dit » | Mesure | Neutre (51 % sur 200 parties) |
| Resoumission pendant le classement de la version live | Attendre la promotion | Une soumission **relance** les parties classées |
| Bug vu seulement en revue (3-4 joueurs ; arrêt anticipé d'une recherche) | Test qui échoue d'abord | Chaque trouvaille de revue devient un test |

**Défaites mesurées (v2, Wood 2, 14:00 UTC, 212 parties classées, 88 perdues) :** 74 course au territoire, 11 fin de remplissage, 3 coupés au contact, 0 temps dépassé. Classement automatique, pas vérifié partie par partie.

---

## Par jeu

Une fiche par jeu, lue dans les fichiers de l'équipe du jeu à l'heure indiquée. Les chiffres sont ceux écrits dans ces fichiers.

### Tron Battle — Bronze depuis 16:10 UTC (API 16:19) ; Wood 1 dès 14:01:12 (STATUS lu à 14:37 UTC)
- **Live :** v3 C++, alpha-bêta + Voronoï avec points d'articulation ; la v2 Python (remplissage + Voronoï) a été promue de Wood 2 avec un score d'environ 30 contre environ 19 pour le boss. À 14:37 UTC : 46 % du classement, rang 1 sur 562, 94 victoires, 4 défaites.
- **Erreur → correction → règle :** resoumission pendant un classement → on a attendu la promotion → ne resoumets jamais près d'une promotion.
- **Erreur → correction → règle :** défaites cherchées en fin de partie → rejeu des images 10-60 → 74 des 88 défaites étaient une course au territoire perdue tôt.
- **Erreur → correction → règle :** bugs vus en revue → tests qui échouent d'abord → les revues trouvent ce que 1000 parties simulées ne voient pas.
- **Entre ligues :** aucun changement noté dans nos fichiers entre Wood 2 et Wood 1 ; plus de joueurs par partie en Silver/Gold : *non vérifié* (forum 2016).
- **Meilleure trouvaille :** le territoire de Voronoï comme évaluation principale [[vks.ai]](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/).

### Mad Pod Racing — Wood 1 depuis ~15:01 UTC (STATUS lu à 15:11 UTC)
- **Live :** v2 C++, pilote « vise devant » (cible = checkpoint − 4 × vitesse). Wood 3 : 100 %, score 28,1 ; Wood 2 : 100 %, 21,76 contre 16,86 pour le boss (14:49-15:01 UTC). Une v3 avec BOOST est prête, non soumise.
- **Erreur → correction → règle :** « 1 pod, solo » en Wood 3 alors que le boss court aussi → lire un journal de test → lis un journal avant de concevoir.
- **Erreur → correction → règle :** le format d'entrée change en Wood 2, la v1 ne joue plus → v2 qui accepte les deux formats → compare l'énoncé après chaque promotion.
- **Erreur → correction → règle :** un rang lu juste après une soumission → ne lire qu'à ≥ 50 % → au-dessus du boss, on laisse tourner.
- **Entre ligues :** Wood 3 → 2 : 2 valeurs en plus et une ligne adversaire ; Wood 1 : BOOST, même entrée.
- **Meilleure trouvaille :** viser devant, k = 3 à 4 [[Hastings, 4e]](https://mightyprofessionalgaming.com/tutorials/case-study-search-legends.html). DEFEATS vide : aucune partie classée perdue lue.

### Troll Farm (Spring Challenge 2026) — Bronze depuis 14:47:20 UTC (STATUS lu à 15:40 UTC)
- **Live :** v3 Python 3, planificateur « points par tour de trajet », bois = 4 points, un 2e troll entraîné dès le tour 1. À 31 % : score 28,49, rang 1 sur 395, 20 victoires pour 1 défaite sur les 21 premières parties classées.
- **Erreur → correction → règle :** 100 tours codés en dur, la ligue suivante en a 300 → 5 défaites sur 5 → lire le diff de l'énoncé dès la promotion.
- **Erreur → correction → règle :** l'inventaire de départ n'avait pas été lu → afficher l'entrée du tour 1 → un « chopper » est possible dès le tour 1.
- **Erreur → correction → règle :** boss victorieux sur dépassement de temps → ne juger que les parties finies → un réglage sans effet se voit dans le journal (nombre de TRAIN).
- **Entre ligues :** Wood 2 : 1 troll, fruits seuls, 100 tours ; Wood 1 : 300 tours et TRAIN ; Bronze : toutes les règles (CHOP, MINE, PLANT).
- **Meilleure trouvaille :** valeur = objets par tour d'un aller-retour complet [[post-mortem, 3e]](https://www.yannmoisan.com/spring-challenge-2026-postmortem.html).

### Hypersonic — Wood 1 depuis 16:07:46 UTC (STATUS lu à 16:12 UTC ; Wood 2 depuis 15:27:34, 40 min)
- **Live :** v1 C++, recherche en faisceau (profondeur 12, largeur ~100, 15 ms), survie vérifiée. Wood 3 : 100 %, score 27,22 ; Wood 2 : 16 victoires, 3 défaites de 2 caisses (16:10 UTC). Parties de test (15:29 UTC) : 24-4 contre le boss, 24-6 contre le 1er de Wood 3.
- **Erreur → correction → règle :** un index de case en `int8_t` repart en négatif → le bot se fige, 3 parties de test perdues sans message → ASan + UBSan sur une partie locale l'ont montré en une exécution → un timeout avec des tours rapides avant = un plantage jusqu'à preuve du contraire.
- **Erreur → correction → règle :** on a d'abord cru à un serveur lent → afficher l'entrée lue sur `stderr` → la dernière ligne avant le timeout nomme l'état fautif.
- **Erreur → correction → règle :** un modèle d'adversaire pessimiste jugé séduisant → mesuré 45,8 % sur 60 parties et 42,5 % sur 120 → écarté.
- **Entre ligues :** Wood 2 : objets ; Wood 1 : murs X, bombes adverses mortelles, dernier en vie gagne (STATUS, 16:12 UTC).
- **Meilleure trouvaille :** simulateur exact du tour, puis recherche sur ses propres coups [[forum]](https://forum.codingame.com/t/hypersonic-feedback-strategy/2067). DEFEATS : 19 victoires, 0 défaite (14:58 UTC).

### Ultimate Tic-Tac-Toe — Bronze depuis 15:29:58 UTC (STATUS lu à 15:31 UTC, CHANGELOG à 15:42 UTC)
- **Live :** v2 C++, un seul fichier : minimax exact en 3×3, MCTS (UCT, constante 0,5) en 9×9. Wood : 100 %, score 22,59 contre 14,69. 4 victoires sur 4 contre le boss de Bronze en test.
- **Erreur → correction → règle :** la détection du mode 3×3 / 9×9 se trompait en jouant second → l'arène l'a trouvé (~1 coup illégal pour 100 parties) → teste les départs ambigus en arène.
- **Erreur → correction → règle :** constante d'exploration réglée à l'œil → 200 parties locales : 0,5 bat 0,3 à 75 % → règle sur 200 parties jumelées, pas à l'intuition.
- **Erreur → correction → règle :** un `sed` raté laisse un budget inchangé → `grep` du résultat → relis tout changement par script.
- **Entre ligues :** Wood = 3×3 ; Bronze = Ultimate, même format d'entrée, et la soumission du Wood « s'arrête de jouer » si elle ne sait pas le 9×9.
- **Meilleure trouvaille :** MCTS simple, constante bien sous √2 [[forum]](https://forum.codingame.com/t/ultimate-tic-tac-toe-puzzle-discussion/22616/150). DEFEATS : aucune lue (classement Bronze à 0 % au dernier relevé).

---

## Sources
- [a1k0n, Google AI Challenge 2010](https://www.a1k0n.net/2010/03/04/google-ai-postmortem.html) · [vks.ai, 78 lignes](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/) · [forum Tron](https://forum.codingame.com/t/tron-battle-aka-line-racing-multiplayer-challenge-discussion/49) · [Mighty Professional, étude de cas](https://mightyprofessionalgaming.com/tutorials/case-study-search-legends.html) · [Troll Farm, post-mortem](https://www.yannmoisan.com/spring-challenge-2026-postmortem.html) · [forum Hypersonic](https://forum.codingame.com/t/hypersonic-feedback-strategy/2067) · [forum Ultimate Tic-Tac-Toe](https://forum.codingame.com/t/ultimate-tic-tac-toe-puzzle-discussion/22616)
