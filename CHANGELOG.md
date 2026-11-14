# Nouveautés / What's new

Chaque version publiée a sa section ici. Elle sert à la fois de notes de version sur GitHub et de page
« Nouveautés » dans le programme. Écrite pour les joueurs : ce qui change pour eux, pas le détail technique.
Neutre, en français comme en anglais (ni « tu », ni « vous », ni « you » : un test le garde) et courte : une puce, une ligne.
La partie anglaise de chaque section vient après la ligne `<!-- en -->`.

## 1.3.4

**Amélioré**
- Nouveau logo dans le menu (F2) et nouvelles images dans l'installateur.
- Nouvelle icône, avec la pastille « RL » rose et orange du nouveau logo.
- Pendant le match, la probabilité réagit de nouveau aux occasions et à la pression, pas seulement aux buts.
- Jeu en plein écran exclusif : une notification Windows explique pourquoi l'anneau et le menu ne s'affichent pas.

**Corrigé**
- Menu (F2) en anglais : les interrupteurs affichent « On » et « Off » au lieu de « Activé » et « Désactivé ».
- Quand tracker.gg limite les demandes, la prédiction patiente puis estime le MMR au lieu d'être perdue.
- Un bot présent au début du match (joueur qui charge encore) ne bloque plus la prédiction pour toute la partie.
- Le match qui suit un podium n'est plus ignoré : l'anneau et la prédiction s'affichent de nouveau.

<!-- en -->

**Improved**
- New logo in the menu (F2) and new images in the installer.
- New icon, with the pink and orange “RL” badge of the new logo.
- During the match, the probability reacts again to chances and pressure, not only to goals.
- Game in exclusive fullscreen: a Windows notification explains why the ring and the menu do not show.

**Fixed**
- Menu (F2) in English: the switches show “On” and “Off” instead of “Activé” and “Désactivé”.
- When tracker.gg limits requests, the prediction waits, then estimates the MMR instead of being lost.
- A bot present at the start of the match (a player still loading) no longer blocks the prediction for the whole game.
- The match after a podium is no longer ignored: the ring and the prediction show again.

## 1.3.3

**Amélioré**
- Nouvelle icône : l'anneau de probabilité autour du badge « RL », nette aussi près de l'horloge.

<!-- en -->

**Improved**
- New icon: the probability ring around the “RL” badge, sharp in the notification area too.

## 1.3.2

**Corrigé**
- Menu en anglais : les titres des colonnes, l'onglet Prédiction et les paliers d'entraînement restaient en français.

<!-- en -->

**Fixed**
- English menu: the column titles, the Prediction tab and the training stages were shown in French.

## 1.3.1

**Sécurité**
- Le navigateur qui lit tracker.gg tourne dans un bac à sable, ne charge que tracker.gg et se met à jour avec le programme.
- Le diagnostic ne contient plus le nom de session Windows, le nom du PC ni les pseudos des autres joueurs.
- Aucun site ne peut afficher la page de l'overlay Steam dans un cadre caché.
- Les enregistrements de matchs de plus de 6 mois sont effacés (ils gardaient les pseudos des autres joueurs).

**Corrigé**
- L'historique des parties ne peut plus être vidé par un arrêt brutal du PC ; une ligne abîmée ne le bloque plus.
- Un adversaire au même pseudo sur une autre plateforme n'est plus pris pour le joueur (caméra du coup d'envoi).
- Après une bêta, c'est la version finale du même numéro qui s'installe.
- Les anciens installateurs ne s'accumulent plus dans le dossier temporaire ; les stats tracker.gg périmées sont effacées.
- Un pseudo contenant « @ » est lu en entier.

<!-- en -->

**Security**
- The invisible browser that reads tracker.gg runs in a sandbox, only loads tracker.gg and updates with the program.
- Diagnostics pasted into an issue no longer contain the Windows session name, the PC name or other players' usernames.
- No website can show the Steam overlay page in a hidden frame anymore.
- Match recordings older than 6 months are deleted: they kept other players' usernames.

**Fixed**
- Match history can no longer be wiped by an abrupt PC shutdown; a damaged line no longer makes it unreadable.
- An opponent with the same username on another platform is no longer taken for the player (kickoff camera).
- After a beta, the final version with the same number installs, not the beta.
- Old installers no longer pile up in Windows' temporary folder; expired tracker.gg stats are deleted.
- A username that contains "@" is read in full.

## 1.3.0

