# Exemple : un bot Tron Battle

Un bot d'entraînement écrit avec l'IA, via l'API officielle de CodinGame. Il joue sous le pseudo `sg0-degodas`.

- Jeu : [Tron Battle](https://www.codingame.com/multiplayer/bot-programming/tron-battle) · [classement](https://www.codingame.com/multiplayer/bot-programming/tron-battle/leaderboard)
- Code : [`bot.py`](bot.py) (Python 3, 56 lignes)

## Comment il joue

1. Il ne fait **jamais de coup illégal** : il évite les murs et les traînées.
2. Pour chaque coup possible, il compte les **cases encore accessibles** et garde le maximum.
3. En cas d'égalité, il préfère le coup qui lui laisse **plus de territoire que l'adversaire**.

## Ce qu'il a donné

Avant soumission : 4 parties de test gagnées sur 4 en ligue Bois 2, dont 2 contre le boss.

## À toi

Ne le copie pas : **bats-le**. Choisis `sg0-degodas` comme adversaire dans l'éditeur, regarde le replay, et améliore ton bot une idée à la fois.

Ceci est un bot d'entraînement sur un jeu public. Aucun code de compétition n'ira dans ce repo.
