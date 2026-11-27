# Hypersonic — Bois 1 pour l'instant

**Jouer :** https://www.codingame.com/multiplayer/bot-programming/hypersonic
**Où on en est :** Bois 1 depuis 16:07:46 UTC ; (Bois 3 dès 14:39, Bois 2 dès 15:27) ; relevé API de 16:19 UTC : rang 1 sur 193, score 20,71 contre 18,05 pour le boss, classement à 18 % **[notre run]**. Bronze non atteint.

**Le chemin**
- **Bois 3 :** grille 13×11, 200 tours, une bombe à la fois. Casser des caisses sans mourir ; 100 %, score 27,22.
- **Bois 2 :** les objets (portée, bombes) apparaissent. 40 min de classement ; 16 victoires pour 3 défaites lues à 16:10 UTC.
- **Bois 1 :** murs X, les bombes ennemies tuent, les siennes sont inoffensives, dernier en vie gagne (lu dans le STATUS).
- **Bronze :** non lu.

**La recette**
1. **Un simulateur exact d'un tour** : minuteries, explosions en chaîne, caisses et objets qui bloquent le souffle.
2. **Recherche sur ses propres coups** (faisceau, ~12 tours) ; garde de survie : on ne garde que les chemins où l'on survit.
3. **Note = caisses cassées + à casser + objets, moins la distance**, avec un facteur de patience.
4. **Langage :** C++ : la recherche en faisceau tient en 15 ms.

**Pièges**
- **Erreur :** un index `int8_t` repart en négatif → le bot se fige, 3 parties perdues sans message → **correction :** `int16_t`, trouvé avec ASan/UBSan sur une partie locale **[notre run, 27 nov]**.
- **Erreur :** croire à un serveur lent → **correction :** afficher l'entrée lue sur `stderr`.
- **Erreur :** trop aimer les objets → 3 défaites de justesse (14-16) en Bois 2 → **correction prévue :** baisser leur valeur, testée sur 100+ parties jumelées **[notre run, 16:10 UTC]**.

**Astuces**
- **Portée 3 = souffle de 2 cases** : mesuré sur une partie de test **[notre run, 27 nov]**.
- **Un modèle d'adversaire pessimiste** : 45,8 % sur 60 parties, rejeté **[notre run]**.
- **Beaucoup de joueurs forts** utilisent la recherche en faisceau [forum Hypersonic](https://forum.codingame.com/t/hypersonic-feedback-strategy/2067).

**Temps** (27 nov 2026, UTC) : v1 soumise 14:48 → Bois 2 à 15:27:34 (39 min) → Bois 1 à 16:07:46 (40 min) ; attente = classement à 100 %.


## Journal des trouvailles

Ajoute une ligne par trouvaille, la plus récente en haut ([comment contribuer](../CONTRIBUTING.md)).

| Date (UTC) | Ligue | Erreur → correction → règle | Source |
|---|---|---|---|
| … | … | … | notre essai / lien |
