# Squelettes de bots

Deux points de départ génériques, à adapter à l'énoncé du jeu :

- [`python/bot.py`](python/bot.py)
- [`cpp/bot.cpp`](cpp/bot.cpp)

Tester en local :

```bash
echo "tour 1" | python3 starters/python/bot.py
```

```bash
g++ -std=c++20 -O2 -o bot starters/cpp/bot.cpp && echo "tour 1" | ./bot
```

Rappel : pas de code de compétition dans ce repo.
