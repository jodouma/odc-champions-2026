# Ultimate Tic-Tac-Toe — Bronze atteint

**Jouer :** https://www.codingame.com/multiplayer/bot-programming/tic-tac-toe
**Où on en est :** Bronze depuis 15:29:58 UTC ; (Bois dès 14:39) ; relevé API de 16:19 UTC : rang 1 sur 5 453, score 30,17 contre 26,92 pour le boss, classement à 31 % **[notre run]**. Pas encore en Silver.

**Le chemin**
- **Bois :** morpion 3×3 : minimax exact, ne perd jamais ; 100 %, score 22,59 contre 14,69.
- **Bronze :** Ultimate (9 grilles), même format d'entrée ; l'ancienne version cesse de jouer. Il a fallu un MCTS.
- **Silver :** non lu.

**La recette**
1. **Un seul programme** qui détecte le mode (3×3 ou 9×9) à partir de la première liste de coups légaux.
2. **3×3 : minimax complet.**
3. **9×9 : MCTS** (parties aléatoires, arbre qui se souvient de la partie), constante d'exploration réglée.
4. **Règle l'arène :** si personne n'aligne trois grilles, celui qui en a le plus gagne.
5. **Langage :** C++ : ~780 000 parties simulées par seconde.

**Pièges**
- **Erreur :** détection de mode ambiguë (le 3×3 ressemble à un début de 9×9) → **correction :** arène avec départs ambigus, historique de la partie fautive : environ 1 coup illégal pour 100 parties **[notre run, 15:30 UTC]**.
- **Erreur :** un `sed` raté, budget inchangé → **correction :** `grep` du résultat avant de tester.
- **Erreur :** constante réglée à l'œil → **correction :** 200 parties jumelées : 0,5 bat 0,3 à 75 %.

**Astuces**
- **MCTS simple, constante bien sous √2, résolveur et réutilisation de l'arbre** [forum](https://forum.codingame.com/t/ultimate-tic-tac-toe-puzzle-discussion/22616/150).
- **Gagner tout de suite dans les parties simulées** : 59,8 % sur 200 parties **[notre run, 15:42 UTC]**, version candidate non soumise.
- **Ouverture au centre de la grille centrale** (presque tous les bots Legend) [même forum](https://forum.codingame.com/t/ultimate-tic-tac-toe-puzzle-discussion/22616/150).

**Temps** (27 nov 2026, UTC) : v1 soumise 14:41 → Bronze à 15:29:58 (49 min, dont l'attente du classement) ; v2 soumise 15:30 (corrige le bug de détection de mode) ; classement Bronze à 31 % à 16:19 UTC.

---

*Non vérifié :* les règles du Bronze de Tron, et celles de Mad Pod Racing et Hypersonic (pas encore en Bronze) ; le Silver des jeux Bronze ; les estimations d'heure (marquées *estimation*) ; les chiffres, copiés des fichiers de l'équipe et non rejoués. Les relevés API datent de 16:19 UTC ; les fichiers d'équipe de 14:37 à 16:12 UTC.


## Journal des trouvailles

Ajoute une ligne par trouvaille, la plus récente en haut ([comment contribuer](../CONTRIBUTING.md)).

| Date (UTC) | Ligue | Erreur → correction → règle | Source |
|---|---|---|---|
| … | … | … | notre essai / lien |
