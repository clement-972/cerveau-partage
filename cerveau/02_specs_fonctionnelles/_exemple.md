# Exemple : reinitialisation de mot de passe

> Statut : stable | Derniere maj : 2026-06-24 | Auteur : Cerveau Partage | Mots-cles : authentification, mot de passe, parcours, exemple

Fiche d'exemple. Elle montre le format attendu dans `02_specs_fonctionnelles/`. Remplacez son contenu ou supprimez-la.

## Besoin
Un utilisateur qui a oublie son mot de passe doit pouvoir le reinitialiser sans contacter le support.

## Parcours
1. L'utilisateur saisit son email.
2. Un lien valable 30 minutes est envoye.
3. Apres definition d'un nouveau mot de passe, toutes les sessions actives sont fermees.

## Regles metier
Le lien est a usage unique. Au dela de 5 demandes par heure, on temporise.

---

*Example note (EN): shows the expected format for the `02_specs_fonctionnelles/` folder (product behavior, user journeys, business rules). Replace or delete it.*
