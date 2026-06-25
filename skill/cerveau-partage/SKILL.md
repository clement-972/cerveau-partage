---
name: cerveau-partage
description: >-
  Memoire partagee d'equipe produit, posee sur des fichiers Markdown dans un
  dossier "cerveau/". A utiliser quand une session demarre sur un projet qui
  contient un dossier cerveau/ (lecture ciblee du savoir d'equipe au demarrage),
  et quand l'utilisateur ecrit le mot-cle "MAJ cerveau" pour ranger une
  information stabilisee (reglementaire, specs fonctionnelles, specs techniques,
  skills, roadmap, sujets en cours). Shared product-team memory over Markdown
  files in a "cerveau/" folder: read relevant team knowledge at session start,
  and write only when the user says "MAJ cerveau".
---

# Cerveau Partage

Couche legere de memoire d'equipe au dessus d'un dossier de fichiers Markdown. Tout le savoir vit dans un dossier `cerveau/`. Ce Skill n'apporte que la discipline de lecture et d'ecriture : il ne stocke rien lui-meme, il ne remplace pas les fichiers.

*(English section below / Section anglaise plus bas.)*

## Ou se trouve le cerveau

Le cerveau est un dossier nomme `cerveau/` a la racine de l'espace de travail partage (le dossier ouvert dans la session). S'il n'existe pas, ce Skill ne fait rien : il n'y a pas de cerveau a lire ni a alimenter.

La source de verite des conventions est `cerveau/00_CONTEXTE.md`. Ce Skill ne duplique pas ces conventions, il s'y refere.

## Synchronisation Git (optionnelle, automatique si presente)

Si le cerveau vit dans un depot Git, ce Skill maintient la synchro tout seul : l'equipe n'a jamais a taper de commande Git. Si le cerveau n'est pas dans un depot Git, ignorer entierement cette section (le Skill fonctionne en local comme avant).

**Detection** : depuis le dossier du cerveau, recuperer la racine du depot avec `git -C "<cerveau>" rev-parse --show-toplevel`. Si la commande echoue, il n'y a pas de depot : ne rien faire de ce qui suit.

**Au demarrage, avant la lecture, se mettre a jour** :
- `git -C "<racine>" pull --rebase --autostash`
- Si la commande echoue (hors ligne, pas d'acces reseau), ne pas bloquer : continuer avec la version locale et le signaler en une phrase.
- En cas de conflit, le resoudre s'il est trivial (fichiers differents ou ajouts distincts) ; sinon, prevenir l'utilisateur et continuer en lecture seule.

**Sur "MAJ cerveau", apres avoir range, journalise et rafraichi le cockpit, publier** :
- `git -C "<racine>" add -A`
- `git -C "<racine>" commit -m "MAJ cerveau: <resume en une phrase>"`
- `git -C "<racine>" push`
- Si le push est rejete parce que le distant a avance, faire `git -C "<racine>" pull --rebase --autostash` puis re-pousser.
- Si le push echoue pour cause d'authentification ou de reseau, le signaler clairement : le travail est commite en local et sera pousse a la prochaine occasion. Ne pas bloquer.

Cette synchro ne concerne que le contenu du cerveau. Le fichier d'identite de l'auteur (voir plus bas) vit hors du depot et ne doit jamais etre committe.

## Declencheurs

- **Au demarrage d'une session** sur un projet contenant `cerveau/` : appliquer le protocole de lecture.
- **Quand l'utilisateur ecrit "MAJ cerveau"** (eventuellement suivi de l'information) : appliquer le protocole d'ecriture. C'est le seul declencheur d'ecriture. Ne jamais ecrire dans le cerveau sans ce mot-cle.

## Protocole de lecture (au demarrage)

0. **Se synchroniser d'abord** (si le cerveau est dans un depot Git) : appliquer le `pull` decrit dans "Synchronisation Git" pour partir de la derniere version de l'equipe avant de lire.
1. Lire `cerveau/00_CONTEXTE.md` en entier. Il est court et contient la table d'aiguillage.
2. Identifier le sujet de la session (ce que l'utilisateur demande).
3. A l'aide de la table d'aiguillage, charger **uniquement** le ou les sous-dossiers pertinents. Ne pas charger tout le cerveau.
4. Si le sujet est vague, lister les titres de fiches des dossiers candidats avant de lire en detail.
5. Utiliser ce savoir comme acquis : ne pas redemander a l'utilisateur ce qui est deja ecrit dans le cerveau.

## Protocole d'ecriture (sur "MAJ cerveau")

Detail complet et exemples : voir `references/protocole-ecriture.md`. En resume :

1. **Recueillir** l'information a memoriser (la demander si "MAJ cerveau" arrive seul).
2. **Categoriser** via la table d'aiguillage de `00_CONTEXTE.md` (le bon dossier selon la nature de l'info).
3. **Anti-doublon** : lire les fiches du dossier cible et chercher si l'info existe deja (titres et mots-cles). Si une fiche proche existe, proposer de la mettre a jour plutot que d'en creer une nouvelle, et attendre l'accord.
4. **Ranger** : integrer proprement dans la fiche choisie, ou creer une nouvelle fiche au format de `references/modeles-fiches.md` (nom en minuscules sans accents, en-tete avec statut, date, auteur, mots-cles).
5. **Journaliser** : ajouter une ligne en haut du tableau de `cerveau/00_JOURNAL.md` (date du jour, auteur, chemin du fichier, resume en une phrase).
6. **Rafraichir le cockpit** (si present) : si le cerveau contient `_cockpit/generate.py`, regenerer la visualisation avec `python3 <cerveau>/_cockpit/generate.py`. Commodite en lecture seule ; si `python3` est absent, ignorer sans bloquer.
7. **Synchroniser** (si le cerveau est dans un depot Git) : appliquer le `add` + `commit` + `push` decrit dans "Synchronisation Git" pour rendre la mise a jour visible a l'equipe.
8. **Confirmer** en une seule phrase, en indiquant le fichier touche, l'action (cree ou mis a jour) et, si Git est present, que la mise a jour a ete poussee (ou conservee en local si le push n'a pas pu aboutir).

