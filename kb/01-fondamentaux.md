# 01 — Fondamentaux de la forgemagie

## Vocabulaire essentiel

| Terme | Définition |
|---|---|
| **Jet** | Valeur actuelle d'une stat sur l'item (ex : 250 vita) |
| **Jet max** | Valeur maximale possible pour cette stat sur cet item |
| **Jet min** | Valeur minimale possible (souvent 0 ou 1) |
| **Jet relatif** | Écart entre jet actuel et jet max (ex : 240/250 vita = -10 relatif) |
| **Poids** | "Coût caché" de chaque stat. Toutes les stats ont un coef de poids. La somme des poids ne peut pas dépasser le **poids max** de l'item. |
| **Poids max** | Limite supérieure de poids autorisée par l'item. C'est ce qui empêche de tout maxer en même temps. |
| **Surcharge** | Quand tu dépasses le poids max → l'item se "casse" sur d'autres stats (jets négatifs) |
| **Exo** | Statistique ajoutée *au-delà* du max théorique : +1 PA, +1 PM, +1 Portée. Très rare, très cher. |
| **FM blanche** | FM "safe" : on reste sous le poids max, on stabilise des stats existantes. Risque faible, gain faible. |
| **FM brisée** | FM sur item déjà bien jeté qu'on veut corriger. Risque modéré. |
| **FM exo** | Tentative d'ajout d'un exo (PA/PM/Po). Risque énorme, gain énorme. |
| **Ra / Pa / Pwa** | Les 3 tailles de rune. Ra = +1 jet, Pa ≈ ×3-5, Pwa ≈ ×9-15 selon la stat. |
| **Rune brisée** | Quand une rune utilisée échoue, elle est consommée sans effet. C'est la perte de base de la FM. |

## Principe de base

Un item Dofus a :
- Des **stats max** (le jet "parfait" affiché en vert)
- Un **poids total max** qu'on ne peut pas dépasser
- Des stats négatives possibles si on déborde

Quand tu **utilises une rune sur un item** :
1. Tu **ajoutes du poids** sur la stat ciblée (ex : Ra Vi = +1 vita → +0.2 poids)
2. Tu **consommes la rune** (avec une proba d'échec si conditions pas réunies)
3. Si tu dépasses le poids max → l'item **perd** sur d'autres stats (à choisir aléatoirement parmi les stats "exotiques", i.e. sagesse, prospection, dommages, etc.)

## Les 3 mouvements de base

### 1. Ajouter une stat
Tu utilises une rune de cette stat. Si la stat est déjà au max → impossible (rune échoue).
**Condition** : il doit rester du **poids disponible** sur l'item (poids actuel < poids max).

### 2. Retirer une stat
Tu utilises une rune sur une stat **autre** que celle que tu veux retirer, mais en mode "puits" : tu cliques sur la stat à retirer pour la diminuer (-1 ou plus).
**Mécanique** : la rune utilisée part en "puits", et la stat ciblée perd un jet. La rune est consommée.

### 3. Échanger
Quand tu n'as plus de poids dispo, tu **échanges** : tu fais baisser une stat (moins importante) pour pouvoir en monter une autre (plus importante). C'est le cœur de la FM.

## Les 3 stratégies de FM par niveau de risque

### FM blanche (débutant — sécurisé)
- **Objectif** : optimiser les jets sans tenter d'exo
- **Méthode** : on travaille sur un item déjà bien jeté, on rééquilibre
- **Risque** : faible (on perd quelques runes au pire)
- **Gain** : modéré (un item bien FM se vend 30-100% plus cher)

### FM brisée (intermédiaire)
- **Objectif** : récupérer un item raté (jets négatifs ou stats inutiles maxées)
- **Méthode** : on retire les stats parasites, on remet les bonnes
- **Risque** : modéré (item déjà cassé, peut se re-casser)
- **Gain** : élevé (acheter cassé = pas cher, revendre clean = cher)

### FM exo (avancé — high risk / high reward)
- **Objectif** : ajouter +1 PA, +1 PM ou +1 Portée
- **Méthode** : surcharger très fort l'item pour forcer un débordement favorable
- **Risque** : très élevé (proba d'exo très basse, item peut se détruire)
- **Gain** : énorme (PA exo sur cape Otomaï = +500k à +2M kamas selon l'item)

## Règles d'or pour ne pas perdre bêtement

1. **Ne FM jamais sans avoir calculé le poids cible.** Toujours vérifier que c'est mathématiquement possible.
2. **Achète les runes au bon prix.** Un Pa Vi à 2x son prix te ruine la marge.
3. **Backup le brut.** Avant de FM, screenshot l'item brut. Si tu fais une connerie, tu pourras refaire à partir d'un identique.
4. **Connais le marché de l'item final.** FM un item parfait qui ne se vend pas = 0 kamas.
5. **Spécialise-toi sur 3-5 items max au début.** La maîtrise vaut mieux que la dispersion.

---

**Suivant** : [02-runes-et-poids.md](02-runes-et-poids.md) — Le tableau des poids et comment l'utiliser
