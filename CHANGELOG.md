# Nouveautés / What's new

Chaque version publiée a sa section ici. Elle sert à la fois de notes de version sur GitHub et de page
« Nouveautés » dans le programme. Écrite pour les joueurs : ce qui change pour eux, pas le détail technique.
La partie anglaise de chaque section vient après la ligne `<!-- en -->`.

## 1.2.1

**Nouveau**
- La proba en direct réagit aux occasions. Sur une belle occasion (balle frappée fort vers le but, tir, défense adverse
  sortie ou débordée, adversaires qui n'arrivent plus à dégager), elle monte pendant quelques secondes, puis retombe si
  rien ne se passe. Elle s'apprend sur tes propres parties et n'est utilisée que si elle rend la proba au moins aussi juste.

**Amélioré**
- Le menu (F2) se déplace : tire son en-tête avec la souris. Un double-clic sur l'en-tête le remet au centre.
- Le menu se redimensionne avec la poignée en bas à droite, et son contenu défile à la molette quand il est plus grand
  que l'écran. Il garde sa place et sa taille tant que le programme tourne.

**Retiré**
- La page web du programme (adresse 127.0.0.1:8765) n'existe plus : elle ne servait pas en jeu. Les boutons « Historique
  complet (page web) » et « Mes stats » disparaissent du menu et de l'icône près de l'horloge. L'overlay Steam
  (127.0.0.1:8765/overlay) continue de fonctionner. Tes données et ton historique ne changent pas.

**Corrigé**
- Juste après un but, le score affiché pouvait compter un but de trop (ou à la mauvaise équipe) pendant le replay.
- Après un but en or, il arrivait que le match ne soit pas clos et que la suite soit prise pour le même match.

<!-- en -->

**New**
- The live probability reacts to scoring chances. On a good chance (ball hit hard towards goal, a shot, an opposing
  defence pulled out or overrun, opponents who can no longer clear), it goes up for a few seconds, then drops back if
  nothing happens. It is learned from your own matches and only used if it keeps the probability at least as accurate.

**Improved**
- The menu (F2) can be moved: drag its header with the mouse. A double-click on the header puts it back in the middle.
- The menu can be resized with the handle at the bottom right, and its content scrolls with the mouse wheel when it is
  taller than the screen. It keeps its place and size while the program runs.

**Removed**
- The program's web page (address 127.0.0.1:8765) is gone: it was not useful in game. The "Full history (web page)" and
  "My stats" buttons disappear from the menu and from the icon next to the clock. The Steam overlay page
  (127.0.0.1:8765/overlay) still works. Your data and history do not change.

**Fixed**
- Right after a goal, the displayed score could count one goal too many (or for the wrong team) during the replay.
- After a golden goal, the match was sometimes not closed and what followed was taken for the same match.

## 1.2.0

**Amélioré**
- Sécurité des mises à jour : le programme n'installe plus que des versions authentifiées comme venant bien de Prédiction RL.
  Une version modifiée par quelqu'un d'autre est refusée, même si elle est publiée à la place de la vraie.
- Le programme est reconstruit pour être plus difficile à copier ou à modifier. Rien ne change pour toi à l'utilisation,
  et tes données restent sur ton PC.
- L'installateur et les propriétés du fichier n'indiquent plus « open source » : le code n'est plus publié depuis la 1.1.2.

**Corrigé**
- Les fichiers de mise à jour téléchargés sont désormais rangés dans un dossier temporaire réservé à ton compte Windows.

<!-- en -->

**Improved**
- Update security: the app now only installs versions that are verified as coming from Prédiction RL. A version modified by
  someone else is refused, even if it is published in place of the real one.
- The app has been rebuilt to be harder to copy or modify. Nothing changes for you when using it, and your data stays
  on your PC.
- The installer and the file properties no longer say "open source": the code has not been published since 1.1.2.

**Fixed**
- Downloaded update files are now stored in a temporary folder reserved for your Windows account.

## 1.1.3

**Amélioré**
- Cette version change l'adresse où le programme cherche ses mises à jour. Installe-la pour continuer à recevoir les
  prochaines versions. Rien ne change pour toi à l'utilisation, et tes données restent sur ton PC.

<!-- en -->

**Improved**
- This version changes the address the app checks for updates. Install it to keep receiving future versions. Nothing
  changes for you when using it, and your data stays on your PC.

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
