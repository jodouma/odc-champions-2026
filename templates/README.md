# Kit de démarrage

**Pour ne jamais partir d'une page blanche sur un nouveau jeu.** Copie le kit dans ton dossier de travail, puis remplis chaque fichier au moment indiqué.

Le mode d'emploi pas à pas : **[Utiliser les templates](../docs/utiliser-les-templates.md)**.

| Fichier | À quoi il sert | Quand le remplir |
|---|---|---|
| [`../fiches/_modele.md`](../fiches/_modele.md) | La fiche du jeu : règles, format d'entrée et de sortie, limites | Minute 0, puis après chaque promotion |
| [`../starters/python/bot.py`](../starters/python/bot.py) | Squelette de bot Python : lecture, état, coups légaux, note, chrono, debug | Minute 10 : le bot « jamais illégal » |
| [`../starters/cpp/bot.cpp`](../starters/cpp/bot.cpp) | Le même squelette en C++, avec la ligne `#pragma` d'optimisation | Quand la recherche ou la simulation limite la force |
| [`suivi/STATUS.md`](suivi/STATUS.md) | Où on en est : ligue, version en ligne, rang, budget de temps | Après chaque soumission et chaque relevé de rang |
| [`suivi/CHANGELOG.md`](suivi/CHANGELOG.md) | Une ligne par version, et les idées rejetées | À chaque nouvelle version, même non soumise |
| [`suivi/LESSONS.md`](suivi/LESSONS.md) | Erreur → correction → règle | Dès qu'une erreur est trouvée |
| [`suivi/DEFEATS.md`](suivi/DEFEATS.md) | Les défaites comptées par cause | Après chaque lot de parties classées |
| [`suivi/defaites.csv`](suivi/defaites.csv) | Une ligne par défaite lue : `partie,version,cause,tour,note` | Pendant la lecture des défaites |
| [`suivi/versions/`](suivi/versions/) | Le code de chaque version soumise, jamais écrasé | Au moment de chaque soumission |
| [`prompts/`](prompts/) | 5 prompts à copier pour l'IA, avec des `<...>` à remplacer | Voir le tableau ci-dessous |
| [`outils/bilan.py`](outils/bilan.py) | Calcule un duel A/B (avec intervalle de confiance) et compte les défaites du CSV | Avant chaque décision de soumettre |

## Les prompts

| Prompt | Quand |
|---|---|
| [1. Règles → fiche](prompts/01-regles-vers-fiche.md) | Minute 0, et après chaque promotion |
| [2. Premier bot légal](prompts/02-premier-bot-legal.md) | Minute 10 |
| [3. Analyser une défaite](prompts/03-analyser-une-defaite.md) | Après chaque lot de parties classées |
| [4. Prochaine amélioration](prompts/04-prochaine-amelioration.md) | Quand une cause de défaite domine |
| [5. Relire avant de soumettre](prompts/05-relire-avant-soumission.md) | Avant chaque soumission |

## Ce que le kit ne contient pas

- **Aucune stratégie de jeu** : elle dépend du jeu, c'est ton travail.
- **Aucun simulateur** : il est propre à chaque jeu. Le prompt 4 demande comment tester sans le site ; l'[arène](../arena/) sert à s'entraîner au protocole.
- **Pas tes fichiers de suivi remplis** : ils restent dans ton dossier de travail, hors de ce repo public.

## Vérifier les outils

```bash
python3 -m unittest discover templates/outils
```
