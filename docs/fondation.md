# Fondation : être prêt pour 7 heures de bot sur un jeu inconnu, avec une IA

Tiré de nos cinq entraînements du 27 nov 2026 (fichiers d'équipe lus jusqu'à 16:28 UTC). **[notre run]** = mesuré par nous, heure UTC ; *non vérifié* = pas contrôlé. Les ligues Silver à Legend viennent d'un relevé de l'API CodinGame (28 nov 2026, 13:33 UTC), **pas de nos journaux** : les bots y sont montés dans la nuit sans nouvelle version, et nous n'avons pas encore analysé ces ligues. Aucun code publié.

## 1. Le plan des 7 heures

- **0 – 30 min : lire, puis un bot jamais illégal.** Lis tout l'énoncé, le format d'entrée/sortie, le temps par tour, ce qui arrive à un joueur éliminé. Affiche l'entrée du premier tour ; lis **un** journal de test. *Pourquoi :* Troll Farm : l'inventaire de départ a permis un coupeur dès le tour 1 ; Mad Pod Racing : « 1 joueur » cachait un adversaire (27 nov). Soumets ce bot : les ligues Bois passent en minutes (Mad Pod Racing ~10 min, Troll Farm ~2 min).
- **30 – 60 min : un simulateur local et une première bonne idée.** Test sans limite, contre un bot aléatoire et contre ta version précédente. *Pourquoi :* un réglage sur 40 courses × 12 valeurs a coûté 0 appel API (Mad Pod Racing) ; les parties de test du site sont comptées.
- **Heures 2 – 5 : la boucle.** Un seul changement → 100+ parties jumelées (départs inversés) → relecture du code → soumission par **une** personne. Pendant que le classement tourne (40 à 66 min par ligue Bois ; ~2 h en Bronze à Troll Farm), travaille hors ligne. **Après chaque promotion, relis l'énoncé** (Troll Farm : 100 tours codés en dur, 300 ensuite = 5 défaites sur 5). Ne resoumets pas pendant qu'une version finit son classement.
- **Dernière heure : plus de risque.** Seulement des améliorations mesurées ; contrôle le pire temps de tour (le serveur a mesuré 77 à 104 ms pour un budget de 70 ms, Tron) ; garde un budget d'environ la moitié du temps permis.
- **15 dernières minutes : rien de neuf.** Vérifie ce qui est en ligne (liste des soumissions), mets le journal de versions à jour. Une soumission relance les parties classées : le règlement du concours sur le classement final n'est *pas vérifié*.

## 2. Reconnaître le type de jeu

| Type | Approche qui a marché | Langage | Première technique | Nos preuves |
|---|---|---|---|---|
| Duel sur grille (Tron) | Territoire (Voronoï) + recherche | Python puis C++ | Éviter les impasses (cases accessibles), puis Voronoï | v3 C++ bat v2 Python 159-41 (27 nov, ~14:05 UTC) ; Bronze 16:10 ; Legend (rang 61 sur 820, depuis 07:31, 28 nov, relevé API) |
| Course / physique (Mad Pod Racing) | Viser devant le checkpoint, simulateur exact | C++ | Cible = checkpoint − 4 × vitesse | Wood 1 à 81 % (27 nov, 16:21) ; Gold, très loin du boss (rang 9 421 sur 23 613, 28 nov, relevé API) |
| Économie / ressources (Troll Farm) | Valeur = objets par tour d'un aller-retour complet | Python 3 | Noter chaque cible en points par tour | Bronze 14:47 UTC, rang 1 à 53 % (16:21) ; Gold sous le boss (rang 71 sur 465, 28 nov, relevé API) |
| Bombes / arène (Hypersonic) | Simulateur exact du tour + recherche en faisceau | C++ | Survivre d'abord, puis casser des caisses | Wood 1 à 25 % (16:27) ; Legend (rang 347 sur 811, 28 nov, relevé API) |
| Jeu de plateau (Ultimate Tic-Tac-Toe) | Minimax exact en petit, MCTS en grand | C++ | Un seul programme, mode détecté à la 1re liste de coups | Bronze 15:29:58 ; Legend (rang 309 sur 514, depuis 03:16, 28 nov, relevé API) |