**Nouveau**
- Nouvel overlay : la proba dans un anneau net, aux couleurs de Rocket League, avec la raison du moment dessous.
- « Placer » (menu F2, onglet Overlay) : 9 zones de l'écran pour l'anneau, la molette règle sa taille.
- Au choix sous l'anneau : score et chrono, proba avant-match, barre de pression, courbe.
- Les messages du programme s'affichent dans une petite bulle en haut à gauche, qui disparaît seule.
- Mises à jour automatiques désactivées : un bouton cherche une version, un autre l'installe.

**Amélioré**
- Menu F2 refait aux couleurs de Rocket League : quatre onglets, réglages à flèches « ‹ › », page Match façon score télé.
- Le changement de langue s'applique à la prochaine ouverture du menu, sans relancer le programme.

<!-- en -->

**New**
- New overlay: the win chance in a sharp ring, in Rocket League's colors, with the reason of the moment below.
- “Place” (F2 menu, Overlay tab): 9 screen zones for the ring, the mouse wheel sets its size.
- Optional under the ring: score and clock, pre-match chance, pressure bar, win chance curve.
- Program messages show in a small bubble at the top left, which goes away on its own.
- Automatic updates turned off: one button checks for a new version, another installs it.

**Improved**
- F2 menu redesigned in Rocket League's colors: four tabs, “‹ ›” arrows for settings, a TV-scoreboard Match page.
- Changing the language applies the next time the menu opens, without restarting the program.

## 1.2.3

**Amélioré**
- Version d'entretien, sans nouveauté en jeu : le compilateur et le navigateur de tracker.gg sont mis à jour.

<!-- en -->

**Improved**
- Maintenance release, nothing new in game: the compiler and the tracker.gg browser were updated.

## 1.2.2

**Nouveau**
- Barre « pression » sur l'overlay : verte vers la droite quand l'équipe presse, rouge vers la gauche sinon.
- « OCCASION ! » ou « DANGER ! » quand un but est possible, avec l'effet sur la proba (« +4% », « -3% »).
- La barre se masque dans le menu (F2).

**Amélioré**
- La proba en direct suit la pression d'une équipe sur une vingtaine de secondes : tirs, arrêts, démos, dégagements ratés.
- Le modèle est appris sur les parties jouées.

<!-- en -->

**New**
- A “pressure” bar on the overlay: green to the right when the team is pressing, red to the left when the opponents are.
- “CHANCE!” or “DANGER!” when a goal is possible, with the effect on the probability (“+4%”, “-3%”).
- The bar can be hidden in the menu (F2).

**Improved**
- The live probability follows one team's pressure over about twenty seconds: shots, saves, demos, failed clears.
- The model is learned from the matches played.

## 1.2.1

**Nouveau**
- La proba en direct réagit aux occasions : elle monte sur une belle occasion, puis retombe si rien ne se passe.
- Apprise sur les parties jouées, elle n'est utilisée que si elle rend la proba au moins aussi juste.

**Amélioré**
- Le menu (F2) se déplace (tirer l'en-tête, double-clic pour recentrer) et se redimensionne (poignée en bas à droite).
- Son contenu défile à la molette ; position et taille sont gardées tant que le programme tourne.

**Retiré**
- La page web du programme (127.0.0.1:8765) n'existe plus ; l'overlay Steam continue de fonctionner.
- Les boutons « Historique complet (page web) » et « Mes stats » disparaissent ; données et historique inchangés.

**Corrigé**
- Après un but, le score affiché pouvait compter un but de trop (ou à la mauvaise équipe) pendant le replay.
- Après un but en or, le match pouvait ne pas être clos et la suite être prise pour le même match.

<!-- en -->

**New**
- The live probability reacts to scoring chances: it goes up on a good chance, then drops back if nothing happens.
- Learned from the matches played, it is only used if it keeps the probability at least as accurate.

**Improved**
- The F2 menu can be moved (drag its header, double-click to re-center) and resized (handle at the bottom right).
- Its content scrolls with the mouse wheel; position and size are kept while the program runs.

**Removed**
- The program's web page (127.0.0.1:8765) is gone; the Steam overlay page still works.
- The "Full history (web page)" and "My stats" buttons disappear; data and history are unchanged.

**Fixed**
- Right after a goal, the displayed score could count one goal too many (or for the wrong team) during the replay.
- After a golden goal, the match was sometimes not closed and what followed was taken for the same match.

## 1.2.0

**Amélioré**
- Mises à jour authentifiées : seules les versions venant bien de Prédiction RL s'installent.
- Programme reconstruit pour être plus difficile à copier ou à modifier ; rien ne change à l'usage.
- L'installateur n'indique plus « open source » : le code n'est plus publié depuis la 1.1.2.

**Corrigé**
- Les fichiers de mise à jour téléchargés sont rangés dans un dossier temporaire réservé au compte Windows.

<!-- en -->

**Improved**
- Verified updates: only versions coming from Prédiction RL are installed.
- The app is rebuilt to be harder to copy or modify; nothing changes in use.
- The installer no longer says "open source": the code has not been published since 1.1.2.

**Fixed**
- Downloaded update files are stored in a temporary folder reserved for the Windows account.

## 1.1.3

**Amélioré**
- Nouvelle adresse pour les mises à jour : cette version est à installer pour recevoir les suivantes.
- Rien ne change à l'usage ; les données restent sur le PC.

<!-- en -->

**Improved**
- New address for updates: this version has to be installed to receive future ones.
- Nothing changes in use; data stays on the PC.

## 1.1.2

**Amélioré**
- Le programme reste gratuit, mais son code n'est plus publié (versions jusqu'à la 1.1.1 sous licence MIT).
- Rien ne change à l'usage ; les données restent sur le PC.