## Identite de l'auteur

L'auteur inscrit au journal vient d'un fichier local, propre a chaque machine, hors du dossier partage :

- macOS / Linux : `~/.cerveau-partage/auteur.txt`
- Windows : `%USERPROFILE%\.cerveau-partage\auteur.txt`

Le fichier contient une seule ligne : le prenom (ou un identifiant) de l'utilisateur.

Au moment d'ecrire (etape 5 ci dessus) :
1. Lire ce fichier. S'il existe, utiliser son contenu comme auteur, sans poser de question.
2. S'il n'existe pas, demander une fois a l'utilisateur "Sous quel nom journaliser tes mises a jour ?", creer le dossier et le fichier avec sa reponse, puis continuer. Les fois suivantes, l'etape 1 suffit.

Ce fichier est volontairement hors de `cerveau/` pour ne pas se synchroniser entre les membres de l'equipe.

## Cockpit (visualisation, optionnel)

Le cerveau peut contenir un cockpit : une page HTML autonome (`cerveau/cockpit.html`) qui presente les fiches, le journal et les conventions, en lecture seule. Elle est generee par `cerveau/_cockpit/generate.py` (Python standard, sans dependance), qui lit les fichiers Markdown sans jamais les modifier. Le protocole d'ecriture la regenere apres chaque MAJ cerveau pour qu'elle reste a jour. Si le cerveau n'a pas de dossier `_cockpit/`, ignorer cette etape.

## Regles de prudence

- Aucune ecriture sans "MAJ cerveau".
- Ne pas supprimer ni reecrire en masse une fiche existante sans accord explicite.
- En cas de doublon, proposer la mise a jour, ne pas dupliquer.
- Toujours journaliser une ecriture, et toujours confirmer en une phrase.

---

# Cerveau Partage (English)

