# Prompt 5 : relire le changement avant de soumettre

**Quand :** juste avant chaque soumission, après le test. De préférence par une autre IA ou une autre personne que celle qui a écrit le code.

**Ce que tu colles :** la différence entre la version en ligne et la nouvelle (par exemple la sortie de `diff versions/v2.py bot.py`), et la fiche.

```text
Voici la fiche d'un jeu CodinGame et la différence entre notre bot en ligne (<v2>)
et le candidat (<v3>).

<colle la fiche>

<colle le diff>

Relis ce changement comme un relecteur exigeant. Cherche, dans cet ordre :
1. un coup qui peut devenir illégal (liste vide, indice hors limites, case interdite) ;
2. un tour qui peut dépasser le budget (boucle sans contrôle du chrono, recherche sans limite) ;
3. une entrée mal lue (ligne oubliée, format de la nouvelle ligue) ;
4. une constante codée en dur qui devrait venir de l'entrée (nombre de tours, taille, joueurs) ;
5. un réglage qui ne change rien en pratique.
Pour chaque problème : la ligne, le cas qui le déclenche, la correction en une phrase.
Si tu ne trouves rien, dis-le. Termine par : « VERSION vaut bien <v3> : oui / non ».
```

**Vérifie après :** chaque problème trouvé devient d'abord un test qui échoue, puis on corrige. Ensuite seulement, une personne soumet et copie le fichier dans `versions/`.
