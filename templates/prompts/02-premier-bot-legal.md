# Prompt 2 : écrire le premier bot « jamais illégal »

**Quand :** juste après la fiche. But : un bot qui joue toujours un coup autorisé, à temps. Pas de stratégie.

**Ce que tu colles :** la fiche remplie et le squelette du repo ([`starters/python/bot.py`](../../starters/python/bot.py) ou [`starters/cpp/bot.cpp`](../../starters/cpp/bot.cpp)).

```text
Voici la fiche d'un jeu de bots CodinGame, puis notre squelette de bot en <Python 3 / C++>.

<colle la fiche>

<colle le squelette>

Remplis UNIQUEMENT les zones marquées « À ADAPTER » :
- les constantes (limite de temps par tour et au 1er tour, tirées de la fiche) ;
- read_init et read_turn : lire TOUTES les lignes données, même celles qu'on n'utilise pas ;
- legal_moves : la liste complète des coups autorisés, jamais vide ;
- evaluate : renvoie 0 pour tous les coups (pas de stratégie pour l'instant).
Ne change pas le reste (chrono, debug sur stderr, VERSION, choix du coup).
Donne le fichier complet, puis une entrée de test d'un tour (copiée du format de la fiche)
pour le lancer en local.
```

**Vérifie après :** lance-le en local avec l'entrée de test. Puis une partie de test sur le site : lis le journal, tu dois voir `VERSION v1` au tour 1, `entree=` à chaque tour, et aucun « invalid » ni « timeout ».
