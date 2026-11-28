#!/usr/bin/env python3
"""Deux petits calculs pour décider sur des chiffres, pas sur une impression.

  python3 templates/outils/bilan.py ab 118 82 [nuls]
      Résultat d'un duel A contre B (parties jumelées, départs inversés) :
      taux de victoire de A, intervalle de confiance à 95 %, verdict.

  python3 templates/outils/bilan.py defaites defaites.csv
      Compte les défaites par cause à partir du CSV rempli à la main
      (colonnes : partie,version,cause,tour,note) et affiche le tableau
      à coller dans DEFEATS.md.

Aucune dépendance : Python 3.8+ suffit.
"""
import argparse
import csv
import math
import sys
from collections import Counter

MIN_GAMES = 100  # en dessous, on ne décide pas (bonnes pratiques, règle 6)


def wilson(wins, n, z=1.96):
    """Intervalle de Wilson à 95 % pour une proportion (wins peut être un demi-entier)."""
    if n == 0:
        return 0.0, 1.0
    p = wins / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def ab_report(wins, losses, draws=0):
    """Renvoie le texte du bilan A/B. Un nul compte pour une demi-victoire."""
    n = wins + losses + draws
    if n == 0:
        return "Aucune partie : rien à juger."
    score = wins + 0.5 * draws
    lo, hi = wilson(score, n)
    lines = [
        f"Parties : {n} (A gagne {wins}, perd {losses}, nuls {draws})",
        f"Taux de A : {100 * score / n:.1f} %  (95 % : {100 * lo:.1f} à {100 * hi:.1f} %)",
    ]
    if lo > 0.5:
        verdict = "A est meilleure que B."
    elif hi < 0.5:
        verdict = "A est moins bonne que B : garde B."
    else:
        verdict = "Pas clair : l'intervalle contient 50 %. Joue plus de parties ou garde B."
    if n < MIN_GAMES:
        verdict += f" Attention : moins de {MIN_GAMES} parties, ne décide pas encore."
    lines.append("Verdict : " + verdict)
    return "\n".join(lines)


def read_defeats(path):
    """Lit le CSV des défaites. Ignore les lignes vides ; la cause est obligatoire."""
    with open(path, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]
    for i, r in enumerate(rows, start=2):
        if not (r.get("cause") or "").strip():
            raise ValueError(f"ligne {i} : la colonne « cause » est vide")
    return rows


def defeats_table(rows):
    """Tableau Markdown des causes, de la plus fréquente à la plus rare."""
    if not rows:
        return "Aucune défaite dans le fichier."
    counts = Counter(r["cause"].strip() for r in rows)
    example = {}
    for r in rows:
        example.setdefault(r["cause"].strip(), (r.get("partie") or "").strip())
    total = len(rows)
    lines = [
        f"{total} défaites lues.",
        "",
        "| Cause | Nombre | % | Exemple de partie |",
        "|---|---|---|---|",
    ]
    for cause, k in counts.most_common():
        lines.append(f"| {cause} | {k} | {100 * k / total:.0f} % | {example[cause] or '-'} |")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Bilan A/B et tri des défaites.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    ab = sub.add_parser("ab", help="duel A contre B : victoires, défaites, nuls")
    ab.add_argument("victoires", type=int)
    ab.add_argument("defaites", type=int)
    ab.add_argument("nuls", type=int, nargs="?", default=0)
    df = sub.add_parser("defaites", help="compte les défaites par cause depuis un CSV")
    df.add_argument("csv")
    args = parser.parse_args(argv)

    if args.cmd == "ab":
        if min(args.victoires, args.defaites, args.nuls) < 0:
            parser.error("les nombres doivent être positifs")
        print(ab_report(args.victoires, args.defaites, args.nuls))
    else:
        try:
            print(defeats_table(read_defeats(args.csv)))
        except (OSError, ValueError) as e:
            print(f"Erreur : {e}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