A light team-memory layer on top of a folder of Markdown files. All knowledge lives in a `cerveau/` folder. This Skill only adds reading and writing discipline; it stores nothing itself and does not replace the files.

## Where the brain is

The brain is a folder named `cerveau/` at the root of the shared workspace (the folder opened in the session). If it does not exist, this Skill does nothing. The source of truth for conventions is `cerveau/00_CONTEXTE.md`; this Skill refers to it instead of duplicating it.

## Git synchronization (optional, automatic when present)

If the brain lives in a Git repository, this Skill keeps it in sync by itself: the team never types a Git command. If the brain is not in a Git repository, ignore this whole section (the Skill works locally as before).

**Detection**: from the brain folder, get the repo root with `git -C "<brain>" rev-parse --show-toplevel`. If it fails, there is no repo: do none of the following.

**At startup, before reading, update**: `git -C "<root>" pull --rebase --autostash`. If it fails (offline, no access), do not block: continue with the local version and say so in one sentence. On a conflict, resolve it if trivial (different files or distinct additions); otherwise warn the user and continue read-only.

**On "MAJ cerveau", after filing, logging and refreshing the cockpit, publish**: `git -C "<root>" add -A`, then `git -C "<root>" commit -m "MAJ cerveau: <one-sentence summary>"`, then `git -C "<root>" push`. If the push is rejected because the remote moved ahead, run `git -C "<root>" pull --rebase --autostash` then push again. If the push fails for auth or network reasons, say so clearly: the work is committed locally and will be pushed next time. Do not block.

This sync only covers the brain content. The author identity file (see below) lives outside the repo and must never be committed.

## Triggers

- **At session start** on a project containing `cerveau/`: apply the reading protocol.
- **When the user writes "MAJ cerveau"** (the project keyword, kept in French): apply the writing protocol. This is the only write trigger. Never write to the brain without it.

## Reading protocol (at startup)

0. **Sync first** (if the brain is in a Git repo): run the `pull` from "Git synchronization" to start from the team's latest version before reading.
1. Read all of `cerveau/00_CONTEXTE.md` (short, contains the routing table).
2. Identify the session topic.
3. Using the routing table, load **only** the relevant subfolder(s). Do not load the whole brain.
4. If the topic is vague, list note titles from candidate folders before reading in detail.
5. Treat this knowledge as given: do not re-ask the user what the brain already records.

## Writing protocol (on "MAJ cerveau")

Full detail and examples: see `references/protocole-ecriture.md`. In short: collect the information, categorize it via the routing table, check for an existing near-duplicate (and offer to update it rather than create a new one), file it cleanly using the templates in `references/modeles-fiches.md`, prepend a line to `cerveau/00_JOURNAL.md`, refresh the cockpit if present (run `python3 <cerveau>/_cockpit/generate.py`, a read-only convenience, skipped without blocking if python3 is unavailable), then (if the brain is in a Git repo) commit and push the update so the team sees it (see "Git synchronization"), then confirm in a single sentence.

## Author identity

The journal author comes from a local, per-machine file outside the shared folder: `~/.cerveau-partage/auteur.txt` (macOS/Linux) or `%USERPROFILE%\.cerveau-partage\auteur.txt` (Windows), one line with the user's name. On write: read it and use it silently if present; if missing, ask once, create the file, then continue. It is kept outside `cerveau/` so it does not sync between teammates.

## Cockpit (optional visualization)

The brain may contain a cockpit: a self-contained HTML page (`cerveau/cockpit.html`) that presents the notes, the log and the conventions, read-only. It is generated by `cerveau/_cockpit/generate.py` (standard Python, no dependency), which reads the Markdown files without ever modifying them. The writing protocol regenerates it after each MAJ cerveau so it stays current. If the brain has no `_cockpit/` folder, skip this step.

## Safety rules

No write without "MAJ cerveau". Never mass-delete or mass-rewrite an existing note without explicit agreement. On a duplicate, offer an update instead of duplicating. Always log a write, and always confirm in one sentence.
