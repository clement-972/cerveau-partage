---
name: cerveau-partage
description: >-
  Shared product-team memory living in a structured Doc inside the team's
  documentation tool (ClickUp, Notion, etc.), reached through its connector. Use
  it to consult team knowledge when a request overlaps it (regulatory,
  functional specs, technical specs, skills, roadmap, ongoing topics), and when
  the user writes the keyword "MAJ cerveau" to file a stabilized piece of
  information. Memoire produit partagee d'equipe, posee sur un Doc structure dans
  l'outil de documentation de l'equipe et accessible via son connecteur ;
  ecriture uniquement sur le mot-cle "MAJ cerveau".
---

# Cerveau Partage

A light team-memory layer on top of a structured Doc, inside the documentation tool the team already uses (ClickUp, Notion, or any tool with a connector that can read and write pages). This Skill only adds reading and writing discipline; it stores nothing itself.

The project name ("Cerveau Partage"), the write keyword ("MAJ cerveau") and the category names are kept in French on purpose: they are the team's working convention. A team may change them to suit its own language.

*(Version francaise plus bas / French section below.)*

## Where the brain is

The brain is a Doc named "Cerveau". It has a "Sommaire et conventions" page holding the routing table, one sub-page per domain (01 Reglementaire ... 06 En cours), and a "Journal" page. Everything is handled through the documentation tool's connector (reading and writing pages).

To locate it, in order:

1. **Configured reference.** If a reference is filled in here, use it directly.
   - **Brain reference: _(team to fill in: Doc URL or ID, e.g. a ClickUp Doc or a Notion page)_**
2. **Search by convention.** Otherwise, search via the connector for a Doc or page named "Cerveau" in the team's documentation space.
3. **Ask once.** Otherwise, ask the user for the brain's URL, then remember it so you do not ask again.

If no documentation connector is available, this Skill does nothing.

## Triggers

- **When a request overlaps team knowledge** (regulatory, specs, conventions, roadmap, ongoing topics): apply the reading protocol.
- **When the user writes "MAJ cerveau"** (optionally followed by the information): apply the writing protocol. This is the only write trigger. Never write to the brain without it.

## Reading protocol

1. Locate the brain and read its "Sommaire et conventions" page: it is short and holds the routing table.
2. Identify the request's topic.
3. Using the routing table, open **only** the relevant sub-page(s). Do not load the whole brain.
4. If the topic is vague, list note titles from candidate sub-pages before reading in detail.
5. Treat this knowledge as given: do not re-ask the user what the brain already records.

## Writing protocol (on "MAJ cerveau")

Full detail and example: see `references/protocole-ecriture.md`. In short:

1. **Collect** the information to store (ask if "MAJ cerveau" comes alone).
2. **Categorize** via the routing table on the "Sommaire et conventions" page (the right sub-page by the nature of the info).
3. **De-duplicate**: read the target sub-page and check whether the info already exists (titles and keywords). If a close note exists, offer to update it rather than create a new one, and wait for agreement.
4. **File**: fold it cleanly into the chosen note, or add a new note using `references/modeles-fiches.md`.
5. **Log**: prepend one line to the table on the "Journal" page (today's date, author, sub-page, one-sentence summary).
6. **Confirm** in a single sentence, naming the sub-page touched and the action (created or updated).

### Write-safety rule (important)

Some connectors **replace a page's entire content** on update (ClickUp does; Notion edits surgically). So, whatever the tool: **read the page first, then send back its full content plus the addition**, never an isolated fragment, or you may overwrite the rest of the page.

## Author identity

The journal records who made each update. On write: if the user's name is already known (remembered from a previous session, or exposed by the connector), use it silently; otherwise ask once "What name should I log your updates under?", then remember it.

## Safety rules

No write without "MAJ cerveau". Always read a page before rewriting it (see the write-safety rule). Never mass-delete or mass-rewrite an existing note without explicit agreement. On a duplicate, offer an update instead of duplicating. Always log a write, and always confirm in one sentence.

---

# Cerveau Partage (Francais)

Couche legere de memoire d'equipe posee sur un Doc structure, dans l'outil de documentation que l'equipe utilise deja (ClickUp, Notion, ou tout outil muni d'un connecteur permettant de lire et ecrire des pages). Ce Skill n'apporte que la discipline de lecture et d'ecriture : il ne stocke rien lui-meme.

