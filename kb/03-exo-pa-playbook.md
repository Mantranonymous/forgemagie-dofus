# 03 — Exo PA : playbook complet

> ⚠️ **Avant d'attaquer** : un exo PA, c'est un pari haut-risque/haute-récompense. Ne tente JAMAIS un exo sans avoir le budget pour potentiellement TOUT perdre, et sans avoir validé le marché de revente sur Tylezia.

## Comment fonctionne un exo PA (mécanique)

L'exo PA est un **événement aléatoire** qui peut se déclencher lors d'une FM quand l'item est en **état de surcharge** (poids actuel > poids max).

### Principe en 3 phases

```
1. MAXER l'item        →  Toutes les stats principales au jet max
2. SURCHARGER          →  Ajouter encore du poids au-delà du poids max
3. SPAMMER les runes   →  Chaque rune en surcharge = 1 tentative d'exo
```

À chaque rune utilisée en condition de surcharge, le jeu **roule un dé** :
- Sur "succès" → +1 PA permanent sur l'item 🎉
- Sur "échec" → la rune part en surcharge :
  - Soit elle augmente la stat ciblée + dégrade une autre stat (jets négatifs sur sagesse/dommages typiquement)
  - Soit elle ne fait rien (rune brisée pure)

### Probabilité (estimations communauté)

- Proba par tentative : **~1-3% en conditions optimales** (souvent moins en Dofus 3)
- Espérance : il faut compter **30-100 tentatives en moyenne** pour réussir
- Variance énorme : certains exo en 5 runes, d'autres en 500+

### Ce qui INFLUE sur la proba (théories communauté, non garanties)

| Facteur | Effet probable |
|---|---|
| **Niveau de surcharge** | Plus tu dépasses le poids max, plus la proba monte (mais avec un cap) |
| **Type de rune** | Pwa > Pa > Ra (en proba par rune, mais Pwa = plus de dégâts si échec) |
| **Item sur-jeté à la base** | Peut influencer le seuil de surcharge |
| **Stat "déclencheuse"** | Stat lourde (sagesse, dommages) = surcharge plus rapide avec moins de runes |

> ⚠️ Ces facteurs sont **empiriques**. Ankama n'a jamais publié les formules. Sur Dofus 3 / Unity (Tylezia), certaines mécaniques ont changé — à valider via tests.

## Plan d'action concret pour le Voile d'encre

### Étape 0 — Prérequis (avant même de commencer)

- [ ] **Budget validé** : minimum 5M kamas (pessimiste : 30M+). Si t'as pas ça en surplus, ne tente pas.
- [ ] **Marché vérifié** : check HDV Tylezia pour un *Voile d'encre PA exo* et confirme qu'il se vend > 30M kamas. Sinon → pas rentable.
- [ ] **Coefs poids calibrés** : la mécanique de surcharge dépend du poids max. Sans coefs Dofus 3 validés, tu navigues à vue. **À faire avant la première tentative.**
- [ ] **Backup mental** : si tu perds 20M, accepte-le. Ne jamais "tilter" en remettant des kamas pour "se refaire".

### Étape 1 — Acquérir un Voile d'encre parfait

Le base de départ doit être un Voile d'encre **au jet max sur toutes les stats** (vita 350, fo 70, in 70, sa 40, %CC 3, dom 10, rés 10/10/10).

- **Option A** : acheter parfait au HDV (cher mais immédiat — sans doute 500k-2M kamas selon offre)
- **Option B** : acheter brut + FM blanche pour maxer (économique mais demande la maîtrise FM blanche)

> ⚠️ Le malus de portée (-1) est **gravé dans l'item**, on ne peut pas le supprimer en FM normale. Donc à accepter.

### Étape 2 — Identifier la stat "déclencheuse"

C'est la stat qu'on va spammer en surcharge. Critères :
- **Coef poids élevé** = surcharge rapide avec peu de runes
- **Runes accessibles HDV** = pas trop chères, dispo en volume
- **Pas critique pour la valeur finale** = si elle se dégrade un peu pendant le process, l'item reste vendable

Candidates pour Voile d'encre :
| Stat | Coef | Pourquoi |
|---|---:|---|
| **Sagesse** | 3 | Stat secondaire, coef élevé, runes Pa Sa relativement courantes |
| **Dommages** | 20 | Coef énorme = très peu de runes pour surcharger, mais c'est aussi la stat la plus précieuse de la cape → à éviter comme déclencheuse |
| Force/Intel | 1 | Coef faible = il faudrait BEAUCOUP de runes pour surcharger |

