# 00 - CONTEXTE : mode d'emploi du cerveau partage

> Ce fichier est la source unique de verite du cerveau. Il est lu en premier au demarrage de chaque session IA. Il reste comprehensible meme sans l'outil "Cerveau Partage" : ce ne sont que des fichiers Markdown.

*(English version below / Version anglaise plus bas)*

---

## A quoi sert ce dossier

Ce dossier est la memoire commune d'une equipe produit. Chacun y verse le savoir stabilise (reglementaire, specs, decisions, roadmap, skills), et tout le monde le relit au demarrage de ses sessions IA. Objectif : ne plus reexpliquer ce qui est deja su, et garder une trace auditable des decisions.

## Les deux regles fondamentales

1. **Lecture ciblee au demarrage.** L'IA lit ce fichier, puis charge uniquement le ou les sous-dossiers utiles au sujet en cours (voir la table d'aiguillage). Elle ne charge pas tout le cerveau.
2. **Ecriture sur declenchement humain uniquement.** Rien n'est ecrit dans le cerveau sans le mot-cle explicite **"MAJ cerveau"**. Aucune ecriture spontanee.

## Table d'aiguillage

Pour trouver ou lire et ou ecrire, on associe un sujet a un dossier.

| Sujet | Dossier | Exemples de contenu |
|-------|---------|---------------------|
| Conformite, obligations legales | `01_reglementaire/` | RGPD, normes, mentions obligatoires, facturation electronique, contraintes legales |
| Comportement du produit | `02_specs_fonctionnelles/` | parcours utilisateur, regles metier, fonctionnalites, cas limites |
| Realisation technique | `03_specs_techniques/` | architecture, API, schema de donnees, stack, choix d'implementation |
| Travail avec l'IA | `04_skills/` | prompts, skills, procedures reutilisables, methodes de travail |
| Direction produit | `05_roadmap/` | vision, priorites, jalons, ce qui est prevu plus tard |
| Sujets non stabilises | `06_en_cours/` | decisions en cours, questions ouvertes, travaux a trancher |

Regle de tri en cas de doute : on choisit le dossier qui correspond a la **nature** de l'information, pas au projet qui l'a produite. Si une info est encore mouvante, elle va dans `06_en_cours/` ; une fois stabilisee, elle est deplacee vers son dossier definitif.

## Convention des fiches

Chaque fiche est un fichier `.md`. Nom en minuscules, mots separes par des tirets bas, sans accents (exemple : `mentions-obligatoires-facture.md`). En-tete standard :

```
# Titre clair de la fiche

> Statut : stable | Derniere maj : AAAA-MM-JJ | Auteur : Prenom | Mots-cles : mot1, mot2, mot3

Contenu de la fiche.
```

Les mots-cles servent au reperage et a l'anti-doublon. Le statut vaut `stable` dans les dossiers definitifs et `en cours` dans `06_en_cours/`.

## Convention du journal

Le fichier `00_JOURNAL.md` enregistre chaque ecriture, ligne la plus recente en haut, au format tableau : date, auteur, fichier, resume en une phrase.

## Hors perimetre

Pas de serveur, pas de base de donnees, pas de recherche semantique, pas de gestion de conflits de modification simultanee. Le cerveau reste un ensemble de fichiers Markdown que l'on peut lire, editer et versionner a la main.

---

# 00 - CONTEXT: shared brain user guide

> This file is the single source of truth for the brain. It is read first at the start of every AI session. It stays understandable even without the "Cerveau Partage" tool: these are just Markdown files.

## What this folder is for

This folder is the shared memory of a product team. Everyone writes stabilized knowledge into it (regulatory, specs, decisions, roadmap, skills), and everyone reads it back at the start of their AI sessions. Goal: stop re-explaining what is already known, and keep an auditable trace of decisions.

## The two core rules

1. **Targeted reading at startup.** The AI reads this file, then loads only the subfolder(s) relevant to the current topic (see the routing table). It does not load the whole brain.
2. **Human-triggered writing only.** Nothing is written into the brain without the explicit keyword **"MAJ cerveau"** (the project keyword, kept in French). No spontaneous writes.

## Routing table

To know where to read and where to write, a topic maps to a folder.

| Topic | Folder | Example content |
|-------|--------|-----------------|
| Compliance, legal obligations | `01_reglementaire/` | GDPR, standards, mandatory notices, e-invoicing, legal constraints |
| Product behavior | `02_specs_fonctionnelles/` | user journeys, business rules, features, edge cases |
| Technical implementation | `03_specs_techniques/` | architecture, API, data model, stack, implementation choices |
| Working with AI | `04_skills/` | prompts, skills, reusable procedures, working methods |
| Product direction | `05_roadmap/` | vision, priorities, milestones, what is planned later |
| Unsettled topics | `06_en_cours/` | ongoing decisions, open questions, work to be settled |

Sorting rule when in doubt: pick the folder that matches the **nature** of the information, not the project that produced it. If an item is still moving, it goes to `06_en_cours/`; once stabilized, it is moved to its final folder.

## Note convention

Each note is a `.md` file. Lowercase name, words separated by underscores or hyphens, no accents (example: `mentions-obligatoires-facture.md`). Standard header:

```
# Clear note title

> Status: stable | Last update: YYYY-MM-DD | Author: FirstName | Keywords: word1, word2, word3

Note content.
```

Keywords help discovery and de-duplication. Status is `stable` in final folders and `en cours` in `06_en_cours/`.

## Log convention

The `00_JOURNAL.md` file records every write, most recent line on top, in table format: date, author, file, one-sentence summary.

## Out of scope

No server, no database, no semantic search, no concurrent-edit conflict handling. The brain stays a set of Markdown files you can read, edit and version by hand.
