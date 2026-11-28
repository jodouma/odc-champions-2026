# Prompt 3 : analyser une défaite et la classer

**Quand :** après chaque lot de parties classées, pour chaque défaite lue (commence par 5 à 10).

**Ce que tu colles :** le journal de la partie perdue (le texte du replay, avec ton stderr si le site le montre), la fiche, et la liste de causes déjà utilisée dans ton `DEFEATS.md`.

```text
Voici le journal d'une partie perdue par notre bot <version> dans un jeu CodinGame,
la fiche du jeu, et nos causes de défaite déjà connues.

<colle le journal>

<colle la fiche>

Causes connues : <coup illégal, temps dépassé, plantage, moins bon tôt, moins bon en fin de partie, ...>

1. Est-ce une faute (sortie invalide, temps dépassé, plantage) ? Cite la ligne du journal.
   Un temps dépassé alors que les tours d'avant étaient rapides : traite-le comme un plantage
   et montre la dernière entrée lue sur stderr.
2. Sinon, trouve le tour où la partie a basculé (souvent bien avant la fin) et dis pourquoi,
   en 2 lignes, avec ce que le journal montre à ce tour.
3. Choisis UNE cause dans la liste. Si aucune ne va, propose un nom court de nouvelle cause.
4. Donne une ligne CSV : partie,version,cause,tour,note
Ne propose pas de correction de code.
```

**Vérifie après :** ouvre le replay au tour indiqué et regarde toi-même. Puis ajoute la ligne dans `defaites.csv`.
