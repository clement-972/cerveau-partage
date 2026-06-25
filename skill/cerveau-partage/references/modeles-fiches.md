# Modeles de fiches / Note templates

Gabarits a utiliser quand on cree une fiche. L'en-tete est commun a toutes les categories ; le corps s'adapte. / Templates to use when creating a note. The header is common to all categories; the body adapts.

## En-tete commun / Common header

```
# Titre clair de la fiche

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : mot1, mot2, mot3
```

- `Statut` : `stable` dans les dossiers definitifs, `en cours` dans `06_en_cours/`.
- `Derniere maj` : date du jour de la derniere ecriture.
- `Mots-cles` : 3 a 6 termes qui servent au reperage et a l'anti-doublon.

## 01_reglementaire

```
# Titre

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Regle
Ce qui est obligatoire ou interdit, en une a trois phrases.

## Source
Texte de loi, norme ou reference interne.

## Impact produit
Ce que cela impose concretement au produit.
```

## 02_specs_fonctionnelles

```
# Titre

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Besoin
Le besoin utilisateur, en une phrase.

## Parcours
Les etapes principales.

## Regles metier
Les contraintes et cas limites.
```

## 03_specs_techniques

```
# Titre

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Decision
Le choix technique retenu.

## Raison
Pourquoi ce choix.

## Consequences
Ce que cela implique pour la suite.
```

## 04_skills

```
# Titre

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Quand l'utiliser
Le declencheur ou le contexte d'usage.

## Procedure
Les etapes a suivre.

## Exemple
Une illustration concrete.
```

## 05_roadmap

```
# Titre

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Cap
L'objectif vise.

## Maintenant / Ensuite / Plus tard
Ce qui est fait maintenant, ce qui suit, ce qui viendra plus tard.
```

## 06_en_cours

```
# Titre

> Statut : en cours | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Question ouverte
Ce qui reste a trancher.

## Options envisagees
Les pistes et leurs compromis.

## A trancher
Ce qui declenchera la decision, et vers quel dossier deplacer la fiche une fois stabilisee.
```
