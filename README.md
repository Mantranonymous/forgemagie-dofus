# Forgemagie Dofus — Projet Tylezia

**Objectif** : devenir rentable en forgemagie sur Tylezia (mono-compte). On vise le profit, pas le challenge esthétique.

## Pourquoi ce projet

Sur Tylezia, mono-compte, les **exos PA/PM/Po** se vendent en or massif et les builds PvP/PvM sont diversifiés. Une FM maîtrisée = un avantage économique énorme :
- Acheter un item brut sous-coté → FM → revendre 2-5x
- Vendre les services de FM exo (PA/PM)
- Arbitrer le marché runes ↔ items finis

## Roadmap

### Phase 1 — Maîtrise mécanique (savoir = arrêter de perdre)
- [x] Structure projet
- [x] KB fondamentaux : vocabulaire, mécaniques, poids ([01](kb/01-fondamentaux.md))
- [x] KB runes et poids : tableau coefs ([02](kb/02-runes-et-poids.md))
- [x] KB exo PA playbook ([03](kb/03-exo-pa-playbook.md))
- [ ] KB lecture d'item : repérer un jet sous/surcoté en 2 sec
- [ ] **Calibration coefs Dofus 3 / Unity** (in-game, à faire en priorité)

### Phase 2 — Calculateurs (décisions chiffrées)
- [ ] Calc poids : stat actuelle → stat voulue, coût en runes
- [ ] Calc proba exo : PA/PM/Po, espérance de gain
- [ ] Calc ROI : prix item + runes vs valeur revente

### Phase 3 — Arbitrage marché HDV Tylezia
- [ ] Base de prix runes (mise à jour manuelle au début)
- [ ] Détecteur d'items sous-cotés à FM
- [ ] Watchlist d'opportunités

### Phase 4 — Tracker & assistant externe (optionnel)
- [ ] Tracker de mes tentatives (input/output, runes consommées, gain net)
- [ ] App externe : screenshot d'item → reco de FM (zéro injection client, conforme CGU Ankama)

## Structure

```
forgemagie-dofus/
├── README.md              ← tu es ici
├── kb/                    ← base de connaissances (markdown)
├── tools/                 ← outils HTML/JS interactifs (à ouvrir dans le navigateur)
├── data/                  ← référentiels (poids runes, prix HDV…)
├── scripts/               ← scripts Python (scraping, calculs lourds)
└── tracker/               ← logs de mes sessions FM (phase 4)
```

## Comment l'utiliser

1. Lire les fichiers `kb/` dans l'ordre (01 → 02 → …)
2. Ouvrir les outils dans le navigateur — point d'entrée recommandé : `open tools/calc-poids/index.html`
   - Onglet **Calc poids** : calculateur de poids et conversion runes
   - Onglet **Leveling FM** : tuto guidé par métier (Bijoutomage, Cordomage, Costumage, Armes)
3. Importer un nouvel item d'un site DofusDB : `python3 scripts/import_item.py <DOFUSDB_ID>`
4. Tenir à jour `data/prices-tylezia.json` avec les prix runes vus en HDV
5. Logger chaque session FM dans `tracker/` pour analyser ce qui marche
