# 02 — Runes et poids : le tableau de référence

Tout en FM revient à un calcul de poids. **Maîtriser ce tableau = 80% du game.**

## Coefficient de poids par stat

> ⚠️ Valeurs consensuelles Dofus 2.x/Unity. À valider contre une source à jour pour Tylezia (Inflexible.fr, wiki officiel, JoL).

| Stat | Coef poids | Interprétation |
|---|---:|---|
| **Vitalité** | 0.2 | 1 vita = 0.2 poids. Très léger → on peut en monter beaucoup. |
| **Initiative** | 0.1 | 1 init = 0.1 poids. La plus légère. |
| **Pods** | ~0.0625 | Quasi gratuite en poids. |
| **Force / Intel / Chance / Agi** | 1 | 1 stat élémentaire = 1 poids. Stat de référence. |
| **% Critique** | 1 | 1% crit = 1 poids. |
| **Sagesse** | 3 | 1 sagesse = 3 poids. Lourde. |
| **Prospection** | 3 | 1 prospec = 3 poids. |
| **Tacle / Esquive PA-PM** | ~4 | À valider. |
| **% Résistance neutre** | ~2 | Léger comparé aux autres rés. |
| **% Résistance élémentaire** | 6 | 1% rés élem = 6 poids. Lourd. |
| **Rés fixe élémentaire** | 6 | Idem. |
| **Dommages** | 20 | 1 dommage = 20 poids. **Très lourd.** |
| **Soins** | 20 | 1 soin = 20 poids. |
| **Portée (Po)** | 51 | 1 Po = 51 poids. Quasi-exo en soi. |
| **PM** | 90 | 1 PM = 90 poids. |
| **PA** | 100 | 1 PA = 100 poids. Le saint graal. |

## Comment se lit le poids d'un item

Chaque item a un **poids max** caché. Tu peux le calculer :

```
poids_max_item = somme(stat_max_i × coef_i) pour toutes les stats de l'item
```

**Exemple — Cape Otomaï (chiffres illustratifs)** :
- 80 vita (max) × 0.2 = 16
- 50 sagesse (max) × 3 = 150
- 40 force (max) × 1 = 40
- 50 intel (max) × 1 = 50
- 50 chance (max) × 1 = 50
- 50 agi (max) × 1 = 50
- 1 PA (max) × 100 = 100

**Poids max ≈ 456**

Si l'item actuel a :
- 78 vita × 0.2 = 15.6
- 48 sagesse × 3 = 144
- ...

Tu calcules le **poids actuel**. Le **poids disponible** = poids_max - poids_actuel.

## Les runes : taille et conversion

### Ra (rune normale)
- Donne **+1 jet** sur la stat ciblée
- Poids consommé = coef de la stat (Ra Vi = 0.2, Ra Fo = 1, Ra Sa = 3…)
- Le **carburant fin** : sert à terminer les jets ou ajuster au plus juste

### Pa (rune puissante)
- Donne **+plusieurs jets** d'un coup (en moyenne ×3 à ×5 selon la stat)
- Plus économique en runes que les Ra à grande échelle
- **Risque** : peut surcharger si on n'a pas calculé

### Pwa (rune surpuissante)
- Donne **+beaucoup de jets** (×9 à ×15 selon la stat)
- À réserver aux gros bonds (passer de 0 à 40 vita d'un coup)
- **Très inflammable** côté poids : à manier avec précision

### Règle de conversion approximative
- 1 Pwa ≈ 3 Pa ≈ 9 Ra (en termes de jet donné)
- **Mais** : le rapport prix HDV n'est pas linéaire ! Souvent les Pa et Pwa coûtent moins que leur équivalent en Ra (économie d'échelle). À vérifier dans `data/prices-tylezia.json`.

## La règle d'or du poids

**Tu ne peux pas dépasser le poids max sans pénalité.** Si tu dépasses :
- Le jeu te **retire automatiquement du jet** sur d'autres stats
- Stats les plus "à risque" : sagesse, prospection, dommages (les stats lourdes que tu n'as pas verrouillées)
- En cas de surcharge volontaire pour tenter un exo → tu peux perdre 5-20 sagesse / 5-10 dommages d'un coup

## Cas particulier : la tentative d'exo

Pour ajouter un PA exo (+1 PA au-delà du max théorique), on doit **surcharger très fort** l'item. La proba d'exo dépend de plein de facteurs (à creuser dans 03-strategies-fm.md), mais le principe :

- **Sur-poids requis** : il faut avoir un poids actuel TRÈS au-dessus du poids max
- **Méthode classique** : maxer 6/7 stats principales, puis spammer Pa/Pwa sur une stat secondaire jusqu'à exo
- **Coût moyen** : 10-50 Pwa par tentative, avec proba d'exo souvent <5%
- **Gain si réussi** : un item exo PA se vend généralement **5x à 20x** le prix d'un item parfait non-exo

## Action concrète : à faire maintenant

1. Ouvrir l'outil `tools/calc-poids/index.html` (à venir)
2. Tester avec 1-2 items que tu possèdes pour vérifier les coefs
3. Si tu trouves une valeur fausse → corriger dans `data/runes.json`

---

**Suivant** : `03-strategies-fm.md` (à venir) — Les vraies stratégies rentables par type d'item
