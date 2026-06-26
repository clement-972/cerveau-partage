# Example: onboarding a teammate (ClickUp)

This is a **concrete example** of using the cerveau-partage skill with **ClickUp** as the documentation tool. The skill itself is connector-agnostic; if your team uses Notion or another tool, adapt the steps to that connector. The brain here is a ClickUp Doc named "Cerveau".

*(Version francaise plus bas.)*

## One-time setup (for the teammate)

1. Install the `cerveau-partage` skill in their Cowork.
2. Authorize the ClickUp connector in their Cowork.
3. Confirm they can open the "Cerveau" Doc in ClickUp (the doc inherits the documentation space's sharing).

## First use / test

4. **Read.** Ask Claude "What is in our cerveau?". Claude locates the "Cerveau" Doc and reads its routing table. If it cannot find it, it asks once for the Doc URL; paste it.
5. **Write.** Send a `MAJ cerveau` with a small piece of info. On the very first one, Claude asks for the name to log under (once). Claude files the note in the right sub-page and adds a line to the Journal.
6. **Check.** Open ClickUp and confirm the note and the journal line appeared.

## Cross-check

7. Another team member opens the cockpit (or the ClickUp Doc) and confirms they see the teammate's update.
8. Optional: the teammate asks "open the brain cockpit" to instantiate their own read-only dashboard (a Cowork artifact).

**Success criterion:** the teammate's `MAJ cerveau` appears in ClickUp and others see it, without the teammate being the Doc owner.

Ready-to-use test phrase for step 5:

> MAJ cerveau : pour les exports CSV, on utilise le point-virgule comme separateur.

(It should land in `03 Specs techniques`. Delete the test note afterward.)

---

# Exemple : embarquer un coequipier (ClickUp)

Ceci est un **exemple concret** d'usage du skill cerveau-partage avec **ClickUp** comme outil de documentation. Le skill, lui, est agnostique du connecteur ; si l'equipe utilise Notion ou un autre outil, adapter les etapes a ce connecteur. Ici, le cerveau est un Doc ClickUp nomme "Cerveau".

## Preparation (une seule fois, cote coequipier)

1. Installer le skill `cerveau-partage` dans son Cowork.
2. Autoriser le connecteur ClickUp dans son Cowork.
3. Verifier qu'il ouvre bien le Doc "Cerveau" dans ClickUp (le doc herite des droits de partage de l'espace Documentation).

## Premier usage / test

4. **Lecture.** Demander a Claude "Qu'y a-t-il dans notre cerveau ?". Claude localise le Doc "Cerveau" et lit la table d'aiguillage. S'il ne le trouve pas, il demande l'URL une fois ; la coller.
5. **Ecriture.** Envoyer un `MAJ cerveau` avec une info de test. Au tout premier, Claude demande le nom a inscrire au journal (une fois). Claude range la fiche dans la bonne sous-page et ajoute une ligne au Journal.
6. **Verifier.** Ouvrir ClickUp et confirmer que la fiche et la ligne de journal sont apparues.

## Validation croisee

7. Un autre membre ouvre le cockpit (ou le Doc ClickUp) et confirme qu'il voit la contribution du coequipier.
8. Optionnel : le coequipier demande "ouvre le cockpit du cerveau" pour instancier son propre tableau de bord en lecture seule (un artefact Cowork).

**Critere de reussite :** le `MAJ cerveau` du coequipier apparait dans ClickUp et les autres le voient, sans qu'il soit proprietaire du Doc.

Phrase de test prete a l'emploi pour l'etape 5 :

> MAJ cerveau : pour les exports CSV, on utilise le point-virgule comme separateur.

(Elle doit aller dans `03 Specs techniques`. Supprimer la fiche de test ensuite.)
