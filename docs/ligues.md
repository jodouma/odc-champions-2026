# Les ligues à grimper

**En bref :** tout le monde commence en Bois. Pour monter, il faut battre le **boss** de sa ligue. La dernière ligue s'appelle Légende.

## L'échelle (exemple : Tron Battle)

| Ligue | Joueurs (27 nov 2026) |
|---|---|
| 🏆 Légende | 817 |
| 🥇 Or | 864 |
| 🥈 Argent | 2 746 |
| 🥉 Bronze | 1 697 |
| 🪵 Bois 1 | 560 |
| 🪵 Bois 2 (départ) | 1 628 |

Classement en direct : <https://www.codingame.com/multiplayer/bot-programming/tron-battle/leaderboard>

Selon le jeu, il y a une ou plusieurs ligues Bois, et la dernière ligue n'est pas toujours Légende.

## Comment monter

1. **Soumets ton bot.** Il joue ses parties de classement contre les joueurs de ta ligue.
2. **Dépasse le boss.** Chaque ligue (sauf la dernière) a un boss : un bot placé là par CodinGame.
   - En **Bois**, il faut en général gagner un certain nombre de parties contre le boss.
   - À partir du **Bronze**, il faut que ton score dépasse celui du boss une fois toutes tes parties jouées.
3. **Attends la promotion.** Elle n'est pas immédiate : souvent environ une minute, parfois plus.
4. **Relis l'énoncé.** Une nouvelle ligue peut apporter de nouvelles règles. Si c'est le cas, ton ancien bot ne joue plus : il faut en soumettre un nouveau.

## À savoir

- Gagner contre le boss en partie de test est bon signe, mais c'est le **classement contre toute la ligue** qui compte.
- Une soumission ratée coûte du temps : teste contre le boss **avant** de soumettre.
- Une fois « promouvable », tu le restes, même si ton score baisse ensuite.
- Tu ne peux choisir comme adversaires que des joueurs de **ta ligue ou d'une ligue inférieure**.

Source : [guide des ligues de CodinGame](https://www.codingame.com/api/v1/docs/leagues).
