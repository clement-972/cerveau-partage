# Cerveau Partage

*Langue : Francais (ce fichier) | [English](README.md)*

Une memoire partagee pour equipe produit, posee sur un Doc structure dans l'outil de documentation que ton equipe utilise deja (ClickUp, Notion, ou tout outil muni d'un connecteur). Chacun y verse le savoir stabilise (reglementaire, specs, decisions, roadmap, skills) ; tout le monde le relit au fil de ses sessions IA. Plus besoin de reexpliquer ce qui est deja su.

Pas de dossier a synchroniser, pas de fichiers locaux a gerer : le cerveau vit la ou ton equipe travaille deja, et l'IA y accede par le connecteur de cet outil.

Le nom du projet, le mot-cle "MAJ cerveau" et les noms de categories sont en francais : c'est la langue de travail de l'equipe d'origine. C'est une convention que tu peux changer.

## Ce que contient ce depot

```
cerveau-partage/
├── README.md            version anglaise (primaire)
├── README.fr.md         ce fichier (FR)
├── LICENSE              licence MIT
└── skill/
    └── cerveau-partage/ le Skill (standard Agent Skills)
        ├── SKILL.md
        └── references/  protocole d'ecriture + modeles de fiches
```

## Comment ca marche, en deux idees

1. **Lecture ciblee.** Quand une question recoupe le savoir d'equipe, l'IA localise le Doc "Cerveau", lit sa page "Sommaire et conventions" (la table d'aiguillage), puis ouvre seulement la sous-page utile (pas tout le cerveau).
2. **Ecriture sur declenchement.** Rien n'est ecrit sans le mot-cle **"MAJ cerveau"**. Quand tu l'ecris, l'IA range l'info dans la bonne sous-page, evite les doublons, ajoute une ligne au Journal et confirme en une phrase.

## Structure du cerveau

Le cerveau est un Doc "Cerveau", a recreer dans ton outil :

```
Cerveau
└── Sommaire et conventions   (mode d'emploi + table d'aiguillage)
    ├── Journal               (journal horodate des ecritures)
    ├── 01 Reglementaire      conformite, obligations legales, normes
    ├── 02 Specs fonctionnelles  comportement produit, parcours, regles metier
    ├── 03 Specs techniques   architecture, API, schema de donnees, choix techniques
    ├── 04 Skills             prompts, procedures reutilisables, methodes IA
    ├── 05 Roadmap            vision, priorites, jalons
    └── 06 En cours           decisions en cours, questions ouvertes
```

## Deux choses a ne pas confondre

- **La competence** (le dossier `skill/cerveau-partage/`, celui qui contient `SKILL.md`) est l'outil. Tu l'ajoutes a Claude une fois par personne. Elle ne contient aucune donnee.
- **Le cerveau** est la donnee partagee de l'equipe : le Doc "Cerveau" dans ton outil de documentation. L'IA y accede via le connecteur de cet outil.

## Installation

### 1. Installer la competence dans Claude
La competence suit le standard ouvert Agent Skills (un dossier avec un `SKILL.md`). Ajoute-la dans les reglages de ton assistant, a l'endroit qui gere les competences (Reglages, Capacites ou Skills selon l'outil), en pointant le dossier `skill/cerveau-partage`. C'est une etape a faire une fois par machine.

### 2. Creer le cerveau dans ton outil de documentation
Recree la structure ci-dessus dans l'outil de ton equipe (ClickUp, Notion, etc.) : un Doc "Cerveau" avec une page "Sommaire et conventions" qui porte la table d'aiguillage, une page "Journal", et une sous-page par categorie. Partage ce Doc avec l'equipe selon les droits de ton espace.

Une seule contrainte : l'outil doit etre accessible a Claude via un connecteur, et chaque membre doit avoir autorise ce connecteur de son cote.

### 3. Pointer la competence sur le cerveau
La competence localise le cerveau de trois facons, dans l'ordre : une reference (URL ou ID du Doc) renseignee dans `SKILL.md` ; sinon une recherche par nom ("Cerveau") via le connecteur ; sinon une question posee une fois, dont la reponse est memorisee. Pour une equipe, le plus simple est de renseigner la reference du Doc dans `SKILL.md`.

### Ton nom pour le journal
Le journal note qui fait chaque mise a jour. La competence te demande ton nom au tout premier "MAJ cerveau" et le reutilise ensuite. Tu n'as la question qu'une fois.

## Usage au quotidien

**Lire (automatique).** Pose ta question, par exemple : "Quelles sont nos mentions obligatoires sur les factures ?" L'IA ouvre `01 Reglementaire` et te repond avec ce qui est deja connu.

**Ecrire (sur demande).** Ecris "MAJ cerveau" suivi de l'information :

> MAJ cerveau : on a tranche, on part sur des UUID v4 pour les identifiants d'API.

L'IA range la decision dans `03 Specs techniques`, verifie qu'une fiche proche n'existe pas deja, journalise, et confirme : "C'est range : fiche ajoutee dans `03 Specs techniques` et journalisee."

## Une regle technique a connaitre

Certains connecteurs remplacent tout le contenu d'une page a la mise a jour (ClickUp ; Notion edite de facon ciblee). La competence applique donc systematiquement la regle "lire la page avant de la reecrire" : elle relit le contenu actuel et renvoie l'ensemble augmente de l'ajout, pour ne jamais ecraser le reste.

## Hors perimetre

Pas de recherche semantique, pas de detection de contradictions au dela de l'anti-doublon simple, pas de gestion fine des modifications simultanees. La competence s'appuie sur l'outil de documentation et son connecteur : elle herite donc des limites et des droits de cet outil.

## Exemple

Pour un deroule concret d'embarquement d'un coequipier avec ClickUp, voir [examples/onboarding-clickup.md](examples/onboarding-clickup.md). Le skill reste agnostique du connecteur ; ce n'est que l'instance d'un outil.

## Licence

MIT. Voir [LICENSE](LICENSE). Utilisation, modification et diffusion libres.

## Auteur

Cerveau Partage, cree et maintenu par Clément Deschamps. LinkedIn : https://www.linkedin.com/in/clementdeschamps/
