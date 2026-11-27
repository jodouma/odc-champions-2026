# Tron Battle — Bronze atteint

**Jouer :** https://www.codingame.com/multiplayer/bot-programming/tron-battle
**Où on en est :** Bronze depuis 16:10 UTC (Bois 2 dès 12:10, Bois 1 dès 14:01) ; relevé API de 16:19 UTC : rang 1 sur 1 698, score 27,13 contre 25,79 pour le boss, classement à 14 % **[notre run]**. Le score n'est pas final avant 100 %.

**Le chemin**
- **Bois 2 :** 2 joueurs, grille 30×20, 100 ms par tour, un mur ou une trace = élimination. Il fallait un bot sans coup illégal qui évite les impasses (v2 Python : remplissage + territoire).
- **Bois 1 :** aucun changement de règle noté dans nos fichiers (*non vérifié*). Il fallait chercher en avance : la v2 perdait la course au territoire (88 défaites sur 212 en Bois 2, 14:00 UTC), la v3 C++ à recherche a pris le relais.
- **Bronze :** règles non relues dans nos fichiers au moment de cette fiche (*non vérifié*) ; la version live est la v3 d'après le dernier journal (14:37 UTC), sans resoumission notée depuis. Prochain travail prévu : la course aux murs au milieu de partie, au-delà de l'horizon de recherche.

**La recette**
1. **Un bot qui ne joue jamais un coup illégal** : n'importe quelle case libre voisine.
2. **Ajoute le calcul des impasses** : compte les cases accessibles après chaque coup, évite les poches trop petites.
3. **Note les positions par le territoire** : les cases où j'arrive avant l'adversaire (Voronoï).
4. **Ajoute une recherche** (alpha-bêta, quelques coups d'avance) sur cette note, avec un garde de temps.
5. **Langage :** Python pour les étapes 1-3 (rapide à écrire) ; C++ pour l'étape 4 (la recherche est trop lente en Python). La v3 C++ a battu la v2 Python 159-41 sur 200 parties jumelées (27 nov, ~14:05 UTC) **[notre run]**.

**Pièges**
- **Erreur :** chercher les défaites en fin de partie → **correction :** rejouer les images 10 à 60 : 74 des 88 défaites de la v2 étaient une course au territoire perdue tôt **[notre run, 14:00 UTC]**.
- **Erreur :** budget de 70 ms → **correction :** 55 puis 40 ms : le serveur a mesuré 77 à 104 ms, et 40 ms ne coûte rien (51,0 % sur 200 parties) **[notre run]**.
- **Erreur :** resoumettre pendant le classement → **correction :** attendre la promotion, puis soumettre. La v3 a été soumise juste après la promotion de la v2 et a passé le Bois 1 sans nouvelle soumission **[notre run]**.

**Astuces**
- **La meilleure évaluation bat la recherche la plus profonde** [a1k0n](https://www.a1k0n.net/2010/03/04/google-ai-postmortem.html).
- **Voronoï seul** a mené un bot Python de 78 lignes au top 5 % en 2016 [vks.ai](https://vks.ai/2016-09-07-ai-challenge-in-78-lines/).
- **Beaucoup de parties se jouent au départ** : compare avec départs inversés ; 3 des 4 défaites de la v3 en Bois 1 (lu à 14:36 UTC) étaient des départs perdus **[notre run, 27 nov]**.

**Temps** (27 nov 2026, UTC, relevés API) : Bois 2 de 12:10 à 14:01 (111 min ; v2 soumise à 12:55, donc ~66 min de classement jusqu'à 100 %) ; Bois 1 de 14:01 à 16:10 (129 min ; v3 soumise à 14:07, attente = classement à 100 %) ; Bronze depuis 16:10. Nos fichiers d'équipe n'ont pas été mis à jour entre 14:37 et 16:10 : les chiffres de cette période viennent uniquement de l'API.


## Journal des trouvailles

Ajoute une ligne par trouvaille, la plus récente en haut ([comment contribuer](../CONTRIBUTING.md)).

| Date (UTC) | Ligue | Erreur → correction → règle | Source |
|---|---|---|---|
| … | … | … | notre essai / lien |
