# Note templates / Modeles de fiches

Each note (fiche) is its own **sub-page** under its category. The note's **title is the page name**; the page **content** starts with a status line, then the category-specific sections below. The body field labels are kept in French (the team's convention) and can be translated.

*(Version francaise plus bas.)*

## Status line (first line of every note)

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : mot1, mot2, mot3
```

- `Statut`: `stable` in the settled categories, `en cours` in `06 En cours`.
- `Derniere maj`: date of the last write.
- `Mots-cles`: 3 to 6 terms used for retrieval and de-duplication.

Below are the body templates per category (page content goes after the status line; the page name carries the title).

## 01 Reglementaire

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Regle
Ce qui est obligatoire ou interdit, en une a trois phrases.

## Source
Texte de loi, norme ou reference interne.

## Impact produit
Ce que cela impose concretement au produit.
```

## 02 Specs fonctionnelles

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Besoin
Le besoin utilisateur, en une phrase.

## Parcours
Les etapes principales.

## Regles metier
Les contraintes et cas limites.
```

## 03 Specs techniques

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Decision
Le choix technique retenu.

## Raison
Pourquoi ce choix.

## Consequences
Ce que cela implique pour la suite.
```

## 04 Skills

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Quand l'utiliser
Le declencheur ou le contexte d'usage.

## Procedure
Les etapes a suivre.

## Exemple
Une illustration concrete.
```

## 05 Roadmap

```
> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Cap
L'objectif vise.

## Maintenant / Ensuite / Plus tard
Ce qui est fait maintenant, ce qui suit, ce qui viendra plus tard.
```

## 06 En cours

```
> Statut : en cours | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : ...

## Question ouverte
Ce qui reste a trancher.

## Options envisagees
Les pistes et leurs compromis.

## A trancher
Ce qui declenchera la decision, et vers quelle categorie deplacer la fiche une fois stabilisee.
```

---

# Modeles de fiches (Francais)

Chaque fiche est une **sous-page** de sa categorie. Le **titre de la fiche est le nom de la page** ; le **contenu** de la page commence par une ligne d'etat, suivie des sections propres a la categorie (gabarits ci-dessus).

- `Statut` : `stable` dans les categories definitives, `en cours` dans `06 En cours`.
- `Derniere maj` : date du jour de la derniere ecriture.
- `Mots-cles` : 3 a 6 termes qui servent au reperage et a l'anti-doublon.
- Le nom de la page porte le titre ; pas de ligne `# Titre` dans le contenu, et pas de regle de nom de fichier.
