# Squelettes de bots

Deux points de départ génériques, à adapter à l'énoncé du jeu. Ils font partie du [kit de démarrage](../templates/) : mode d'emploi dans [Utiliser les templates](../docs/utiliser-les-templates.md).

- [`python/bot.py`](python/bot.py)
- [`cpp/bot.cpp`](cpp/bot.cpp)

Les deux ont la même forme : constantes de l'énoncé, `State`, lecture du début de partie et de chaque tour, coups légaux, note d'un coup, choix du meilleur coup avec un chrono à la moitié du temps permis, `VERSION` et debug sur stderr. Tu ne remplis que les zones « À ADAPTER ».

Tester en local (une ligne de début de partie, puis une ligne par tour) :

```bash
printf 'init\ntour 1\ntour 2\n' | python3 starters/python/bot.py
```

```bash
g++ -std=c++17 -O2 -o bot starters/cpp/bot.cpp && printf 'init\ntour 1\ntour 2\n' | ./bot
```

Le squelette adapté au jeu de l'[arène](../arena/) : [`arena/bots/depart.py`](../arena/bots/depart.py).

Rappel : pas de code de compétition dans ce repo.
