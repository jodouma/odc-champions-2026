# Mad Pod Racing — Bois 1 pour l'instant

**Jouer :** https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing
**Où on en est :** Bois 1 depuis 15:00 UTC ; Bois 3 dès 14:39, Bois 2 dès 14:49 ; relevé API de 16:19 UTC : rang 1 sur 13 259, score 30,22 contre 21,74 pour le boss, classement à 80 % **[notre run]**. Bronze non atteint à cette heure.

**Le chemin**
- **Bois 3 :** 1 pod, une course contre le boss (le « 1 joueur » de l'API le cache). Un pilote qui vise bien les checkpoints suffit : 100 %, score 28,1.
- **Bois 2 :** 2 valeurs en plus et une ligne adversaire dans l'entrée : l'ancienne version cesse de jouer. Score 21,76 contre 16,86 pour le boss.
- **Bois 1 :** ajoute BOOST, même format d'entrée : la v2 continue de jouer.
- **Bronze :** non lu.

**La recette**
1. **Un pilote qui vise un point devant le checkpoint** (checkpoint moins quelques fois la vitesse) et coupe la poussée quand la cible est derrière.
2. **Recalcule la vitesse à partir du déplacement** : elle n'est pas dans l'entrée.
3. **Règle les paramètres dans un petit simulateur local**, un paramètre à la fois.
4. **Après chaque promotion, compare l'énoncé** et corrige la lecture de l'entrée avant tout le reste.
5. **Langage :** C++ dès le début, pour ne pas réécrire quand la simulation deviendra utile.

**Pièges**
- **Erreur :** croire à une course en solo en Bois 3 → **correction :** lire un journal de test avant de concevoir.
- **Erreur :** deux règles partageaient un même paramètre dans la grille de réglage, le freinage « ne faisait rien » → **correction :** un paramètre par grille.
- **Erreur :** lire un rang juste après une soumission → **correction :** ne lire qu'à ≥ 50 %.

**Astuces**
- **Viser devant, facteur 3 à 4** : « 4 fait mieux que 3 ou 5 » [Hastings, 4e](https://mightyprofessionalgaming.com/tutorials/case-study-search-legends.html).
- **BOOST une seule fois, sur le trajet le plus long** ; −5,4 tours en simulation locale **[notre run, 27 nov 15:02 UTC]**, version prête non soumise.
- **Physique exacte** (18°/tour, frottement 0,85) pour tester hors ligne [tcourreges](https://tcourreges.github.io/coders-strike-back).

**Temps** (27 nov 2026, UTC) : v1 soumise 14:41 → Bois 2 à 14:49:54 (~9 min) ; v2 soumise 14:50 → Bois 1 à ~15:01 (~11 min) ; Bois 1 à 26 % à 15:10. Ici l'attente a été courte parce que les classements étaient rapides.


## Trouvailles de l'équipe

Chaque trouvaille est un petit fichier dans [`trouvailles/`](trouvailles/). Pour en ajouter une : [comment contribuer](../../CONTRIBUTING.md).
