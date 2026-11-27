# Contribuer au repo

**En bref :** ce repo est la base commune des équipes. L'objectif est la ligue **Légende** ; chaque trouvaille utile sur le chemin va ici, dans **son propre petit fichier**.

## Ajouter une trouvaille (2 minutes, sans rien installer)

1. Ouvre le dossier `trouvailles/` du jeu, par exemple [`fiches/tron-battle/trouvailles/`](fiches/tron-battle/trouvailles/).
2. Clique sur **Add file → Create new file**.
3. Nomme le fichier `AAAA-MM-JJ-sujet-court.md`, par exemple `2026-11-28-piege-murs.md`.
4. Colle le contenu de [`fiches/_modele-trouvaille.md`](fiches/_modele-trouvaille.md) et remplis-le.
5. Clique sur **Commit changes → Propose changes**, puis **Create pull request**. Le coach relit et valide.

Un exemple rempli : [`2026-11-27-budget-temps.md`](fiches/tron-battle/trouvailles/2026-11-27-budget-temps.md).

## Pourquoi un fichier par trouvaille

Deux personnes peuvent contribuer au même jeu, à la même ligue, le même jour : chacune écrit dans **son** fichier, donc git n'a jamais de conflit à résoudre.

| Situation | Quoi faire |
|---|---|
| Quelqu'un a déjà écrit **la même trouvaille** | N'en crée pas une seconde : ajoute une ligne dans sa section « Confirmé par » (date, ligue, ton chiffre). Deux essais qui disent pareil, c'est une preuve plus forte. |
| Ta trouvaille **contredit** une autre | Écris la tienne quand même, avec ta ligue, ta date et ta preuve. Le coach tranche, ou la note « à vérifier ». |
| Deux fichiers ont **le même nom** | Ajoute ton pseudo à la fin : `2026-11-28-piege-murs-pseudo.md`. |
| Tu veux **corriger** la trouvaille d'un autre | Propose la correction dans une pull request, avec ta preuve. |

## Où mettre quoi

| Tu as trouvé… | Ça va dans… |
|---|---|
| Une astuce, un piège ou une mesure sur **un jeu précis** | un nouveau fichier dans `fiches/<jeu>/trouvailles/` |
| Un changement de **ligue ou de rang** | la fiche du jeu, `fiches/<jeu>/README.md` : la ligne « Où on en est » (avec date et heure) et une ligne dans « Le chemin » |
| Une règle valable pour **tous les jeux** | [`docs/bonnes-pratiques.md`](docs/bonnes-pratiques.md), tableau « Erreur → correction → règle » |
| Un **nouveau jeu** d'entraînement | un nouveau dossier `fiches/<jeu>/` : copie [`fiches/_modele.md`](fiches/_modele.md) en `README.md` et crée `trouvailles/` |
| Ton **pseudo CodinGame** | [`docs/jouer-ensemble.md`](docs/jouer-ensemble.md), section « Nos pseudos » |
| Un outil ou un squelette **générique** | [`starters/`](starters/) ou [`arena/`](arena/) |

Les fiches des jeux sont le **résumé** : le coach y reporte régulièrement les meilleures trouvailles. Tu n'as pas besoin d'y toucher pour partager une astuce.

## Ce qu'une bonne trouvaille contient

- **La ligue et la date** : une astuce de Bois ne vaut pas toujours en Argent.
- **Erreur → correction → règle** : ce qui s'est mal passé, ce que tu as changé, ce qu'on retient.
- **Une preuve chiffrée** : « 14 victoires sur 20 contre la version précédente ». Un chiffre sans source ne compte pas.
- **Des mots simples** : un débutant doit comprendre.

## Avec git, si tu préfères

Une branche par contribution, jamais de push direct sur `main` :

```bash
git checkout -b trouvaille-tron-murs
```

```bash
git add fiches/tron-battle/trouvailles/2026-11-28-piege-murs.md
```

```bash
git commit -m "fiches: Tron Battle, piège des murs en Bronze"
```

```bash
git push origin trouvaille-tron-murs
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

- [ ] Un fichier à moi, bien nommé, dans le bon dossier `trouvailles/` ?
- [ ] La ligue, la date et la preuve y sont ?
- [ ] J'ai vérifié que la trouvaille n'existe pas déjà ?
- [ ] Rien de privé, aucun code de compétition ?
