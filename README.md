# Cerveau Partage

*Langue : Francais (ce fichier) | [English](README.en.md)*

Une memoire partagee pour equipe produit, posee sur de simples fichiers Markdown dans un dossier partage. Chacun y verse le savoir stabilise (reglementaire, specs, decisions, roadmap, skills) ; tout le monde le relit au demarrage de ses sessions IA. Plus besoin de reexpliquer ce qui est deja su.

Pas de serveur, pas de base de donnees, pas d'interface a installer. Le cerveau reste lisible et editable a la main : meme sans l'outil, ce sont juste des fichiers Markdown.

## Ce que contient ce depot

```
cerveau-partage/
├── README.md            ce fichier (FR)
├── README.en.md         version anglaise
├── LICENSE              licence MIT
├── cerveau/             le modele de cerveau, pret a copier dans le dossier partage
│   ├── 00_CONTEXTE.md   mode d'emploi + table d'aiguillage (lu par l'IA au demarrage)
│   ├── 00_JOURNAL.md    journal horodate des ecritures
│   ├── 01_reglementaire/ ... 06_en_cours/   6 categories, une fiche d'exemple chacune
│   ├── cockpit.html     visualisation autonome (instantane genere, lecture seule)
│   └── _cockpit/        generateur du cockpit (generate.py, Python standard, sans dependance)
└── skill/
    └── cerveau-partage/ le Skill (standard Agent Skills)
        ├── SKILL.md
        └── references/  protocole d'ecriture + modeles de fiches
```

## Comment ca marche, en deux idees

1. **Lecture ciblee au demarrage.** Quand tu ouvres une session IA dans le dossier partage, l'IA lit `cerveau/00_CONTEXTE.md`, puis charge seulement le sous-dossier utile a ton sujet (pas tout le cerveau).
2. **Ecriture sur declenchement.** Rien n'est ecrit dans le cerveau sans le mot-cle **"MAJ cerveau"**. Quand tu l'ecris, l'IA range l'info dans la bonne categorie, evite les doublons, ajoute une ligne au journal et confirme en une phrase.

## Les categories

| Dossier | Pour quoi |
|---------|-----------|
| `01_reglementaire/` | conformite, obligations legales, normes |
| `02_specs_fonctionnelles/` | comportement du produit, parcours, regles metier |
| `03_specs_techniques/` | architecture, API, schema de donnees, choix techniques |
| `04_skills/` | prompts, procedures reutilisables, methodes de travail avec l'IA |
| `05_roadmap/` | vision, priorites, jalons |
| `06_en_cours/` | decisions en cours, questions ouvertes |

## Deux choses a ne pas confondre

Cette distinction evite la plupart des confusions :

- **La competence** (le dossier `skill/cerveau-partage/`, celui qui contient `SKILL.md`) est l'outil. Tu l'ajoutes a Claude une fois par personne. Elle ne contient aucune donnee.
- **Le cerveau** (le dossier `cerveau/`) est la donnee partagee de l'equipe. Il vit dans un dossier synchronise, et c'est ce dossier que tu ouvres dans Claude pour travailler.

## Installation

### 1. Installer la competence dans Claude
La competence suit le standard ouvert Agent Skills (un dossier avec un `SKILL.md`). Ajoute la dans les reglages de ton assistant, a l'endroit qui gere les competences (Reglages, Capacites ou Skills selon l'outil), en pointant le dossier `skill/cerveau-partage` (celui qui contient `SKILL.md`), surtout pas le dossier `cerveau/`.

Pour Claude Code, l'emplacement habituel est `~/.claude/skills/cerveau-partage/` (pour toi seul) ou `.claude/skills/cerveau-partage/` dans le dossier du projet (partage avec l'equipe). C'est une etape a faire une fois par machine.

### 2. Mettre le cerveau dans un dossier partage
Le cerveau n'est qu'un dossier de fichiers Markdown. Copie le dossier `cerveau/` la ou ton equipe synchronise deja ses fichiers. L'outil n'impose aucun service : il fonctionne avec ce que ta boite utilise et a deja valide.

Une seule regle technique a respecter : choisis une synchro qui garde les fichiers reellement sur le disque local (evite les modes "en ligne uniquement" ou "streaming"). Sinon Claude n'ecrit pas de facon fiable. C'est ce qui posait probleme avec Google Drive en streaming, pas le partage en lui meme.

Quelques recettes equivalentes, a choisir selon ton contexte :

