# versions/

> Un fichier par version soumise, copié au moment de la soumission. On n'écrase jamais un fichier.

- Nom : `v1.py`, `v2.py`, `v3.cpp` : le numéro de la ligne du `CHANGELOG.md`.
- La constante `VERSION` dans le fichier vaut ce même numéro : on la retrouve au tour 1 sur stderr, dans les journaux de test.
- Une version moins bonne ? On resoumet le fichier de la version d'avant, sans rien changer.
- Une idée en essai, pas encore soumise : `v4-essai.py`. Elle devient `v4.py` seulement si elle est soumise.

Copier la version qui part en ligne (exemple pour v2 en Python) :

```bash
cp bot.py versions/v2.py
```
