# Protocole d'ecriture detaille / Detailed writing protocol

Reference appelee par `SKILL.md` lors d'un "MAJ cerveau". Elle precise chaque etape et donne un exemple complet.

*(English version below.)*

## Etapes

### 1. Recueillir l'information
Si "MAJ cerveau" arrive seul, demander quoi memoriser. Si l'information suit le mot-cle, la reformuler en une ou deux phrases et la confirmer mentalement avant de ranger.

### 2. Categoriser
Ouvrir la table d'aiguillage de `cerveau/00_CONTEXTE.md` et choisir le dossier selon la **nature** de l'information :
- une obligation ou une contrainte legale : `01_reglementaire/`
- un comportement attendu du produit : `02_specs_fonctionnelles/`
- un choix d'architecture ou d'implementation : `03_specs_techniques/`
- une methode ou un prompt reutilisable : `04_skills/`
- une priorite ou un jalon : `05_roadmap/`
- une decision non encore tranchee : `06_en_cours/`

En cas d'hesitation entre deux dossiers, privilegier `06_en_cours/` si l'info est mouvante, sinon demander a l'utilisateur.

### 3. Anti-doublon
Avant de creer quoi que ce soit :
1. Lister les fiches du dossier cible.
2. Comparer le sujet aux titres et aux mots-cles des fiches existantes.
3. Si une fiche traite deja le meme sujet, proposer : "Une fiche existe deja sur ce sujet (`nom.md`). Je la mets a jour ?" et attendre l'accord.
4. Ne creer une nouvelle fiche que si aucune fiche proche n'existe.

### 4. Ranger
- Mise a jour : integrer l'info dans la fiche existante, mettre a jour la date et, si besoin, les mots-cles. Ne pas effacer l'historique utile.
- Creation : nouvelle fiche au format de `modeles-fiches.md`. Nom de fichier en minuscules, sans accents, mots separes par des tirets (`nom-clair.md`).

### 5. Journaliser
Ajouter **une ligne en haut** du tableau de `cerveau/00_JOURNAL.md`, sous la ligne d'en-tete :

```
| 2026-06-24 | Prenom | 01_reglementaire/conservation-donnees.md | Ajout de la regle de conservation 36 mois. |
```

La date est celle du jour. L'auteur vient du fichier local (voir SKILL.md). Le chemin est relatif a `cerveau/`. Le resume tient en une phrase.

### 6. Rafraichir le cockpit (si present)
Si le cerveau contient `_cockpit/generate.py`, regenerer la visualisation :

```
python3 /chemin/vers/cerveau/_cockpit/generate.py
```

Le script lit les fichiers Markdown et reecrit `cerveau/cockpit.html` sans jamais modifier les fiches. C'est une commodite : s'il n'y a pas de dossier `_cockpit/`, ou si `python3` n'est pas disponible, ignorer cette etape sans bloquer.

### 7. Confirmer
Une seule phrase, par exemple : "C'est range : fiche `01_reglementaire/conservation-donnees.md` mise a jour, journalisee et cockpit rafraichi." Ne pas detailler davantage.

## Exemple complet

Utilisateur : "MAJ cerveau : a partir de maintenant, les factures doivent afficher le numero de TVA intracommunautaire du client pour les ventes dans l'Union europeenne."

1. Information claire, pas besoin de la redemander.
2. Categorie : obligation legale d'affichage, donc `01_reglementaire/`.
3. Anti-doublon : le dossier contient `mentions-obligatoires-facture.md`. Le sujet recoupe cette fiche. Proposer la mise a jour de cette fiche plutot qu'une nouvelle.
4. Apres accord, ajouter la regle dans la section "Mentions UE" de la fiche, et mettre la date du jour.
5. Journal : `| 2026-06-24 | Clement | 01_reglementaire/mentions-obligatoires-facture.md | Ajout TVA intracommunautaire client pour ventes UE. |`
6. Cockpit : relancer `python3 cerveau/_cockpit/generate.py` pour rafraichir `cockpit.html`.
7. Confirmation : "C'est range : `mentions-obligatoires-facture.md` mise a jour (TVA intracommunautaire UE), journalisee et cockpit rafraichi."

---

# Detailed writing protocol (English)

Reference called by `SKILL.md` on a "MAJ cerveau". It details each step and gives a full example.

## Steps

1. **Collect.** If "MAJ cerveau" comes alone, ask what to store. Otherwise restate the information in one or two sentences before filing.
2. **Categorize.** Use the routing table in `cerveau/00_CONTEXTE.md`, choosing the folder by the **nature** of the information (legal constraint, product behavior, technical choice, reusable method, priority, unsettled decision). If torn between two folders, prefer `06_en_cours/` when the item is still moving, otherwise ask the user.
3. **De-duplicate.** List the notes in the target folder, compare the subject to existing titles and keywords. If a note already covers it, offer "A note already exists on this (`name.md`). Shall I update it?" and wait for agreement. Only create a new note if none is close.
4. **File.** Update: fold the info into the existing note, refresh the date and keywords, keep useful history. Create: a new note using `modeles-fiches.md`, lowercase filename, no accents, hyphen-separated.
5. **Log.** Prepend **one line** to the table in `cerveau/00_JOURNAL.md`, just under the header row: `| date | author | path-relative-to-cerveau | one-sentence summary |`. The author comes from the local file (see SKILL.md).
6. **Refresh the cockpit (if present).** If the brain contains `_cockpit/generate.py`, regenerate the view with `python3 /path/to/cerveau/_cockpit/generate.py`. It reads the Markdown and rewrites `cerveau/cockpit.html` without modifying notes; skip without blocking if there is no `_cockpit/` folder or python3 is unavailable.
7. **Confirm.** One sentence only, naming the file touched and whether it was created or updated.

## Full example

User: "MAJ cerveau: from now on, invoices must show the customer's intra-EU VAT number for sales within the European Union."

1. Clear, no need to re-ask.
2. Category: legal display obligation, so `01_reglementaire/`.
3. De-dup: the folder has `mentions-obligatoires-facture.md`, which overlaps. Offer to update it rather than create a new note.
4. After agreement, add the rule to the note's "EU notices" section, refresh the date.
5. Log: `| 2026-06-24 | Clement | 01_reglementaire/mentions-obligatoires-facture.md | Added intra-EU customer VAT number for EU sales. |`
6. Cockpit: run `python3 cerveau/_cockpit/generate.py` to refresh `cockpit.html`.
7. Confirm: "Filed: `mentions-obligatoires-facture.md` updated (intra-EU VAT), logged and cockpit refreshed."
