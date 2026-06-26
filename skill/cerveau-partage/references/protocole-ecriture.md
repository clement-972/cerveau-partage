# Detailed writing protocol / Protocole d'ecriture detaille

Reference called by `SKILL.md` on a "MAJ cerveau". The brain is a Doc in the team's documentation tool (ClickUp, Notion, etc.), handled through its connector.

*(Version francaise plus bas.)*

## Steps

### 1. Collect
If "MAJ cerveau" comes alone, ask what to store. Otherwise restate the information in one or two sentences before filing.

### 2. Categorize
Read the routing table on the "Sommaire et conventions" page and choose the sub-page by the **nature** of the information:
- a legal obligation or constraint: `01 Reglementaire`
- an expected product behavior: `02 Specs fonctionnelles`
- an architecture or implementation choice: `03 Specs techniques`
- a reusable method or prompt: `04 Skills`
- a priority or milestone: `05 Roadmap`
- an unsettled decision: `06 En cours`

If torn between two sub-pages, prefer `06 En cours` when the item is still moving, otherwise ask the user.

### 3. De-duplicate
Before creating anything: read the target sub-page via the connector, compare the subject to existing titles and keywords, and if a note already covers it, offer "A note already exists on this. Shall I update it?" and wait for agreement. Only create a new note if none is close.

### 4. File (read-before-rewrite)
Many connectors **replace a page's entire content** on update (ClickUp; Notion edits surgically). So, in all cases:
1. Read the sub-page's current content.
2. Build the **full content** including the change (updating an existing note, or adding a new note using `modeles-fiches.md`).
3. Rewrite the page with that complete content. Never send an isolated fragment, or you overwrite the rest.

Update: fold the info into the existing note, refresh the date and keywords if needed, keep useful history.

### 5. Log
Read the "Journal" page, then rewrite it with **one new line at the top** of the table, under the header row:

```
| 2026-06-26 | Name | 01 Reglementaire | Added the 36-month retention rule. |
```

The date is today. The author comes from the remembered name (see SKILL.md). The sub-page column names the sub-page touched. The summary is one sentence.

### 6. Confirm
One sentence only, e.g. "Filed: note added in `01 Reglementaire` and logged." Nothing more.

## Full example

User: "MAJ cerveau: from now on, invoices must show the customer's intra-EU VAT number for sales within the European Union."

1. Clear, no need to re-ask.
2. Category: legal display obligation, so `01 Reglementaire`.
3. De-dup: read `01 Reglementaire`. A "Mentions obligatoires facture" note exists and overlaps. Offer to update it rather than create a new note.
4. After agreement: read the page, add the rule to the note's "EU notices" section, refresh the date, then rewrite the full page.
5. Log: read "Journal", rewrite it with a top line `| 2026-06-26 | Clement | 01 Reglementaire | Added intra-EU customer VAT number for EU sales. |`.
6. Confirm: "Filed: Mentions obligatoires facture updated (intra-EU VAT) and logged."

---

# Protocole d'ecriture detaille (Francais)

Reference appelee par `SKILL.md` lors d'un "MAJ cerveau". Le cerveau est un Doc dans l'outil de documentation de l'equipe (ClickUp, Notion, etc.), manipule via son connecteur.

## Etapes

1. **Recueillir.** Si "MAJ cerveau" arrive seul, demander quoi memoriser. Sinon, reformuler l'info en une ou deux phrases avant de ranger.
2. **Categoriser.** Via la table d'aiguillage de la page "Sommaire et conventions", choisir la sous-page selon la **nature** de l'info (contrainte legale, comportement produit, choix technique, methode reutilisable, priorite, decision non tranchee). En cas d'hesitation, privilegier `06 En cours` si l'info est mouvante, sinon demander.
3. **Anti-doublon.** Lire la sous-page cible, comparer le sujet aux titres et mots-cles. Si une fiche traite deja le sujet, proposer "Une fiche existe deja sur ce sujet. Je la mets a jour ?" et attendre l'accord. Ne creer une fiche que si aucune n'est proche.
4. **Ranger (lire-avant-reecrire).** Beaucoup de connecteurs remplacent tout le contenu d'une page a la mise a jour (ClickUp ; Notion edite finement). Donc toujours : lire la page, construire le contenu complet integrant la modification (mise a jour d'une fiche, ou nouvelle fiche au format de `modeles-fiches.md`), puis reecrire la page entiere. Jamais un fragment isole.
5. **Journaliser.** Lire la page "Journal", la reecrire avec une ligne en haut du tableau, sous l'en-tete : `| date | auteur | sous-page | resume en une phrase |`. L'auteur vient du nom memorise (voir SKILL.md).
6. **Confirmer.** Une seule phrase, nommant la sous-page touchee et l'action (cree ou mis a jour).

## Exemple complet

Utilisateur : "MAJ cerveau : a partir de maintenant, les factures doivent afficher le numero de TVA intracommunautaire du client pour les ventes dans l'Union europeenne."

1. Information claire, pas besoin de la redemander.
2. Categorie : obligation legale d'affichage, donc `01 Reglementaire`.
3. Anti-doublon : lire `01 Reglementaire`. Une fiche "Mentions obligatoires facture" existe et recoupe le sujet. Proposer sa mise a jour.
4. Apres accord : lire la page, ajouter la regle dans la section "Mentions UE", rafraichir la date, puis reecrire la page complete.
5. Journal : lire "Journal", reecrire avec en haut `| 2026-06-26 | Clement | 01 Reglementaire | Ajout TVA intracommunautaire client pour ventes UE. |`.
6. Confirmation : "C'est range : fiche Mentions obligatoires facture mise a jour (TVA intracommunautaire UE) et journalisee."
