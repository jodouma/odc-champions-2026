# Troll Farm (Spring Challenge 2026) — Bronze atteint

**Jouer :** https://www.codingame.com/multiplayer/bot-programming/spring-challenge-2026-troll-farm
**Où on en est :** Bronze depuis 14:47:20 UTC ; (Bois 2 dès 14:39, Bois 1 dès 14:43) ; relevé API de 16:19 UTC : rang 1 sur 395, score 31,01 contre 22,5 pour le boss, classement à 51 % **[notre run]**. Pas encore en Silver.

**Le chemin**
- **Bois 2 :** 1 troll, fruits seuls, 100 tours. Un ramasseur qui note chaque arbre suffit.
- **Bois 1 :** 300 tours et TRAIN (entraîner des trolls). Il fallait étendre l'horizon et entraîner un 2e troll.
- **Bronze :** toutes les règles (CHOP, MINE, PLANT) ; le bois vaut 4 points. Il fallait couper du bois et un 2e troll dès le tour 1.
- **Silver :** non lu.

**La recette**
1. **Note chaque arbre : objets rapportés par tour d'un aller-retour complet** (trajet + attente + récolte + retour), distance réelle, pas à vol d'oiseau.
2. **Prévois l'état des arbres** (maturité) avec les règles de l'arbitre, public.
3. **Entraîne un 2e troll tout de suite** avec l'inventaire de départ, puis coupe du bois.
4. **Compare récolter et couper en points par tour.**
5. **Langage :** Python 3 : 50 ms par tour suffisent pour un parcours en largeur et quelques dizaines de plans.

**Pièges**
- **Erreur :** 100 tours codés en dur → **correction :** lire le diff de l'énoncé au moment de la promotion (5 défaites sur 5 en Bois 1) **[notre run, 14:43 UTC]**.
- **Erreur :** juger sur des victoires où le boss dépasse le temps → **correction :** ne compter que les parties finies.
- **Erreur :** un réglage « plus de trolls » sans effet → **correction :** compter les commandes TRAIN dans le journal avant de dépenser des parties de test.

**Astuces**
- **Ne devine pas les règles :** l'arbitre est public [dépôt](https://github.com/eulerscheZahl/Troll-Farm).
- **Affiche l'entrée du premier tour** : l'inventaire de départ permet d'entraîner un coupeur dès le tour 1 **[notre run, 27 nov]**.
- **« Valeur par tour » pour tout** [post-mortem, 3e](https://www.yannmoisan.com/spring-challenge-2026-postmortem.html).

**Temps** (27 nov 2026, UTC) : v1 soumise 14:41 → Bois 1 à 14:43:16 (~2 min, promotion par parties contre le boss) ; v2 soumise 14:46 → Bronze à 14:47:20 (~4 min) ; Bronze : 51 % à 16:19 (API), 100 % attendu vers 17:20 d'après l'équipe (estimation, ~10 points par 30 min).


## Trouvailles de l'équipe

Chaque trouvaille est un petit fichier dans [`trouvailles/`](trouvailles/). Pour en ajouter une : [comment contribuer](../../CONTRIBUTING.md).