- **OneDrive ou SharePoint** (souvent deja en place en entreprise Microsoft 365) : synchronise un dossier ou une bibliotheque d'equipe sur ta machine, fichiers gardes en local. Synchro automatique en fond : plus rien a penser apres "MAJ cerveau".
- **Partage reseau, Dropbox ou equivalent** : meme principe, un dossier d'equipe synchronise en local. Synchro automatique.
- **Git** (equipes a l'aise, ou si tu veux l'historique et la tracabilite) : un depot prive appartenant a l'organisation. Le partage demande un geste (push et pull), via GitHub Desktop ou automatise. Bonus : chaque modification est datee et attribuee, ce qui complete le journal.

Aucune de ces options n'est imposee. Le cerveau restant un simple dossier, tu peux changer de mode de partage a tout moment sans rien casser.

### 3. (Optionnel) Ton nom pour le journal
Le journal note qui a fait chaque mise a jour. Ton nom est lu dans un petit fichier local, propre a ta machine et hors du dossier partage :

- macOS / Linux : `~/.cerveau-partage/auteur.txt`
- Windows : `%USERPROFILE%\.cerveau-partage\auteur.txt`

Une seule ligne, ton prenom. Si tu ne crees pas ce fichier, l'IA te demandera ton nom au tout premier "MAJ cerveau" et le creera pour toi. Tu n'auras la question qu'une fois.

## Usage au quotidien

**Lire (automatique).** Ouvre une session dans le dossier partage et pose ta question. Exemple : "Quelles sont nos mentions obligatoires sur les factures ?" L'IA charge `01_reglementaire/` et te repond avec ce qui est deja connu.

**Ecrire (sur demande).** Ecris "MAJ cerveau" suivi de l'information. Exemple :

> MAJ cerveau : on a tranche, on part sur des UUID v4 pour les identifiants d'API.

L'IA range la decision dans `03_specs_techniques/`, verifie qu'une fiche proche n'existe pas deja, journalise, et confirme : "C'est range : `03_specs_techniques/identifiants-api.md` cree et journalise."

## Cockpit (visualisation)

Le cerveau inclut un cockpit : une page HTML autonome, `cerveau/cockpit.html`, qui presente toutes les fiches, le journal et les conventions dans une interface lisible, avec recherche. Pour l'ouvrir, double-clique simplement sur `cockpit.html`. C'est une vue en lecture seule : elle ne modifie jamais le cerveau.

La page est un instantane, regenere a partir des fichiers Markdown par `cerveau/_cockpit/generate.py` (Python standard, aucune dependance). Le Skill la rafraichit automatiquement apres chaque "MAJ cerveau", donc elle reste a jour sans rien faire. Pour la regenerer a la main :

```
python3 cerveau/_cockpit/generate.py
```

Si Python n'est pas installe, le cerveau reste pleinement utilisable : le cockpit est un confort, pas une dependance.

## Tester en cinq minutes (le critere de reussite)

1. Mets le dossier `cerveau/` dans un espace partage entre deux machines (OneDrive, un partage reseau ou Git).
2. Sur la machine A, ouvre une session et ecris : `MAJ cerveau : nos factures doivent afficher le numero de TVA intracommunautaire du client pour les ventes dans l'UE.`
3. Verifie qu'une fiche apparait dans `cerveau/01_reglementaire/` et qu'une ligne s'ajoute en haut de `cerveau/00_JOURNAL.md`.
4. Laisse la synchronisation se faire, puis sur la machine B ouvre une session et demande : "Que doit-on afficher sur les factures pour les ventes dans l'UE ?"
5. L'IA doit repondre avec la regle, sans que tu aies eu a la reexpliquer.

## Pourquoi pas de serveur ni de service impose

Choix d'architecture assume, et c'est ce qui distingue l'outil :

- **Legerete** : pas de serveur a heberger, pas de base de donnees, pas de compte a creer. L'outil reste auditable et le cerveau survit a l'outil.
- **Securite** : la donnee, parfois sensible, ne quitte jamais l'infrastructure deja approuvee par ton entreprise. Aucun nouveau prestataire, aucune nouvelle surface d'attaque, pas de contrat supplementaire a faire valider.
- **Portabilite** : chaque organisation a ses contraintes (achats, outils autorises). En restant un dossier, l'outil s'adapte a toutes au lieu d'en imposer une.

## Hors perimetre

Pas de serveur ni de base de donnees, pas de recherche semantique, pas de detection de contradictions au dela de l'anti-doublon simple, pas de gestion de modifications simultanees, pas d'interface graphique, pas de multi-espaces, pas d'authentification. C'est un choix : l'outil reste leger et le cerveau survit a l'outil.

## Licence

MIT. Voir [LICENSE](LICENSE). Utilisation, modification et diffusion libres.

## Auteur

Cerveau Partage, cree et maintenu par Clément Deschamps. LinkedIn : https://www.linkedin.com/in/clementdeschamps/
