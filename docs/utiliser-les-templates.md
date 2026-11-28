# Utiliser les templates : démarrer un nouveau jeu en 30 minutes

**Le point :** sur un jeu inconnu, ne pars jamais d'une page blanche. Copie le [kit](../templates/), remplis les fichiers dans l'ordre ci-dessous, et tu as un bot légal en ligne et un suivi propre en 30 minutes.

Toutes les commandes se lancent **depuis le dossier du repo**. Ton dossier de travail est `../mon-jeu`, **à côté** du repo, jamais dedans : ce repo est public, ton bot et ton suivi restent chez toi.

> Windows : lance les commandes dans Git Bash et remplace `python3` par `py`. Elles ont été testées sur macOS seulement.

---

## Les 30 premières minutes sur un nouveau jeu

1. **Minute 0 : crée ton dossier de travail et copie le suivi.**

   ```bash
   mkdir -p ../mon-jeu
   ```

   ```bash
   cp -R templates/suivi/. ../mon-jeu/
   ```

   Tu as maintenant `STATUS.md`, `CHANGELOG.md`, `LESSONS.md`, `DEFEATS.md`, `defaites.csv` et `versions/`.

2. **Minute 1 : copie la fiche du jeu.**

   ```bash
   cp fiches/_modele.md ../mon-jeu/FICHE.md
   ```

   Remplis-la avec le [prompt 1](../templates/prompts/01-regles-vers-fiche.md). Compare toi-même le format d'entrée avec l'énoncé, ligne par ligne.

3. **Minute 10 : copie le squelette du bot** (Python pour commencer, sauf si la fiche montre tout de suite un jeu de recherche ; voir [langages](langages.md)).

   ```bash
   cp starters/python/bot.py ../mon-jeu/bot.py
   ```

   ou

   ```bash
   cp starters/cpp/bot.cpp ../mon-jeu/bot.cpp
   ```

4. **Minute 12 : remplis les zones « À ADAPTER »** avec le [prompt 2](../templates/prompts/02-premier-bot-legal.md) : constantes, `read_init`, `read_turn`, `legal_moves`. `evaluate` renvoie 0 : pas de stratégie pour l'instant.

5. **Minute 18 : teste en local.** Mets l'exemple d'entrée de l'énoncé dans `../mon-jeu/entree.txt` (copier-coller dans un éditeur), puis :

   ```bash
   python3 ../mon-jeu/bot.py < ../mon-jeu/entree.txt
   ```

   En C++ :

   ```bash
   g++ -std=c++17 -O2 -Wall -o ../mon-jeu/bot ../mon-jeu/bot.cpp
   ```

   ```bash
   ../mon-jeu/bot < ../mon-jeu/entree.txt
   ```

   Tu dois voir `VERSION v1`, puis à chaque tour `entree=...`, un coup, et `t=...ms`. Sur Mac, l'avertissement `unknown pragma ignored` est normal : CodinGame compile avec g++, qui la comprend.

6. **Minute 22 : une partie de test sur le site.** Colle le bot dans l'éditeur CodinGame, lance **une** partie, lis le journal : `VERSION v1` au tour 1, aucune sortie invalide, aucun temps dépassé, et le pire `t=` bien sous la limite.

7. **Minute 25 : soumets (le pilote seulement) et garde la trace.**

   ```bash
   cp ../mon-jeu/bot.py ../mon-jeu/versions/v1.py
   ```

   Ajoute la ligne v1 dans `CHANGELOG.md` et remplis `STATUS.md` (ligue, version en ligne, heure UTC, budget de temps).

8. **Minute 30 : pendant le classement, ne resoumets pas.** Lis le rang seulement à 50 % des parties classées ou plus. Commence la boucle ci-dessous, hors ligne.

---

## La boucle : tester → soumettre → lire les défaites → noter → améliorer

| Étape | Ce que tu fais | Template rempli |
|---|---|---|
| **Améliorer** | Une seule idée, qui vise la cause de défaite la plus fréquente. Change `VERSION`. | [Prompt 4](../templates/prompts/04-prochaine-amelioration.md), `bot.py`, une ligne dans `CHANGELOG.md` |
| **Tester** | 100 parties ou plus contre la version d'avant, départs inversés. Puis le bilan. Puis la relecture du diff. | `bilan.py ab`, [prompt 5](../templates/prompts/05-relire-avant-soumission.md), colonne « Preuve » du `CHANGELOG.md` |
| **Soumettre** | Seulement si le bilan dit « meilleure ». Une seule personne soumet et l'annonce. | `versions/vN.py`, `STATUS.md` |
| **Lire les défaites** | 5 à 10 défaites classées : cause et tour où la partie bascule. | [Prompt 3](../templates/prompts/03-analyser-une-defaite.md), une ligne par défaite dans `defaites.csv` |
| **Noter** | Compter les causes. Noter chaque erreur trouvée en route. | `bilan.py defaites` → `DEFEATS.md` ; `LESSONS.md` |

