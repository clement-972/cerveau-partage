# Cerveau Partage (Shared Brain)

*Language: English (this file) | [Francais](README.fr.md)*

A shared memory for product teams, built on a structured Doc inside the documentation tool your team already uses (ClickUp, Notion, or any tool with a connector). Everyone writes stabilized knowledge into it (regulatory, specs, decisions, roadmap, skills); everyone reads it back across their AI sessions. No more re-explaining what is already known.

No folder to sync, no local files to manage: the brain lives where your team already works, and the AI reaches it through that tool's connector.

The project name, the write keyword "MAJ cerveau" and the category names are kept in French, because that is the original team's working language. They are a convention you can change.

## What this repository contains

```
cerveau-partage/
├── README.md            this file (EN)
├── README.fr.md         French version
├── LICENSE              MIT license
└── skill/
    └── cerveau-partage/ the Skill (Agent Skills standard)
        ├── SKILL.md
        └── references/  writing protocol + note templates
```

## How it works, in two ideas

1. **Targeted reading.** When a question overlaps team knowledge, the AI locates the "Cerveau" Doc, reads its "Sommaire et conventions" page (the routing table), then opens only the relevant sub-page (not the whole brain).
2. **Triggered writing.** Nothing is written without the keyword **"MAJ cerveau"**. When you write it, the AI files the information in the right sub-page, avoids duplicates, adds a line to the Journal, and confirms in one sentence.

## Brain structure

The brain is a "Cerveau" Doc, to recreate in your tool:

```
Cerveau
└── Sommaire et conventions   (user guide + routing table)
    ├── Journal               (timestamped write log)
    ├── 01 Reglementaire      compliance, legal obligations, standards
    ├── 02 Specs fonctionnelles  product behavior, journeys, business rules
    ├── 03 Specs techniques   architecture, API, data model, technical choices
    ├── 04 Skills             prompts, reusable procedures, AI working methods
    ├── 05 Roadmap            vision, priorities, milestones
    └── 06 En cours           ongoing decisions, open questions
```

## Two things not to confuse

- **The skill** (the `skill/cerveau-partage/` folder, the one containing `SKILL.md`) is the tool. You add it to Claude once per person. It holds no data.
- **The brain** is the team's shared data: the "Cerveau" Doc in your documentation tool. The AI reaches it through that tool's connector.

## Installation

### 1. Install the skill in Claude
The skill follows the open Agent Skills standard (a folder with a `SKILL.md`). Add it in your assistant's settings, wherever skills are managed (Settings, Capabilities or Skills depending on the tool), pointing at the `skill/cerveau-partage` folder. This is a one-time step per machine.

### 2. Create the brain in your documentation tool
Recreate the structure above in your team's tool (ClickUp, Notion, etc.): a "Cerveau" Doc with a "Sommaire et conventions" page holding the routing table, a "Journal" page, and one sub-page per category. Share that Doc with the team according to your space's permissions.

One requirement: the tool must be reachable by Claude through a connector, and each member must have authorized that connector on their side.

### 3. Point the skill at the brain
The skill locates the brain in three ways, in order: a reference (Doc URL or ID) filled into `SKILL.md`; otherwise a search by name ("Cerveau") via the connector; otherwise a one-time question whose answer is remembered. For a team, the simplest is to fill the Doc reference into `SKILL.md`.

### Your name for the log
The log records who makes each update. The skill asks for your name on the very first "MAJ cerveau" and reuses it afterward. You are asked only once.

## Daily use

**Read (automatic).** Ask your question, e.g. "What are our mandatory invoice notices?" The AI opens `01 Reglementaire` and answers from what is already known.

**Write (on request).** Write "MAJ cerveau" followed by the information:

> MAJ cerveau: we decided, we are going with UUID v4 for API identifiers.

The AI files the decision under `03 Specs techniques`, checks no close note already exists, logs it, and confirms.

## One technical rule to know

Some connectors replace a page's entire content on update (ClickUp; Notion edits surgically). The skill therefore always applies the "read before rewrite" rule: it re-reads the current content and sends back the whole thing plus the addition, so it never overwrites the rest.

## Out of scope

No semantic search, no contradiction detection beyond simple de-duplication, no fine handling of concurrent edits. The skill builds on the documentation tool and its connector: it inherits that tool's limits and permissions.

## License

MIT. See [LICENSE](LICENSE). Free to use, modify, and distribute.

## Author

Cerveau Partage, created and maintained by Clément Deschamps. LinkedIn: https://www.linkedin.com/in/clementdeschamps/