Jeu inconnu : compare-le à ces cinq lignes, prends l'approche du plus proche, et ne passe en C++ que si la recherche ou la simulation limite la force (Troll Farm est resté en Python 3).

## 3. La boîte à outils (reconstruite pour chaque jeu)

- **Bot « jamais illégal » :** joue n'importe quel coup légal. Sert de v1, de plancher et d'adversaire de test.
- **Simulateur local :** rejoue les règles hors du site. Il garde les parties de test (comptées) pour la validation finale.
- **Tournoi miroir :** chaque départ joué dans les deux sens, 100+ parties. 53 %, 56 % et 52,7 % sur 100/100/300 parties n'ont jamais tranché seuls (Tron).
- **Classeur de défaites :** un script range les défaites par cause. 74 des 88 défaites de la v2 étaient une course au territoire perdue tôt (Tron, 27 nov 14:00 UTC).
- **Journal de versions :** une ligne par version (quoi, pourquoi, résultat) et le code de chacune. Il remplace la mémoire quand on revient demain.
- **Garde de temps :** budget ≈ moitié du temps permis, lecture du pire tour. Un timeout après des tours rapides est un plantage jusqu'à preuve du contraire (Hypersonic : index `int8_t` négatif, trouvé avec ASan/UBSan).

## 4. Travailler avec l'IA en équipe de 4

- **Rôles :** (1) **pilote** : lit l'énoncé, tient le journal, **seul à soumettre** ; (2) **outils** : simulateur et tournoi ; (3) **bot** : écrit et change la stratégie avec l'IA ; (4) **relecteur** : classe les défaites, relit le code, écrit les tests.
- **La boucle :** idée → un changement → tournoi → relecture → soumission annoncée à l'équipe.
- **Donne à l'IA :** l'énoncé tel quel, le format d'entrée/sortie, la limite de temps, le fichier actuel, une demande précise à la fois.
- **Ne fais jamais confiance sans test :** le temps de tour ; la légalité des coups (~1 coup illégal pour 100 parties, Ultimate Tic-Tac-Toe) ; « le changement a bien eu lieu » (un réglage « plus de trolls » n'a rien changé, Troll Farm) ; une idée plausible (modèle d'adversaire pessimiste : 45,8 % sur 60 parties, Hypersonic) ; les sources de l'IA. La revue a trouvé 2 vrais bugs que 1000+ parties simulées n'avaient pas montrés (Tron).

## 5. Ce qui fait passer chaque ligue

- **Bois → Bronze :** un bot sans coup illégal, puis une idée simple et bonne. Les promotions arrivent en 2 à 66 min. Les règles peuvent changer (format d'entrée en Mad Pod Racing, 3×3 puis 9×9 en Ultimate Tic-Tac-Toe) : relis l'énoncé à chaque promotion.
- **Bronze :** parfois **les mêmes règles** (Tron : texte identique à Bois, relu 16:21 UTC) ; ailleurs les règles complètes (Troll Farm). Il faut une évaluation, une économie ou une recherche : Tron v3, Troll Farm v3 (bois + 2e troll), Ultimate Tic-Tac-Toe MCTS.
- **Silver, Gold, Legend :** **pas encore d'analyse de notre part** (nos journaux s'arrêtaient en Bois 1 / Bronze au 27 nov 16:28 UTC). Seul fait : les ligues atteintes le 28 nov (relevé API ci-dessus). Les pistes des recherches (non testées par nous) : chambres et points d'articulation pour Tron, rôles coureur/bloqueur et recherche aléatoire pour Mad Pod Racing, plantation-coupe pour Troll Farm.

Cette section sera complétée à mesure que nous analysons le Silver, l'Or et la Légende.
