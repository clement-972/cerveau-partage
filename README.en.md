# Cerveau Partage (Shared Brain)

*Language: English (this file) | [Francais](README.md)*

A shared memory for product teams, built on plain Markdown files in a shared folder. Everyone writes stabilized knowledge into it (regulatory, specs, decisions, roadmap, skills); everyone reads it back at the start of their AI sessions. No more re-explaining what is already known.

No server, no database, no interface to install. The brain stays readable and editable by hand: even without the tool, it is just Markdown files.

## What this repository contains

```
cerveau-partage/
├── README.md            French readme
├── README.en.md         this file (EN)
├── LICENSE              MIT license
├── cerveau/             the brain template, ready to copy into the shared folder
│   ├── 00_CONTEXTE.md   user guide + routing table (read by the AI at startup)
│   ├── 00_JOURNAL.md    timestamped write log
│   ├── 01_reglementaire/ ... 06_en_cours/  (6 categories, one example note each)
│   ├── cockpit.html     self-contained visualization (generated snapshot, read-only)
│   └── _cockpit/        cockpit generator (generate.py, standard Python, no dependency)
└── skill/
    └── cerveau-partage/ the Skill (Agent Skills standard)
        ├── SKILL.md
        └── references/  writing protocol + note templates
```

The category folder names are kept in French, as is the write keyword "MAJ cerveau", because that is the team's working language. Everything else is bilingual.

## How it works, in two ideas

1. **Targeted reading at startup.** When you open an AI session in the shared folder, the AI reads `cerveau/00_CONTEXTE.md`, then loads only the subfolder relevant to your topic (not the whole brain).
2. **Triggered writing.** Nothing is written into the brain without the keyword **"MAJ cerveau"**. When you write it, the AI files the information in the right category, avoids duplicates, adds a line to the log, and confirms in one sentence.

## The categories

| Folder | For |
|--------|-----|
| `01_reglementaire/` | compliance, legal obligations, standards |
| `02_specs_fonctionnelles/` | product behavior, journeys, business rules |
| `03_specs_techniques/` | architecture, API, data model, technical choices |
| `04_skills/` | prompts, reusable procedures, AI working methods |
| `05_roadmap/` | vision, priorities, milestones |
| `06_en_cours/` | ongoing decisions, open questions |

## Two things not to confuse

This distinction avoids most of the confusion:

- **The skill** (the `skill/cerveau-partage/` folder, the one containing `SKILL.md`) is the tool. You add it to Claude once per person. It holds no data.
- **The brain** (the `cerveau/` folder) is the team's shared data. It lives in a synced folder, and that folder is what you open in Claude to work.

## Installation

### 1. Install the skill in Claude
The skill follows the open Agent Skills standard (a folder with a `SKILL.md`). Add it in your assistant's settings, wherever skills are managed (Settings, Capabilities or Skills depending on the tool), pointing at the `skill/cerveau-partage` folder (the one containing `SKILL.md`), not the `cerveau/` folder.

For Claude Code, the usual location is `~/.claude/skills/cerveau-partage/` (just for you) or `.claude/skills/cerveau-partage/` in the project folder (shared with the team). This is a one-time step per machine.

### 2. Put the brain in a shared folder
The brain is just a folder of Markdown files. Copy the `cerveau/` folder wherever your team already syncs its files. The tool imposes no service: it works with whatever your company already uses and has approved.

One technical rule to follow: choose a sync that keeps the files actually on the local disk (avoid "online-only" or "streaming" modes). Otherwise Claude cannot write reliably. That, not sharing itself, is what broke with Google Drive in streaming mode.

A few equivalent recipes, pick by your context:

- **OneDrive or SharePoint** (often already in place in Microsoft 365 companies): sync a team folder or library to your machine, files kept local. Automatic background sync: nothing to think about after "MAJ cerveau".
- **Network share, Dropbox or equivalent**: same principle, a team folder synced locally. Automatic sync.
- **Git** (teams comfortable with it, or if you want history and traceability): a private repo owned by the organization. Sharing takes an action (push and pull), via GitHub Desktop or automated. Bonus: every change is dated and attributed, which complements the log.

None of these is mandatory. Since the brain stays a plain folder, you can change sharing method at any time without breaking anything.

### 3. (Optional) Your name for the log
The log records who made each update. Your name is read from a small local file, specific to your machine and outside the shared folder:

- macOS / Linux: `~/.cerveau-partage/auteur.txt`
- Windows: `%USERPROFILE%\.cerveau-partage\auteur.txt`

One line, your first name. If you do not create this file, the AI will ask for your name on the very first "MAJ cerveau" and create it for you. You are asked only once.

## Daily use

**Read (automatic).** Open a session in the shared folder and ask your question, e.g. "What are our mandatory invoice notices?" The AI loads `01_reglementaire/` and answers from what is already known.

**Write (on request).** Write "MAJ cerveau" followed by the information, e.g.:

> MAJ cerveau: we decided, we are going with UUID v4 for API identifiers.

The AI files the decision under `03_specs_techniques/`, checks no close note already exists, logs it, and confirms.

## Cockpit (visualization)

The brain includes a cockpit: a self-contained HTML page, `cerveau/cockpit.html`, that presents all notes, the log and the conventions in a readable interface, with search. To open it, just double-click `cockpit.html`. It is a read-only view: it never modifies the brain.

The page is a snapshot, regenerated from the Markdown files by `cerveau/_cockpit/generate.py` (standard Python, no dependency). The skill refreshes it automatically after each "MAJ cerveau", so it stays current with no effort. To regenerate it by hand:

```
python3 cerveau/_cockpit/generate.py
```

If Python is not installed, the brain stays fully usable: the cockpit is a convenience, not a dependency.

## Test it in five minutes (the success criterion)

1. Put the `cerveau/` folder in a space shared between two machines (OneDrive, a network share, or Git).
2. On machine A, open a session and write: `MAJ cerveau: our invoices must show the customer's intra-EU VAT number for sales within the EU.`
3. Check that a note appears in `cerveau/01_reglementaire/` and that a line is added at the top of `cerveau/00_JOURNAL.md`.
4. Let sync happen, then on machine B open a session and ask: "What must we display on invoices for EU sales?"
5. The AI should answer with the rule, without you having to re-explain it.

## Why no server and no imposed service

A deliberate architectural choice, and what sets the tool apart:

- **Lightness**: no server to host, no database, no account to create. The tool stays auditable and the brain outlives the tool.
- **Security**: the data, sometimes sensitive, never leaves the infrastructure your company has already approved. No new vendor, no new attack surface, no extra contract to clear.
- **Portability**: every organization has its constraints (purchasing, approved tools). By staying a folder, the tool adapts to all of them instead of imposing one.

## Out of scope

No server or database, no semantic search, no contradiction detection beyond simple de-duplication, no concurrent-edit handling, no graphical interface, no multi-workspace, no authentication. This is a deliberate choice: the tool stays light and the brain outlives the tool.

## License

MIT. See [LICENSE](LICENSE). Free to use, modify, and distribute.

## Author

Cerveau Partage, created and maintained by Clément Deschamps. LinkedIn: https://www.linkedin.com/in/clementdeschamps/
