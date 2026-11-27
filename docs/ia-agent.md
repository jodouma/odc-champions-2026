# Comment on utilise l'IA

**Notre règle : l'IA propose, l'équipe décide.** Le règlement autorise les LLM, et prévoit leur usage en mode agent pour les épreuves de bots et d'optimisation.

## Ce que CodinGame fournit

- Une **API officielle** pour les jeux de bots et d'optimisation. Sa documentation décrit les parties de test, les soumissions, les scores et les rangs.
  - Guide pour agents : <https://www.codingame.com/api/v1/docs/skill>
  - Référence de l'API : <https://www.codingame.com/api/v1/docs/api>
- Pendant l'épreuve, le bouton **« Agent »**, au-dessus de l'éditeur, donne les instructions d'utilisation.
- **Coding Escape n'est pas couvert par l'API** : cette épreuve se joue en équipe, en co-édition dans le navigateur.

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
