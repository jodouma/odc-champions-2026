# Bronze : la règle exacte des rebonds, pour ton simulateur

- **Jeu :** Mad Pod Racing
- **Ligue :** Bronze
- **Date :** 2026-11-27
- **Type :** mesure
- **Source :** notre essai (5 parties sondes) ; règle de départ tirée du referee communautaire robostac/coders-strike-back-referee

## Erreur

Notre simulateur ignorait un choc qui arrive pile à la fin d'un tour. Dès le tour 2, ses positions ne correspondaient plus à celles du serveur.

## Correction

On a vérifié chaque détail contre le serveur :
- deux pods se touchent à 800 unités de centre à centre (rayon 400 chacun) ;
- un contact pile à la fin du tour compte comme un choc ;
- la poussée vaut la moitié de la vitesse de rapprochement plus 120 quand le choc est doux, la vitesse de rapprochement entière sinon ;
- deux pods qui se chevauchent sont remis à 800 unités l'un de l'autre ;
- à la fin du tour seulement : positions arrondies, vitesses × 0,85 tronquées.

## Règle

Avant de faire confiance à un simulateur, rejoue des vraies parties pleines de chocs et vérifie qu'il retrouve chaque position.

## Preuve

5 parties sondes en Bronze (dont 2 où notre bot fonce sur une copie de lui-même) : 494 tours et 80 rebonds rejoués avec zéro erreur de position.

## Confirmé par

- [Ajoute une ligne ici si tu as retrouvé la même chose : date, ligue, ton chiffre.]
