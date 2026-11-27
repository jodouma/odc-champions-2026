# Tron Battle — bonnes pratiques

**En bref :** ce que `Assoo` a appris en montant en Bois 2 sur [Tron Battle](https://www.codingame.com/multiplayer/bot-programming/tron-battle) (27 nov 2026) : la v3 en Python est 3e sur 1 631, au-dessus du boss. Ce sont des **idées et des méthodes**, pas du code : écris ton propre bot.

Les règles valables pour tous les jeux sont dans [nos bonnes pratiques](../bonnes-pratiques.md). Cette page ne garde que ce qui est propre à Tron, et ce que cette montée a ajouté.
Les erreurs à ne plus refaire sont rangées par ligue, en [bas de page](#bois-2--bois-1).

**Légende :** **[mesuré]** = parties jouées par nous le 27 nov 2026 · *non vérifié* = pas contrôlé.

---

## Le jeu en 5 lignes

- Grille de **30 × 20**. En Bois : **2 joueurs**. Le dernier vivant gagne.
- Les joueurs **jouent l'un après l'autre**, pas en même temps : c'est un vrai jeu à tour alterné, donc le minimax s'applique tel quel.
- **100 ms par tour.**
- À chaque tour tu reçois, pour chaque joueur, `X0 Y0 X1 Y1` (case de départ, tête actuelle). **Garde toi-même toutes les traînées** dans ta grille : l'entrée ne te redonne pas le plateau.
- Quand un joueur meurt, il reçoit `-1` : **libère ses cases** dans ta grille, elles redeviennent jouables.

---

## 1. La méthode de travail

1. Écris une version.
2. **Teste-la contre le boss** de ta ligue.
3. Soumets.
4. **Regarde les replays des défaites** : où la partie a basculé ?
5. Corrige **une seule idée**.
6. Teste la nouvelle version **contre ta version soumise** (A/B) **et contre les meilleurs joueurs** de ta ligue.
7. Resoumets **seulement si c'est nettement mieux**, par exemple **9 victoires sur 12** ou plus.

Pourquoi un seuil aussi haut : **chaque soumission relance le classement de 0 %**. Une version « un peu mieux » qui te fait perdre ta place ne vaut pas le coup. Et ne soumets jamais quand la version en ligne est près de la promotion.

---

## 2. Stratégie : de v1 à v4

| Version | Idée | Résultat **[mesuré]** |
|---|---|---|
| v1 | Voronoï à 1 coup | 56 V / 8 D en classement, assez pour battre le boss de Bois 2 |
| v2 | Minimax alterné + alpha-bêta, approfondissement itératif | bat v1 **5 / 5** |
| v3 | Meilleure évaluation du territoire | bat v2 **9 / 12**. En ligne : 3e / 1 631 en Bois 2 |
| v4 | Port C++ de v3, plus rapide | **pas encore plus fort** : 2 / 6 contre v3, non soumis |

### v1 · Voronoï à 1 coup
Pour chaque coup possible : un **BFS depuis les deux têtes en même temps**, et on compte les cases que j'atteins **avant** l'adversaire. On joue le coup qui maximise *mes cases − ses cases*. Simple, et déjà au-dessus du boss.

### v2 · Recherche minimax
- **Minimax alterné** (moi, lui, moi, lui…) avec **alpha-bêta**, évaluation = score Voronoï.
- **Approfondissement itératif** : profondeur 1, puis 2, puis 3… jusqu'à la limite de temps. On garde le meilleur coup de la dernière profondeur **terminée**.
- Trie les coups à chaque profondeur selon le résultat de la précédente : l'alpha-bêta coupe beaucoup plus.
- **Sa faiblesse :** elle a perdu contre un joueur qui **coupe le plateau tôt avec un long mur droit**. Une recherche peu profonde ne voit pas venir la coupure. La réponse n'était pas « chercher plus loin », mais **mieux évaluer** (v3).

### v3 · Mieux noter le territoire
Trois idées :

1. **L'espace ouvert compte plus qu'un couloir.** Tant que les joueurs se touchent :
   `score = (mes cases − ses cases) × 10 + (voisins libres de mes cases − voisins libres des siennes) × 3`.
   Deux zones de même taille ne se valent pas : un couloir d'une case se remplit mal.
2. **Une fois séparés : la borne du damier (parité).** Colore la grille comme un échiquier. Un chemin **alterne les couleurs** à chaque pas. Donc, depuis ta tête, le plus long chemin possible dans ta zone est au plus
   `2 × min(blanches, noires)`, **+ 1** si la couleur opposée à celle de ta tête est plus nombreuse.
   C'est une borne bien plus juste que « nombre de cases », surtout dans les zones biscornues.
3. **Fin de partie, séparés : chercher le plus long chemin.** Un parcours en profondeur (DFS) avec limite de temps, qui garde le meilleur chemin trouvé. Commence par le coup qui longe les murs (le moins de voisins libres) : c'est souvent le bon, et il sert de réponse si le temps manque.

**Le piège de la v3 : les échelles de score.** Premier essai : cases « séparées » × 1000 contre environ 20 pour les cases disputées. Le bot se ruait pour **s'emmurer** dès que possible, même dans une petite zone. Résultat : **1 / 3**, pire qu'avant. En ramenant le poids à **× 25**, il est devenu meilleur que v2. 👉 Quand tu mélanges deux scores, **vérifie qu'ils sont du même ordre de grandeur**.

### v4 · Le port en C++
Ce qui accélère vraiment :
- **Grille avec bordure** : une ligne et une colonne de murs autour du plateau. Plus aucun test « suis-je dans la grille ? ».
- **Tableaux à tampon** (*stamp*) au lieu de remettre à zéro : un compteur qu'on incrémente à chaque BFS ; une case est « vue » si son tampon égale le compteur. Pas de remise à zéro de 600 cases à chaque nœud.
- **Aucune allocation pendant la recherche** : tous les tableaux sont créés une fois au début.

Résultat : **6 à 12 tours de profondeur** au lieu de 3 à 8 en Python. Mais **2 / 6 seulement contre v3**. Leçons :
- **La vitesse seule ne gagne pas** : la qualité de l'évaluation compte plus (voir aussi [bonnes pratiques](../bonnes-pratiques.md)).
- Après un port, **vérifie que les deux versions choisissent le même coup** sur les mêmes positions avant de comparer leur force. Une petite différence de comportement peut tout expliquer.

---

## 3. Performance et temps

- **Garde une marge.** Un premier budget de 85 ms sur 100 était trop juste. Chez `Assoo` : **50 ms au premier tour, puis 70 à 75 ms** sur les 100. Un autre essai du groupe a mesuré 77 à 104 ms côté serveur avec un budget de 70 ms : si tu vois des dépassements, descends vers 50 ms ([bonnes pratiques](../bonnes-pratiques.md)).
- **Lis l'heure tous les 64 nœuds**, pas à chaque nœud : lire l'horloge coûte cher, surtout en Python.
- **Quand la recherche s'arrête faute de temps, remets le plateau exactement dans son état d'origine.** Une exception qui sort au milieu de la recherche laisse des cases marquées « occupées » : le tour suivant joue sur un faux plateau. Le plus sûr : une copie avant, restaurée après.
- En Python : précalcule une fois les voisins de chaque case (listes de cases), et travaille sur un tableau à une dimension (`y × 30 + x`).

---

## 4. Tester et déboguer

- **Rejoue les mêmes départs.** L'API permet de relancer une partie depuis un replay (`replay_game_id`) : mêmes positions de départ, donc une comparaison juste avant / après. Fais-le vite : si l'adversaire a resoumis, c'est refusé.
- **Vérifie le langage envoyé.** Un banc de test qui envoie du **C++ étiqueté Python3** donne un « timeout » **au premier tour**. Avant de croire un résultat, regarde le champ langage.
- **Compte tous les messages d'échec** : « timeout », « in time », etc. N'en compter qu'un seul cache des défaites.
- **Les identifiants d'agent changent** quand un joueur resoumet. Relis `/opponents` avant chaque série de tests.
- Écris sur `stderr` la profondeur atteinte, le coup choisi et le score de chaque coup : c'est visible dans les parties de test (pas dans les parties classées).

---

## 5. L'API CodinGame

Pour ceux qui testent avec un agent IA (voir [comment on utilise l'IA](../ia-agent.md)) :

- **Connexion :** flux OAuth « device » (on valide un code sur le site). Le jeton reste **sur ta machine**, par exemple dans `~/.config/codingame/token`. **Ne le commite jamais**, ne le colle dans aucun chat.
- **Limites** relevées sur ce compte : environ **10 parties de test par minute, 30 par 15 minutes, 600 par jour**, **5 soumissions par 5 minutes**, **une seule partie de test à la fois**. Lis le champ `limits` de chaque réponse plutôt que de les supposer.
- **Suivre le classement :** interroge la progression **toutes les 1 à 2 minutes**, pas plus vite.
- **Promotion :** il faut être **classé au-dessus du boss** une fois assez de parties de classement jouées. Elle n'est pas immédiate (voir [les ligues](../ligues.md)).

---

**Ligue par ligue :** à chaque promotion, une section avec ce qui a marché et les erreurs à ne plus refaire.

## Bois 2 → Bois 1

*En cours (27 nov 2026) : `Assoo` est 1er de Bois 2, le boss est 5e, classement à 82 %. La promotion n'est pas encore faite.*

### Ce qui a marché
- **Un Voronoï simple suffit pour battre le boss** de Bois 2 (v1 : 56 V / 8 D en classement).
- **La boucle « une idée → A/B contre la version soumise → resoumettre si ≥ 9/12 »** : chaque version gardée battait clairement la précédente (v2 5/5, v3 9/12).
- **Mieux évaluer avant de chercher plus loin** : espace ouvert, borne du damier, plus long chemin en fin de partie (v3).
- **Ne pas resoumettre pendant le classement** : la v3 finit son classement en Python même si un port C++ existe.

### Erreurs à ne plus refaire

| Ce qui s'est passé | Ce que ça a coûté | La règle |
|---|---|---|
| Score de zone séparée × 1000 contre ~20 pour les cases disputées | Le bot s'emmurait trop tôt : **1 / 3** jusqu'au réglage à × 25 | Mets les termes d'un score au même ordre de grandeur avant de tester |
| Le script de test envoyait le code C++ étiqueté **Python3** | **14 fausses défaites** « timeout » ; on a failli abandonner la v4 | Vérifie le champ langage ; un timeout au tour 1 = outil cassé, pas bot lent |
| Premier budget de temps C++ : **85 ms** sur 100 | Trop juste : dépassements | Marge : 50 ms au premier tour, puis 70 ms au plus |
| Un `pkill -f <motif>` correspondait aussi à la boucle qui suit le classement | La boucle de suivi s'est tuée elle-même | Tue par PID, ou avec un motif qui ne peut pas correspondre à ta propre commande |
| Le script de série ne comptait que « in time » | Des défaites « timeout » non comptées | Compte tous les messages d'échec (« timeout », « in time »…) |
| Recherche peu profonde contre un long mur droit (v2) | Défaites contre un joueur qui coupe le plateau tôt | Améliore l'évaluation avant la profondeur |
| Port C++ plus rapide mais pas plus fort | 2 / 6 contre la v3 Python | Vérifie que le port choisit les mêmes coups ; la vitesse seule ne suffit pas |
| Plateau pas restauré après un arrêt de recherche | Le tour suivant joue sur un faux plateau | Copie avant, restaure après |
| Joueur mort oublié | Ses cases restent des murs | `-1` = libère ses cases |
| Ancien identifiant d'adversaire | Tests contre une version périmée | Relis `/opponents` avant chaque série |

---

Une nouvelle section sera ajoutée à chaque promotion.
