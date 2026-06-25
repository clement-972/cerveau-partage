# Exemple : convention de nommage des API

> Statut : stable | Derniere maj : 2026-06-24 | Auteur : Cerveau Partage | Mots-cles : api, rest, convention, exemple

Fiche d'exemple. Elle montre le format attendu dans `03_specs_techniques/`. Remplacez son contenu ou supprimez-la.

## Decision
Les routes REST sont au pluriel et en minuscules (`/invoices`, `/contacts`). Les identifiants sont des UUID v4.

## Raison
Coherence avec l'existant et lisibilite des logs.

## Consequences
Toute nouvelle ressource suit cette convention. Les anciennes routes au singulier sont maintenues en redirection jusqu'a la prochaine version majeure.

---

*Example note (EN): shows the expected format for the `03_specs_techniques/` folder (architecture, API, data model, technical choices). Replace or delete it.*