**Recommandation** : spammer en **Pa Sagesse** (sa coef de 3 fait grimper le poids vite, et la sagesse en surplus reste cherchée).

### Étape 3 — Préparer le stock de runes

Pour un cycle de tentatives "moyen" (50 runes) :
- ~30-50 Pa Sa (déclencheuses)
- ~5-10 Pwa Sa (gros bonds quand on est loin du seuil)
- ~10-20 Ra de réparation (Ra Vi, Ra Fo, Ra In, Ra Do) pour récupérer les jets perdus en cours de route
- Budget de réapprovisionnement si le HDV se vide

> **Astuce** : achète tout AVANT de commencer. Pendant le grind tu seras en tilt si tu dois faire des aller-retours HDV.

### Étape 4 — Le grind

```
Pour chaque tentative :
  1. Vérifier le poids actuel vs poids max
  2. Si poids ≥ poids_max → utiliser une rune (Pa Sa ou Pwa Sa)
  3. Si réussi → on s'arrête, on tcheke les jets
  4. Si échoué → noter ce qui a baissé (sa, dom, vi, autre)
  5. Toutes les 10-20 tentatives → réparer les stats les plus dégradées
  6. Continuer jusqu'à exo OU budget épuisé OU item trop brûlé
```

### Étape 5 — Si exo réussi 🎉

- **Avant de revendre** : vérifier les jets de toutes les stats. Si certaines sont dégradées (sagesse à 25/40, dommages à 7/10) → FM blanche pour les remonter.
- **Mise en vente** : viser le prix médian du HDV, pas le plus cher (vente plus rapide = ROI plus vite).
- **Document** : log ce qui a marché dans `tracker/` pour reproduire.

### Étape 6 — Si trop brûlé

- Si la cape est devenue invendable (sagesse < 20, dommages < 5) :
  - Soit la rebrasser en FM blanche pour la revendre cassée
  - Soit la garder en stock pour un futur essai après calibration

## Estimation économique (à valider sur Tylezia)

| Poste | Valeur (approx.) |
|---|---|
| Voile d'encre parfait | 500k - 2M kamas |
| Stock runes initial (50 Pa Sa + 10 Pwa Sa + Ra réparation) | 5M - 15M kamas |
| Espérance de cycles avant exo | 1 à 3 cycles (très variable) |
| **Coût total moyen** | **10M - 40M kamas** |
| Voile d'encre PA exo (revente) | **30M - 150M kamas** ? |
| **Marge espérée** | Positive **si** marché actif |

> ❗ Avant de te lancer, **vérifie ces chiffres sur le HDV Tylezia**. L'éco mono-compte est différente des serveurs classiques.

## Pourquoi pas le Voile d'encre en PREMIER exo PA ?

Quand on apprend, on perd souvent. Apprends sur un item **moins coûteux** :

| Critère | Voile d'encre | Item idéal pour 1er exo |
|---|---|---|
| Nombre de stats à risque | 10 (énorme) | 3-5 |
| Prix d'achat brut | 500k-2M | 50k-200k |
| Coût d'un cycle complet | 10-40M | 1-5M |
| Difficulté de gestion | Élevée | Modérée |

**Candidats plus accessibles pour t'entraîner** :
- Anneaux niveau ~100-150 (peu de stats, coût bas)
- Capes intermédiaires niveau 100-150 (Cape du Bouftou Royal, Cape Otomaï bas-niveau)
- Items dont le PA exo a un marché actif sur Tylezia

> **Recommandation** : fais 2-3 cycles d'exo PA sur item testeur d'abord. Apprends la sensation du grind, identifie les pièges. **Puis** attaque le Voile d'encre avec confiance.

## Action immédiate

1. **Calibre les coefs Dofus 3** en mesurant le poids max d'un Voile d'encre in-game (cf. demande dans le chat principal)
2. **Vérifie le marché HDV Tylezia** : prix d'un Voile d'encre brut, parfait, et PA exo
3. **Choisis ton item testeur** : si tu acceptes le conseil de ne pas commencer par le Voile d'encre, dis-moi un item plus simple et je l'importe via `import_item.py`

---

**Suivant** : `kb/04-lecture-item.md` (à venir) — Comment lire un item en 2 secondes et estimer sa valeur
