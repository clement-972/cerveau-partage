# Detailed writing protocol / Protocole d'ecriture detaille

Reference called by `SKILL.md` on a "MAJ cerveau". The brain is a Doc in the team's documentation tool (ClickUp, Notion, etc.), handled through its connector. Each note (fiche) is its own sub-page under its category, so the page-title list stays a cheap, self-growing index.

*(Version francaise plus bas.)*

## Steps

### 1. Collect
If "MAJ cerveau" comes alone, ask what to store. Otherwise restate the information in one or two sentences before filing.

### 2. Categorize
Read the routing table on the "Sommaire et conventions" page and choose the category by the **nature** of the information:
- a legal obligation or constraint: `01 Reglementaire`
- an expected product behavior: `02 Specs fonctionnelles`
- an architecture or implementation choice: `03 Specs techniques`
- a reusable method or prompt: `04 Skills`
- a priority or milestone: `05 Roadmap`
- an unsettled decision: `06 En cours`

If torn between two, prefer `06 En cours` when the item is still moving, otherwise ask the user.

### 3. De-duplicate (cheap)
List the note titles under the target category (page names only, no content). Compare the subject to those titles. If one looks close, fetch only that note and check. If it covers the subject, offer "A note already exists on this. Shall I update it?" and wait for agreement. Only create a new note if none is close. Listing titles keeps this cheap even with hundreds of notes.

### 4. File (one note = one sub-page)
Each note is its own sub-page under its category.
- **Update** an existing note: read its page first, build the full content with the change, then rewrite the page (read-before-rewrite, because some connectors replace the whole page). Refresh the date and keywords; keep useful history.
- **Create** a new note: add a new sub-page under the category. The note's title becomes the page name; the page content follows `modeles-fiches.md` (status line, then the category sections).

### 5. Log
Read the "Journal" page, then rewrite it with **one new line at the top** of the table, under the header row:

```
| 2026-06-26 | Name | 01 Reglementaire | Added the 36-month retention rule. |
```

The date is today. The author comes from the remembered name (see SKILL.md). The category column names the category. The summary is one sentence.

### 6. Confirm
One sentence only, e.g. "Filed: new note 'Data retention' created under `01 Reglementaire` and logged." Nothing more.

## Full example

User: "MAJ cerveau: from now on, invoices must show the customer's intra-EU VAT number for sales within the European Union."

1. Clear, no need to re-ask.
2. Category: legal display obligation, so `01 Reglementaire`.
3. De-dup: list the note titles under `01 Reglementaire`. A note "Mentions obligatoires facture" exists and looks close; fetch it. It overlaps. Offer to update it.
4. After agreement: read that note's page, add the rule to its "EU notices" section, refresh the date, then rewrite the full page.
5. Log: read "Journal", rewrite it with a top line `| 2026-06-26 | Clement | 01 Reglementaire | Added intra-EU customer VAT number for EU sales. |`.
6. Confirm: "Filed: Mentions obligatoires facture updated (intra-EU VAT) and logged."

---

# Protocole d'ecriture detaille (Francais)

Reference appelee par `SKILL.md` lors d'un "MAJ cerveau". Le cerveau est un Doc dans l'outil de documentation de l'equipe (ClickUp, Notion, etc.), manipule via son connecteur. Chaque fiche est une sous-page de sa categorie, donc la liste des titres reste un index peu couteux qui grandit tout seul.

## Etapes

1. **Recueillir.** Si "MAJ cerveau" arrive seul, demander quoi memoriser. Sinon, reformuler l'info en une ou deux phrases avant de ranger.
2. **Categoriser.** Via la table d'aiguillage de la page "Sommaire et conventions", choisir la categorie selon la **nature** de l'info (contrainte legale, comportement produit, choix technique, methode reutilisable, priorite, decision non tranchee). En cas d'hesitation, privilegier `06 En cours` si l'info est mouvante, sinon demander.
3. **Anti-doublon (peu couteux).** Lister les titres des fiches de la categorie cible (les noms seulement, sans le contenu). Comparer le sujet a ces titres. Si l'un semble proche, charger seulement cette fiche pour verifier. Si elle traite le sujet, proposer "Une fiche existe deja sur ce sujet. Je la mets a jour ?" et attendre l'accord. Ne creer une fiche que si aucune n'est proche. Lister les titres reste peu couteux meme avec des centaines de fiches.
4. **Ranger (une fiche = une sous-page).** Chaque fiche est une sous-page de sa categorie.
   - **Mettre a jour** une fiche : lire d'abord sa page, construire le contenu complet integrant la modification, puis reecrire la page (lire-avant-reecrire, car certains connecteurs remplacent toute la page). Rafraichir la date et les mots-cles ; conserver l'historique utile.
   - **Creer** une fiche : ajouter une nouvelle sous-page sous la categorie. Le titre de la fiche devient le nom de la page ; le contenu suit `modeles-fiches.md` (ligne d'etat, puis les sections de la categorie).
5. **Journaliser.** Lire la page "Journal", la reecrire avec une ligne en haut du tableau, sous l'en-tete : `| date | auteur | categorie | resume en une phrase |`. L'auteur vient du nom memorise (voir SKILL.md).
6. **Confirmer.** Une seule phrase, nommant la fiche touchee et l'action (cree ou mis a jour).

## Exemple complet

Utilisateur : "MAJ cerveau : a partir de maintenant, les factures doivent afficher le numero de TVA intracommunautaire du client pour les ventes dans l'Union europeenne."

1. Information claire, pas besoin de la redemander.
2. Categorie : obligation legale d'affichage, donc `01 Reglementaire`.
3. Anti-doublon : lister les titres des fiches de `01 Reglementaire`. Une fiche "Mentions obligatoires facture" semble proche ; la charger. Elle recoupe le sujet. Proposer sa mise a jour.
4. Apres accord : lire la page de cette fiche, ajouter la regle dans sa section "Mentions UE", rafraichir la date, puis reecrire la page complete.
5. Journal : lire "Journal", reecrire avec en haut `| 2026-06-26 | Clement | 01 Reglementaire | Ajout TVA intracommunautaire client pour ventes UE. |`.
6. Confirmation : "C'est range : fiche Mentions obligatoires facture mise a jour (TVA intracommunautaire UE) et journalisee."
