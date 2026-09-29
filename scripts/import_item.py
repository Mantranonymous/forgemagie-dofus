#!/usr/bin/env python3
"""
Importe un item depuis l'API DofusDB et l'ajoute à data/items.json.

Usage :
    python scripts/import_item.py <DOFUSDB_ID> [slug-optionnel]

Exemple :
    python scripts/import_item.py 8876 voile-encre

L'API publique DofusDB ne fournit PAS le poids max FM ni les coefficients de poids
(c'est de la data communauté décryptée du client Dofus). Ce script récupère
le nom, le level, le type et tous les jets max via le mapping characteristicId.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.dofusdb.fr"
ROOT = Path(__file__).resolve().parent.parent
ITEMS_FILE = ROOT / "data" / "items.json"

# Mapping characteristicId → clé interne du calculateur.
# Source : api.dofusdb.fr/characteristics (récupéré 2026-05-18).
# Stable car les IDs viennent du client Dofus.
CHAR_ID_TO_STAT = {
    10: "force",
    11: "vitalite",
    12: "sagesse",
    13: "chance",
    14: "agilite",
    15: "intelligence",
    16: "dommages",          # allDamageBonus (générique)
    18: "pctCritique",
    19: "portee",
    23: "pm",                # movementPoints
    25: "dommagesPct",       # damagePercent (Puissance)
    33: "pctResTerre",
    34: "pctResFeu",
    35: "pctResEau",
    36: "pctResAir",
    37: "pctResNeutre",
    44: "initiative",
    48: "prospection",
    49: "soins",
    50: "renvoi",
    54: "resFixeTerre",
    # Note : il manque PA (1 ?), tacle, esquive, etc. — à compléter en
    # rencontrant ces stats sur de nouveaux items.
}

# Typage des items (typeId DofusDB → label lisible). À enrichir au besoin.
TYPE_ID_TO_LABEL = {
    1: "amulette",
    9: "anneau",
    11: "bottes",
    16: "ceinture",
    17: "cape",
}


def http_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "fm-import/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def extract_label(field) -> str | None:
    """Les noms DofusDB sont des objets multilingues {fr, en, ...}."""
    if isinstance(field, dict):
        return field.get("fr") or field.get("en")
    if isinstance(field, str):
        return field
    return None


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def build_preset(item_id: int, override_slug: str | None) -> tuple[str, dict]:
    item = http_get(f"{API}/items/{item_id}")

    name_fr = extract_label(item.get("name")) or f"item-{item_id}"
    level = item.get("level")
    type_id = item.get("typeId")
    type_label = TYPE_ID_TO_LABEL.get(type_id, f"typeId-{type_id}")

    print(f"\n→ Item : {name_fr} (lvl {level}, type {type_label})")
    print(f"  Effets : {len(item.get('effects', []))}")

    jets_max: dict[str, int] = {}
    malus: list[tuple[str, int, int]] = []  # (stat_key, min, max) quand min > max
    unmapped: list[tuple[int | None, int | None, int, int]] = []

    for eff in item.get("effects", []):
        char_id = eff.get("characteristic")
        # l'API peut renvoyer les champs sous "from/to" ou "min/max" selon la version
        emin = eff.get("from", eff.get("min", 0)) or 0
        emax = eff.get("to", eff.get("max", 0)) or 0
        stat_key = CHAR_ID_TO_STAT.get(char_id)

        if not stat_key:
            unmapped.append((eff.get("effectId"), char_id, emin, emax))
            continue

        # cas malus (min > max → ex. Portée 1→0 = -1 portée)
        if emin > emax:
            malus.append((stat_key, emin, emax))
            jets_max[stat_key] = jets_max.get(stat_key, 0) - emin
        else:
            jets_max[stat_key] = jets_max.get(stat_key, 0) + emax

    slug = override_slug or slugify(name_fr)

    preset = {
        "label": name_fr,
        "dofusdbId": item_id,
        "level": level,
        "type": type_label,
        "validateUrl": f"https://dofusdb.fr/fr/database/item/{item_id}",
        "_unverified": False,
        "jetsMax": jets_max,
    }
    if malus:
        preset["malusNote"] = [
            f"{k} : malus {emin}→{emax}" for k, emin, emax in malus
        ]

    print(f"\n  Slug   : {slug}")
    print(f"  Stats  : {dict(sorted(jets_max.items()))}")
    if malus:
        print(f"  Malus  : {malus}")
    if unmapped:
        print(f"\n  ⚠️  {len(unmapped)} effet(s) non mappé(s) — étendre CHAR_ID_TO_STAT :")
        for eid, cid, emin, emax in unmapped:
            print(f"     - effectId={eid} characteristicId={cid} min={emin} max={emax}")

    return slug, preset


def merge_into_items_file(slug: str, preset: dict) -> None:
    if ITEMS_FILE.exists():
        data = json.loads(ITEMS_FILE.read_text(encoding="utf-8"))
    else:
        data = {"_meta": {}, "items": {}}

    data.setdefault("items", {})[slug] = preset
    data.setdefault("_meta", {})["lastUpdated"] = _dt.date.today().isoformat()
    data["_meta"]["description"] = (
        "Presets d'items pour le calculateur de FM. "
        "Le poids max est auto-calculé côté HTML à partir des jets max × coefs poids."
    )

    ITEMS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"\n  ✓ Écrit dans {ITEMS_FILE.relative_to(ROOT)}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    try:
        item_id = int(sys.argv[1])
    except ValueError:
        print(f"Erreur : item_id doit être un entier, reçu '{sys.argv[1]}'")
        sys.exit(1)
    override_slug = sys.argv[2] if len(sys.argv) >= 3 else None

    slug, preset = build_preset(item_id, override_slug)
    merge_into_items_file(slug, preset)
    print(
        f"\n  💡 Le calculateur HTML a une copie inline des presets dans index.html — "
        f"resync manuel pour l'instant."
    )


if __name__ == "__main__":
    main()
