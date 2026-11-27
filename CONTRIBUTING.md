# Contribuer au repo

**En bref :** ce repo est la base commune des équipes. L'objectif est la ligue **Légende** ; chaque trouvaille utile sur le chemin va ici, au bon endroit, en une ligne claire.

## Où mettre quoi

| Tu as trouvé… | Ça va dans… |
|---|---|
| Une astuce ou un piège sur **un jeu précis** | la fiche du jeu dans [`fiches/`](fiches/), section « Journal des trouvailles » |
| Une règle valable pour **tous les jeux** | [`docs/bonnes-pratiques.md`](docs/bonnes-pratiques.md), tableau « Erreur → correction → règle » |
| Un **nouveau jeu** d'entraînement | une nouvelle fiche : copie [`fiches/_modele.md`](fiches/_modele.md) |
| Un changement de **ligue ou de rang** | la ligne « Où on en est » de la fiche du jeu, avec la date et l'heure, et une ligne dans « Le chemin » : ce que la nouvelle ligue ajoute et ce qu'il a fallu pour passer |
| Ton **pseudo CodinGame** | [`docs/jouer-ensemble.md`](docs/jouer-ensemble.md), section « Nos pseudos » |
| Un outil ou un squelette **générique** | [`starters/`](starters/) ou [`arena/`](arena/) |

## Le format d'une trouvaille

Une ligne, toujours dans cet ordre :

```
| 27 nov 15:10 | Bois 1 | 100 tours codés en dur → lu l'énoncé de la nouvelle ligue → relire l'énoncé après chaque promotion | notre essai |
```

- **Date et heure** en UTC, **ligue** au moment de la trouvaille.
- **Erreur → correction → règle** : ce qui s'est mal passé, ce que tu as changé, ce qu'on retient.
- **Source** : « notre essai » ou un lien. Un chiffre sans source ne compte pas.

## Comment envoyer ta contribution

Le plus simple, sans rien installer :

1. Ouvre le fichier sur GitHub et clique sur le crayon ✏️ (« Edit this file »).
2. Ajoute ta ligne.
3. En bas, écris un titre court (ex. `fiches: Tron Battle, piège du budget temps`) et clique sur **Propose changes**.
4. Clique sur **Create pull request**. Le coach relit et valide.

Avec git, si tu préfères :

```bash
git checkout -b ma-trouvaille
```

```bash
git commit -am "fiches: Tron Battle, piège du budget temps"
```

```bash
git push origin ma-trouvaille
```

Puis ouvre une pull request sur GitHub.

## Ce qu'on ne met jamais ici

Ce repo est **public**.

- ❌ **Aucun code de compétition**, ni prompt utilisé pendant une épreuve : le règlement interdit le partage de code entre équipes.
- ❌ Pas d'autres bots complets : un seul exemple de départ est publié ([`examples/tron-battle`](examples/tron-battle/)). Pour le reste, on partage la **méthode**, pas la solution.
- ❌ Pas de noms, d'e-mails, de numéros de téléphone, de notes ou de rangs de classe.
- ❌ Pas de jeton, de mot de passe ou de lien de connexion.
- ❌ Pas de documents de l'organisateur.

## Avant de valider

- [ ] C'est au bon endroit (jeu précis ou règle générale) ?
- [ ] La date, la ligue et la source y sont ?
- [ ] Un débutant comprend la phrase ?
- [ ] Rien de privé, aucun code de compétition ?