<!-- en -->

**Improved**
- The app stays free, but its source code is no longer published (versions up to 1.1.1 remain under the MIT license).
- Nothing changes in use; data stays on the PC.

## 1.1.1

**Corrigé**
- Menu : les choix (position, taille, opacité, langue, proba en direct) affichent l'option sélectionnée.
- Sécurité : la page locale refuse les requêtes d'autres sites, même déguisées (« DNS rebinding »).
- Une capture de match abîmée ne bloque plus l'entraînement de la proba en direct.

**Fiabilité**
- Chaque version est vérifiée avant sa sortie : 176 tests couvrant 100 % du code, analyse de sécurité.

<!-- en -->

**Fixed**
- Menu: choices (position, size, opacity, language, live probability) show the selected option.
- Security: the local page rejects requests from other websites, even disguised ones ("DNS rebinding").
- A damaged match capture no longer blocks training of the live probability.

**Reliability**
- Every version is checked before release: 176 automated tests covering 100% of the code, plus a security scan.

## 1.1.0

**Nouveau**
- Le programme existe en anglais (langue de Windows par défaut, modifiable dans le menu).
- Onglet « Mes stats » : winrate, séries, évolution du MMR, justesse des prédictions, coéquipiers fréquents.
- La proba en direct peut tenir compte des stats du match (tirs, arrêts, démos) quand elles se montrent utiles.
- Versions bêta : une option du menu donne accès aux nouveautés en avance.
- « Copier le diagnostic » (menu ou clic droit sur l'icône) : à coller dans un ticket, sans pseudo ni détail des parties.

**Amélioré**
- En plein écran exclusif (overlay impossible), le programme le signale et explique quoi faire.

<!-- en -->

**New**
- The app is available in English (it follows the Windows language; can be changed in the menu).
- "My stats" tab: win rate, streaks, MMR history, prediction accuracy, frequent teammates.
- The live probability can use match stats (shots, saves, demos) once they prove useful on the matches played.
- Beta versions: an option in the menu gives early access to new features.
- "Copy diagnostics" (menu or right-click on the icon): to paste into an issue, with no names or game details.

**Improved**
- In exclusive fullscreen (overlay impossible), the app says so and explains what to do.

## 1.0.5

**Nouveau**
- Après une mise à jour, un bandeau prévient et le menu affiche les nouveautés de la version.

<!-- en -->

**New**
- After an update, a banner announces it and the menu shows what's new in the version.

## 1.0.4

**Nouveau**
- Comme BakkesMod, le programme se lance à la main avant de jouer ; le démarrage avec Windows reste en option.
- Icône près de l'horloge : clic pour le menu, clic droit pour la page web, le démarrage et quitter.
- L'info-bulle de l'icône indique si le jeu est détecté.

<!-- en -->

**New**
- Like BakkesMod, the program is launched by hand before playing; starting with Windows remains an option.
- Icon next to the clock: click to open the menu, right-click for the web page, start with Windows, or quit.
- The icon's tooltip shows whether the game is detected.

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

- Première version publique : proba de victoire, overlay, menu, mises à jour automatiques.

<!-- en -->

- First public version: win probability before and during each match, overlay, menu, automatic updates.
