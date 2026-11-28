# Prompt 4 : proposer la prochaine amélioration, avec son plan de preuve

**Quand :** quand `DEFEATS.md` montre une cause principale. Une idée à la fois.

**Ce que tu colles :** la fiche, le tableau de `DEFEATS.md`, les dernières lignes de `CHANGELOG.md` (idées rejetées comprises) et le fichier du bot actuel.

```text
Voici la fiche d'un jeu CodinGame, nos défaites classées par cause, notre journal de versions
(avec les idées déjà rejetées) et notre bot actuel <version>.

<colle la fiche>
<colle le tableau de DEFEATS.md>
<colle CHANGELOG.md>
<colle le bot>

1. Propose UNE amélioration qui vise la cause la plus fréquente. Pas une idée déjà rejetée.
   Explique-la en 3 lignes.
2. Dis ce qu'elle coûte en temps de calcul par tour, comparé au budget de <25> ms.
3. Donne le plan de preuve :
   - comment tester sans le site (simulateur local, ou parties contre la version précédente) ;
   - combien de parties (100 au moins, départs inversés) et quel résultat attendu ;
   - ce qu'on doit voir dans le journal pour être sûr que le changement a bien eu lieu.
4. Seulement ensuite : le fichier complet, avec VERSION = "<v suivante>".
```

**Vérifie après :** fais tourner le plan de preuve, puis `python3 templates/outils/bilan.py ab <victoires> <défaites>`. Note le résultat dans `CHANGELOG.md`, même si l'idée est rejetée.
