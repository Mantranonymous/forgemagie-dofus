#!/usr/bin/env python3
"""
Lit tous les fichiers data/items_by_type/*.json et affiche les items par
tranche de niveau pour aider à choisir les items "stars" du leveling guide.

Usage : python scripts/show_items_by_level.py [--limit 8]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "items_by_type"

TYPES = {
    "Anneau": "9_anneau",
    "Amulette": "1_amulette",
    "Cape": "17_cape",
    "Chapeau": "16_chapeau",
    "Bottes": "11_bottes",
    "Ceinture": "10_ceinture",
    "Épée": "6_epee",
    "Marteau": "7_marteau",
    "Dague": "5_dague",
    "Pelle": "8_pelle",
    "Baguette": "3_baguette",
    "Bâton": "4_baton",
    "Arc": "2_arc",
    "Hache": "19_hache",
    "Faux": "22_faux",
}

BUCKETS = [
    (1, 10), (10, 20), (20, 35), (35, 50),
    (50, 75), (75, 100), (100, 125), (125, 150),
    (150, 175), (175, 200), (200, 250),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=8, help="Nb d'items à afficher par tranche")
    parser.add_argument("--filter", type=str, default=None, help="Filtrer par sous-string dans le nom")
    args = parser.parse_args()

    for type_label, file_stem in TYPES.items():
        path = DATA_DIR / f"{file_stem}.json"
        if not path.exists():
            print(f"\n=== {type_label} === (pas de fichier {file_stem}.json — skip)")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        items = data["items"]
        if args.filter:
            items = [it for it in items if args.filter.lower() in it["name"].lower()]

        print(f"\n{'=' * 60}")
        print(f"  {type_label}  ({len(items)} items)")
        print('=' * 60)

        for lo, hi in BUCKETS:
            bucket = [it for it in items if lo <= it["level"] < hi]
            if not bucket:
                continue
            print(f"\n  Lvl {lo}-{hi} ({len(bucket)}) :")
            # tri par level
            for it in bucket[:args.limit]:
                print(f"    [{it['level']:>3}] {it['name']:<40s} id={it['id']}")
            if len(bucket) > args.limit:
                print(f"        ... +{len(bucket) - args.limit} autres")


if __name__ == "__main__":
    main()
