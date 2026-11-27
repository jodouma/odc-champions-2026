# Quel langage pour quelle épreuve ?

**En une phrase :** un bot simple qui marche bat un bot rapide qui plante. On choisit d'abord le langage que l'équipe sait **lire et corriger**, puis on gagne de la vitesse seulement si le jeu le demande.

## Notre recommandation

| Épreuve | Langage conseillé | Pourquoi |
|---|---|---|
| **Bot Programming** (3 et 10 déc) | **Python 3** pour la première version, **C++** si le bot fait de la simulation | La limite de temps par tour est la même pour tous les langages. Si le bot simule des coups, C++ en calcule en général bien plus que Python dans ce temps. |
| **Coding Escape** (9 déc matin) | **Python 3** | Le score dépend du temps de résolution (avec un malus pour les indices et certaines réponses fausses) : il faut écrire vite de petits scripts. |
| **Optimization** (9 déc après-midi) | **Python 3** d'abord, C++ ensuite si besoin | Le classement regarde d'abord le taux de tests réussis. On passe tous les tests, puis on optimise. |

## Bot Programming : Python ou C++ ?

Ce qu'on sait de CodinGame :

- **Même limite de temps pour tout le monde.** Elle est écrite dans l'énoncé de chaque jeu, souvent 1 000 ms au premier tour puis 50 à 100 ms par tour. Un dépassement fait en général perdre la partie.
- **C++ est le langage le plus représenté en haut du classement**, mais pas le seul : dans le top 10 du Spring Challenge 2026, on compte 4 bots en C++, puis Rust, C#, Scala et Python ([classement, site tiers](https://clist.by/standings/spring-challenge-2026-67275504/)).
- **Un bot à règles peut aller très loin.** Le 3e du Spring Challenge 2026 gérait son économie avec des règles, sans recherche de coups ([post-mortem](https://www.yannmoisan.com/spring-challenge-2026-postmortem.html)).
- **Aux qualifications ODC 2025** (une épreuve d'optimisation, pas de bots), Python 3 était le langage le plus utilisé (209 équipes, contre 86 en C++), et le top 3 était C++, C++, Python ([classement](https://www.codingame.com/hackathon/odc-2025-qualifications-kjg654/leaderboard)).

Notre règle de décision, par équipe :

1. **Première heure : Python.** Un bot simple, soumis tôt, qui ne plante jamais.
2. **Ensuite, on se pose une question :** est-ce que notre bot gagnerait à *simuler* des coups (essayer plusieurs actions et garder la meilleure) ?
   - **Non** (le jeu se joue avec de bonnes règles) → on reste en Python et on améliore les règles.
   - **Oui** → on passe en C++. On teste une version C++ et on la compare au bot Python. Condition : **au moins 2 personnes capables de relire du C++**.
3. **On ne change jamais de langage dans la dernière heure.**

### Si on code en C++

D'après l'équipe CodinGame (messages de 2016 et 2017 sur le forum), le C++ y est compilé **sans option d'optimisation**. Les joueurs ajoutent donc cette ligne **tout en haut du fichier, avant les `#include`** :

```cpp
#pragma GCC optimize("O3,omit-frame-pointer,inline")
```

Dans un test publié en avril 2025, cette ligne faisait passer un calcul de 7,5 s à 4,9 s ([forum CodinGame](https://forum.codingame.com/t/spring-challenge-2025/206389?page=4)). Vérifie son effet sur le jeu du jour avant de compter dessus. Compilateur indiqué par CodinGame : g++ 11.2.0 en mode C++20.

### Et Rust, Java, C# ?

- **Rust** : à envisager seulement si quelqu'un le maîtrise déjà. Ce n'est pas le moment de l'apprendre.
- **Java / C#** : possibles. Un retour d'expérience du Summer Challenge 2024 signale des dépassements de temps liés au ramasse-miettes (GC).
- **Le bon choix reste celui que l'équipe relit sans effort.**

### Python : ce qui est disponible

Python 3.11 avec **NumPy, pandas et SciPy**. PyPy ne figure pas dans la liste. Limites pour tous les langages : 100 000 caractères de code, 768 Mo de mémoire ([liste des langages CodinGame](https://github.com/CodinGame/Contribute-Help/blob/64e9ef72fcda5a05eef38239596aa0e5068da6ed/pages/technical/languages.md)).

## Ce qu'on vérifiera le 30 novembre

- La durée exacte des qualifications (le règlement dit 9h–16h, la présentation dit 6 h).
- Les limites de temps par tour du jeu choisi.
- Si l'épreuve d'optimisation a une limite de temps de calcul.
