# Nouveautés / What's new

Chaque version publiée a sa section ici. Elle sert à la fois de notes de version sur GitHub et de page
« Nouveautés » dans le programme. Écrite pour les joueurs : ce qui change pour eux, pas le détail technique.
La partie anglaise de chaque section vient après la ligne `<!-- en -->`.

## 1.1.3

**Amélioré**
- Mise à jour du compte qui publie Prédiction RL : cette version change l'adresse où le programme cherche ses mises à jour.
  Installe-la pour continuer à recevoir les prochaines versions. Rien ne change pour toi à l'utilisation, et tes données
  restent sur ton PC.

<!-- en -->

**Improved**
- The account that publishes Prédiction RL has been renamed: this version updates the address the app checks for updates.
  Install it to keep receiving future versions. Nothing changes for you when using it, and your data stays on your PC.

## 1.1.2

**Amélioré**
- Le programme reste gratuit, mais son code source n'est plus publié : cette page ne garde que la présentation,
  les versions et les tickets. Les versions jusqu'à la 1.1.1 restent sous licence MIT. Rien ne change pour toi à
  l'utilisation, et tes données restent sur ton PC.

<!-- en -->

**Improved**
- The app stays free, but its source code is no longer published: this page now only holds the presentation, the
  releases and the issues. Versions up to 1.1.1 remain under the MIT license. Nothing changes for you when using it,
  and your data stays on your PC.

## 1.1.1

**Corrigé**
- Menu : les choix (position, taille, opacité, langue, proba en direct) affichent bien l'option sélectionnée.
- Sécurité : la page locale du programme refuse désormais les requêtes d'autres sites, même déguisées
  (protection contre le « DNS rebinding »). Tes données restent sur ton PC.
- Une capture de match abîmée (programme coupé en pleine écriture) ne bloque plus l'entraînement de la proba en direct.

**Fiabilité**
- Chaque version est maintenant vérifiée avant sa sortie : 176 tests automatiques couvrant 100 % du code, analyse de
  sécurité du code et des dépendances.

<!-- en -->

**Fixed**
- Menu: choices (position, size, opacity, language, live probability) now show the selected option.
- Security: the app's local page now rejects requests coming from other websites, even disguised ones
  (protection against "DNS rebinding"). Your data stays on your PC.
- A damaged match capture (app closed mid-write) no longer blocks training of the live probability.

**Reliability**
- Every version is now checked before release: 176 automated tests covering 100% of the code, plus a security
  scan of the code and its dependencies.

## 1.1.0

**Nouveau**
- Le programme est disponible en anglais (il suit la langue de Windows, modifiable dans le menu).
- Onglet « Mes stats » : winrate, séries, évolution de ton MMR, justesse des prédictions, coéquipiers fréquents.
- La proba en direct peut tenir compte des stats du match (tirs, arrêts, démos), dès qu'elles se montrent utiles
  sur tes propres parties.
- Versions bêta : coche l'option dans le menu pour recevoir les nouveautés en avance.
- « Copier le diagnostic » (menu ou clic droit sur l'icône) : à coller dans un ticket GitHub pour signaler un
  problème, sans pseudo ni détail de tes games.

**Amélioré**
- En plein écran exclusif (où l'overlay ne peut pas s'afficher), le programme te le signale et t'explique quoi faire.

<!-- en -->

**New**
- The app is now available in English (it follows your Windows language; can be changed in the menu).
- "My stats" tab: win rate, streaks, MMR history, prediction accuracy, frequent teammates.
- The live probability can use match stats (shots, saves, demos) as soon as they prove useful on your own games.
- Beta versions: tick the option in the menu to get new features early.
- "Copy diagnostics" (menu or right-click on the icon): paste it into a GitHub issue to report a problem — no names,
  no game details.

**Improved**
- In exclusive fullscreen (where the overlay can't show), the app tells you and explains what to do.

## 1.0.5

**Nouveau**
- Après une mise à jour, un bandeau te prévient et le menu affiche les nouveautés de la version.

<!-- en -->

**New**
- After an update, a banner tells you and the menu shows what's new in the version.

## 1.0.4

**Nouveau**
- Comme BakkesMod, tu lances Prédiction RL toi-même avant de jouer : il ne démarre plus avec Windows
  (option toujours disponible dans le menu).
- Icône à côté de l'horloge : clic pour ouvrir le menu, clic droit pour la page web, le démarrage avec Windows
  ou quitter. L'info-bulle indique si le jeu est détecté.

<!-- en -->

**New**
- Like BakkesMod, you launch Prédiction RL yourself before playing: it no longer starts with Windows (still
  available as an option in the menu).
- Icon next to the clock: click to open the menu, right-click for the web page, start with Windows, or quit.
  The tooltip shows whether the game is detected.

## 1.0.3

**Amélioré**
- Le programme réserve beaucoup moins de mémoire en fond (64 Mo au lieu de 740 Mo).

<!-- en -->

**Improved**
- The app reserves much less memory in the background (64 MB instead of 740 MB).

## 1.0.2

**Corrigé**
- Le programme répond dès son lancement, même si le reste de son démarrage prend du temps.
- Il continue de fonctionner si l'overlay ne peut pas s'afficher.

<!-- en -->

**Fixed**
- The app responds as soon as it starts, even if the rest of its startup takes time.
- It keeps working if the overlay can't be shown.

## 1.0.1

- Première version publique : proba de victoire avant et pendant chaque match, overlay, menu, mises à jour
  automatiques.

<!-- en -->

- First public version: win probability before and during each match, overlay, menu, automatic updates.
