# Comment on utilise l'IA

**Notre règle : l'IA propose, l'équipe décide.** Le règlement autorise les LLM, et prévoit leur usage en mode agent pour les épreuves de bots et d'optimisation.

## Ce que CodinGame fournit

- Une **API officielle** pour les jeux de bots et d'optimisation. Sa documentation décrit les parties de test, les soumissions, les scores et les rangs.
  - Guide pour agents : <https://www.codingame.com/api/v1/docs/skill>
  - Référence de l'API : <https://www.codingame.com/api/v1/docs/api>
- Pendant l'épreuve, le bouton **« Agent »**, au-dessus de l'éditeur, donne les instructions d'utilisation.
- **Coding Escape n'est pas couvert par l'API** : cette épreuve se joue en équipe, en co-édition dans le navigateur.

## Connecter ton IA à CodinGame (5 minutes)

Colle ce prompt dans ton assistant (Claude Code, Codex ou un autre agent qui peut lancer des commandes). Remplace le nom, la page et l'identifiant par ceux de ton jeu : l'identifiant est la fin de l'adresse de la page.

```text
I want to work on the CodinGame game "Mad Pod Racing" with you.
Game page: https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing
Public id: mad-pod-racing

1. Read https://www.codingame.com/api/v1/docs/llms.txt.
2. Install the CodinGame Agent Skill it links to, and follow it, including the steps to authenticate me.
3. Then work on this game with me.
```

Ce qui se passe ensuite :

1. L'IA lit la documentation et installe le guide de CodinGame.
2. Elle te donne un **lien et un code** : ouvre le lien, connecte-toi à **ton** compte CodinGame et valide le code. Le code expire vite : fais-le tout de suite.
3. Elle peut alors lire les règles, lancer des parties de test, lire les journaux, soumettre et suivre ton rang.

À savoir :

- **Le jeton reste sur ton PC.** Ne le colle jamais dans un groupe, un prompt ou ce repo.
- **Limites** : 10 parties de test par minute et 80 par heure ; 5 soumissions par 5 minutes et 40 par heure.
- **Une soumission peut être refusée** quand la file du jeu est pleine (vu sur Mad Pod Racing le 28 nov). On attend, on ne force pas ; les parties de test continuent de marcher.
- Testé sur notre compte d'entraînement le 27 nov 2026 avec Claude Code. Pour le 3 décembre, on confirme à la session d'information que l'API est ouverte pendant l'épreuve.

## La boucle, toutes les 20 à 30 minutes

1. **Hypothèse** : une idée claire (« on perd quand l'adversaire est proche »).
2. **Génération** : le LLM écrit le code.
3. **Validation** : on teste contre la version précédente.
4. **Go / No-Go** : une seule personne soumet, et note la version.

## Exemple de prompt

```
Voici les règles du jeu et notre bot actuel.
Il perd quand l'adversaire est proche.
Propose UNE amélioration, explique-la en 3 lignes,
puis donne le code complet.
```

## Nos garde-fous

- Une idée par itération.
- Rien n'est soumis sans test.
- On garde toujours la dernière version qui marche.
- Plan de repli : coder sans agent, par copier-coller dans l'éditeur.
- On s'entraîne à l'API **avant** le 3 décembre, sur un jeu public.