## Ou se trouve le cerveau

Le cerveau est un Doc intitule "Cerveau". Il contient une page "Sommaire et conventions" qui porte la table d'aiguillage, une sous-page par domaine (01 Reglementaire ... 06 En cours), et une page "Journal". Tout se manipule via le connecteur de l'outil de documentation.

Pour le localiser, dans l'ordre :

1. **Reference configuree.** Si une reference est renseignee dans la section anglaise ci-dessus ("Brain reference"), l'utiliser directement.
2. **Recherche par convention.** Sinon, chercher via le connecteur un Doc ou une page nomme "Cerveau" dans l'espace de documentation de l'equipe.
3. **Demander une fois.** Sinon, demander a l'utilisateur l'URL du cerveau, puis la memoriser pour ne plus la redemander.

Si aucun connecteur de documentation n'est disponible, ce Skill ne fait rien.

## Declencheurs

- **Quand une demande recoupe le savoir d'equipe** (reglementaire, specs, conventions, roadmap, sujets en cours) : appliquer le protocole de lecture.
- **Quand l'utilisateur ecrit "MAJ cerveau"** : appliquer le protocole d'ecriture. C'est le seul declencheur d'ecriture. Ne jamais ecrire dans le cerveau sans ce mot-cle.

## Protocole de lecture

1. Localiser le cerveau et lire sa page "Sommaire et conventions" : courte, elle contient la table d'aiguillage.
2. Identifier le sujet de la demande.
3. A l'aide de la table d'aiguillage, ouvrir **uniquement** la ou les sous-pages pertinentes. Ne pas charger tout le cerveau.
4. Si le sujet est vague, lister d'abord les titres des fiches des sous-pages candidates.
5. Utiliser ce savoir comme acquis : ne pas redemander ce qui est deja ecrit dans le cerveau.

## Protocole d'ecriture (sur "MAJ cerveau")

Detail complet et exemple : voir `references/protocole-ecriture.md`. En resume :

1. **Recueillir** l'information (la demander si "MAJ cerveau" arrive seul).
2. **Categoriser** via la table d'aiguillage (la bonne sous-page selon la nature de l'info).
3. **Anti-doublon** : lire la sous-page cible et chercher si l'info existe deja. Si une fiche proche existe, proposer de la mettre a jour plutot que d'en creer une nouvelle, et attendre l'accord.
4. **Ranger** : integrer dans la fiche choisie, ou ajouter une nouvelle fiche au format de `references/modeles-fiches.md`.
5. **Journaliser** : ajouter une ligne en haut du tableau de la page "Journal" (date du jour, auteur, sous-page, resume en une phrase).
6. **Confirmer** en une seule phrase, en indiquant la sous-page touchee et l'action (cree ou mis a jour).

### Regle de securite d'ecriture (importante)

Certains connecteurs **remplacent tout le contenu** d'une page lors d'une mise a jour (ClickUp ; Notion edite de facon ciblee). Donc, quel que soit l'outil : **lire d'abord la page, puis renvoyer son contenu complet augmente de l'ajout**, jamais un fragment isole, sous peine d'ecraser le reste.

## Identite de l'auteur

Le journal note qui ecrit. Si le nom est deja connu (memorise, ou expose par le connecteur), l'utiliser sans poser de question ; sinon, demander une fois "Sous quel nom journaliser tes mises a jour ?", puis le memoriser.

## Regles de prudence

- Aucune ecriture sans "MAJ cerveau".
- Toujours lire une page avant de la reecrire (voir la regle de securite d'ecriture).
- Ne pas supprimer ni reecrire en masse une fiche sans accord explicite.
- En cas de doublon, proposer la mise a jour, ne pas dupliquer.
- Toujours journaliser une ecriture, et toujours confirmer en une phrase.