Les commandes de la boucle :

```bash
python3 templates/outils/bilan.py ab 118 82
```

```text
Parties : 200 (A gagne 118, perd 82, nuls 0)
Taux de A : 59.0 %  (95 % : 52.1 à 65.6 %)
Verdict : A est meilleure que B.
```

Si le verdict est « Pas clair », ne soumets pas : joue plus de parties ou garde l'ancienne version. Ajoute le nombre de nuls en 3e nombre s'il y en a.

```bash
diff ../mon-jeu/versions/v1.py ../mon-jeu/bot.py
```

```bash
python3 templates/outils/bilan.py defaites ../mon-jeu/defaites.csv
```

Le tableau affiché se colle tel quel dans `DEFEATS.md`.

Un temps dépassé alors que les tours d'avant étaient rapides ? C'est un plantage jusqu'à preuve du contraire. En C++, compile avec les vérificateurs et rejoue l'entrée du tour fautif (affichée sur stderr par le squelette) :

```bash
g++ -std=c++17 -O1 -g -fsanitize=address,undefined -o ../mon-jeu/bot_asan ../mon-jeu/bot.cpp
```

```bash
../mon-jeu/bot_asan < ../mon-jeu/entree.txt
```

---

## Qui fait quoi dans une équipe de 4 (proposition)

Les rôles viennent de [la fondation](fondation.md#4-travailler-avec-lia-en-équipe-de-4). Chacun tient ses fichiers :

| Rôle | Fait | Tient |
|---|---|---|
| **Pilote** | Lit l'énoncé, relit après chaque promotion, **seul à soumettre** | `FICHE.md`, `STATUS.md`, `CHANGELOG.md`, `versions/` |
| **Outils** | Le test hors ligne : simulateur ou parties contre l'ancienne version, puis le bilan | `bilan.py ab`, colonne « Preuve » |
| **Bot** | Écrit l'idée suivante avec l'IA, une à la fois | `bot.py` ou `bot.cpp`, prompts 2 et 4 |
| **Relecteur** | Lit les défaites, relit chaque diff, transforme chaque bug en test | `defaites.csv`, `DEFEATS.md`, `LESSONS.md`, prompts 3 et 5 |

À 2 ou 3, le pilote garde son rôle et les autres se partagent le reste.

---

## 5 erreurs que le kit évite

Tirées de nos cinq jeux d'entraînement de novembre 2026.

1. **Une règle codée en dur qui change à la promotion.** Le nombre de tours ou le format d'entrée change, l'ancien bot perd tout. → Les constantes sont en haut du squelette, la fiche est relue à chaque promotion (prompt 1).
2. **Dépasser le temps sur le serveur alors que tout passe en local.** Le serveur est plus lent et irrégulier. → Le squelette n'utilise que la moitié du temps permis et affiche `t=` à chaque tour : lis le pire.
3. **Prendre un plantage pour une lenteur.** Un temps dépassé après des tours rapides était un bug. → Le squelette affiche l'entrée lue à chaque tour ; la commande ASan ci-dessus trouve la ligne fautive.
4. **Décider sur 10 ou 20 parties.** 53 %, 56 %, 52 % : chaque run disait autre chose. → `bilan.py ab` donne l'intervalle et refuse de trancher sous 100 parties.
5. **Ne plus savoir ce qui est en ligne, ou perdre la version qui marchait.** → `VERSION` au tour 1 dans chaque journal, `versions/` jamais écrasé, une ligne par version dans `CHANGELOG.md`, une seule personne soumet.

---

## Après : partager ce que tu as trouvé

Une trouvaille utile aux autres (un piège, une règle qui change, une mesure) va dans le repo commun, en **un petit fichier**, sans code de bot : voir [Contribuer](../CONTRIBUTING.md). Une leçon valable pour tous les jeux va dans le tableau « Erreur → correction → règle » des [bonnes pratiques](bonnes-pratiques.md).

Tes fichiers de suivi, ton bot et tes prompts remplis restent dans `../mon-jeu`, hors du repo.
