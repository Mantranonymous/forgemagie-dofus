#!/usr/bin/env python3
"""
Récupère TOUS les items d'un type donné depuis l'API DofusDB en paginant,
et écrit le résultat dans data/items_by_type/<typeId>.json.

Usage :
    python scripts/fetch_items_by_type.py <typeId> [type_label]

Exemple :
    python scripts/fetch_items_by_type.py 9 anneau
    python scripts/fetch_items_by_type.py 17 cape

TypeIds connus (validés via /item-types) :
    1  = Amulette
    9  = Anneau
    10 = Ceinture
    11 = Bottes
    16 = Chapeau
    17 = Cape
    2  = Arc, 3 = Baguette, 4 = Bâton, 5 = Dague, 6 = Épée
    7  = Marteau, 8 = Pelle, 19 = Hache, 22 = Faux

Le script écrit un JSON simplifié : [{id, name, level, levelMin, slug}, ...]
trié par level croissant.
"""

from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
import urllib.request
from pathlib import Path

API = "https://api.dofusdb.fr"
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data" / "items_by_type"
OUT_DIR.mkdir(parents=True, exist_ok=True)

PAGE_SIZE = 50  # DofusDB renvoie max ~50 par page semble-t-il


def http_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "fm-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read())


def extract_label(field) -> str | None:
    if isinstance(field, dict):
        return field.get("fr") or field.get("en")
    if isinstance(field, str):
        return field
    return None


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def fetch_all_items(type_id: int) -> list[dict]:
    """Pagine sur /items?typeId=<id> et retourne la liste complète."""
    out: list[dict] = []
    skip = 0
    total: int | None = None

    while True:
        url = (
            f"{API}/items?typeId={type_id}"
            f"&$limit={PAGE_SIZE}&$skip={skip}"
            f"&$sort[level]=1"
        )
        print(f"  → fetch skip={skip} ...", end=" ", flush=True)
        data = http_get(url)
        if total is None:
            total = data.get("total", 0)
            print(f"(total={total})")
        else:
            print()

        for it in data.get("data", []):
            name = extract_label(it.get("name")) or f"item-{it.get('id')}"
            # garder uniquement les items "vrais" (level > 0, exchangeable, sale)
            level = it.get("level", 0) or 0
            if level < 1:
                continue
            out.append({
                "id": it.get("id"),
                "name": name,
                "level": level,
                "slug": slugify(name),
                "exchangeable": it.get("exchangeable", True),
                "isSaleable": it.get("isSaleable", True),
                "isLegendary": it.get("isLegendary", False),
            })

        skip += PAGE_SIZE
        if total and skip >= total:
            break
        # safety
        if skip > 5000:
            print("  ⚠️ skip > 5000, on stoppe")
            break
        time.sleep(0.1)

    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    try:
        type_id = int(sys.argv[1])
    except ValueError:
        print(f"Erreur : typeId doit être un entier, reçu '{sys.argv[1]}'")
        sys.exit(1)
    type_label = sys.argv[2] if len(sys.argv) >= 3 else f"type-{type_id}"

    print(f"\n→ Récupération de tous les items de typeId={type_id} ({type_label})...")
    items = fetch_all_items(type_id)

    # tri final par level
    items.sort(key=lambda x: (x["level"], x["name"]))

    # filtrer les items non saleable / non exchangeable (souvent des items spéciaux)
    saleable = [it for it in items if it["isSaleable"] and it["exchangeable"]]

    out_file = OUT_DIR / f"{type_id}_{type_label}.json"
    out_file.write_text(json.dumps({
        "_meta": {
            "typeId": type_id,
            "typeLabel": type_label,
            "total": len(items),
            "totalSaleable": len(saleable),
            "fetchedAt": __import__("datetime").datetime.now().isoformat(),
        },
        "items": saleable
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  ✓ {len(items)} items récupérés ({len(saleable)} échangeables)")
    print(f"  ✓ Écrit dans {out_file.relative_to(ROOT)}")

    # afficher un résumé par tranche de level
    print("\n  Distribution par tranche de level :")
    buckets = [(1, 20), (20, 50), (50, 100), (100, 150), (150, 200), (200, 250)]
    for lo, hi in buckets:
        count = sum(1 for it in saleable if lo <= it["level"] < hi)
        print(f"    Lvl {lo:>3}-{hi:<3} : {count} items")


if __name__ == "__main__":
    main()
