# Nouveautés / What's new

Chaque version publiée a sa section ici. Elle sert à la fois de notes de version sur GitHub et de page
« Nouveautés » dans le programme. Écrite pour les joueurs : ce qui change pour eux, pas le détail technique.
La partie anglaise de chaque section vient après la ligne `<!-- en -->`.

## 1.3.1

**Sécurité**
- Le navigateur invisible qui lit tracker.gg tourne maintenant dans son bac à sable, et il ne charge plus que tracker.gg :
  ni publicités, ni scripts d'autres sites. Il se met aussi à jour avec le programme, au lieu de garder la version de son
  premier téléchargement.
- Le diagnostic à coller dans un ticket ne contient plus ton nom de session Windows, le nom de ton PC, ni les pseudos des
  autres joueurs.
- Aucun site ne peut plus afficher la page de l'overlay Steam dans un cadre caché pour te faire cliquer dessus.
- Les enregistrements de tes matchs de plus de 6 mois sont effacés : ils gardaient les pseudos des autres joueurs.

**Corrigé**
- Ton historique de parties ne peut plus être vidé par un arrêt brutal du PC pendant qu'il est enregistré, et une ligne
  abîmée ne le rend plus illisible.
- Quand un adversaire porte le même pseudo que toi sur une autre plateforme, le programme ne le prend plus pour toi : il te
  reconnaît grâce à la caméra du coup d'envoi.
- Après une version bêta, c'est bien la version finale du même numéro qui s'installe, et non la bêta.
- Les installateurs des mises à jour précédentes ne s'accumulent plus dans le dossier temporaire de Windows, et les stats
  de tracker.gg gardées sur ton PC s'effacent une fois périmées.
- Un pseudo qui contient « @ » est lu en entier.

<!-- en -->

**Security**
- The invisible browser that reads tracker.gg now runs in its sandbox and only loads tracker.gg: no ads, no scripts from
  other sites. It also updates along with the program, instead of keeping the version from its first download.
- The diagnostics you paste into an issue no longer contain your Windows session name, your PC's name or the usernames of
  other players.
- No website can show the Steam overlay page in a hidden frame to make you click on it anymore.
- Recordings of your matches older than 6 months are deleted: they kept the usernames of other players.

**Fixed**
- Your match history can no longer be wiped by the PC shutting down abruptly while it is being saved, and a damaged line no
  longer makes it unreadable.
- When an opponent has the same username as you on another platform, the program no longer takes them for you: it recognizes
  you with the kickoff camera.
- After a beta version, the final version with the same number is the one that installs, not the beta.
- Installers from previous updates no longer pile up in Windows' temporary folder, and the tracker.gg stats kept on your
  PC are deleted once they expire.
- A username that contains "@" is read in full.

## 1.3.0

**Nouveau**
- Nouvel overlay : ta proba dans un anneau, net sur le jeu (bords lissés, plus de cadre autour). Il prend les couleurs de
  Rocket League : ta couleur, bleu ou orange, quand c'est en ta faveur, celle d'en face sinon. Dessous, la raison du
  moment (« ▲ +4 % Tu presses », « ▼ –12 % Danger de but »).
- « Placer » (menu F2, onglet Overlay) : choisis l'une des 9 zones de l'écran pour l'anneau, la molette règle sa taille.
- Sous l'anneau, tu choisis ce que tu veux voir en plus : score et chrono, proba avant-match, barre de pression, courbe de
  la proba. Taille et opacité se règlent aussi dans le menu.
- Les messages du programme (lancement, mise à jour prête…) s'affichent dans une petite bulle en haut à gauche, qui
  disparaît seule.
- Mises à jour automatiques désactivées : un bouton cherche une nouvelle version à la demande, et un autre l'installe.

**Amélioré**
- Le menu (F2) est refait aux couleurs de Rocket League : quatre onglets (Match, Overlay, Prédiction, Application), et
  chaque réglage se change comme dans les menus du jeu, avec les flèches « ‹ › ». La page Match se lit comme un score
  télé : ta proba en grand, une barre partagée entre les deux équipes, les joueurs en colonnes.
- Changer la langue dans le menu s'applique dès sa prochaine ouverture, sans relancer le programme.

<!-- en -->

**New**
- New overlay: your win chance in a ring, sharp over the game (smooth edges, no box around it). It uses Rocket League's
  colors: your team's color, blue or orange, when things go your way, the other team's otherwise. Below it, the reason of
  the moment (“▲ +4% You're pressing”, “▼ –12% Goal danger”).
- “Place” (F2 menu, Overlay tab): pick one of the 9 screen zones for the ring, the mouse wheel sets its size.
- Under the ring, choose what else you want to see: score and clock, pre-match chance, pressure bar, win chance curve.
  Size and opacity can be set in the menu too.
- The program's messages (startup, update ready…) show in a small bubble at the top left, which goes away on its own.
- Automatic updates turned off: one button checks for a new version on demand, another installs it.

**Improved**
- The menu (F2) is redesigned in Rocket League's colors: four tabs (Match, Overlay, Prediction, Application), and every
  setting changes like in the game's menus, with the “‹ ›” arrows. The Match page reads like a TV scoreboard: your chance
  in big numbers, a bar shared between both teams, players in columns.
- Changing the language in the menu applies the next time it opens, without restarting the program.

## 1.2.3

**Amélioré**
- Version d'entretien : aucune nouveauté en jeu. Les composants internes du programme (le compilateur qui le fabrique et le
  navigateur qui lit tracker.gg) sont passés à leurs dernières versions correctives. Si tracker.gg ou la mise à jour
  automatique se comportaient bizarrement chez toi, cette version ne devrait rien changer, mais elle garde le programme à jour.

<!-- en -->

**Improved**
- Maintenance release: nothing new in game. The program's internal components (the compiler that builds it and the browser that
  reads tracker.gg) were moved to their latest fix versions. If tracker.gg or automatic updates ever misbehaved for you, this
  version should not change that, but it keeps the program up to date.

## 1.2.2

**Nouveau**
- Une barre « pression » sur l'overlay montre qui domine en ce moment : elle part vers la droite, en vert, quand ton équipe
  met la pression, vers la gauche, en rouge, quand c'est l'adversaire. « OCCASION ! » ou « DANGER ! » s'affiche quand une
  équipe a une vraie chance de marquer dans les secondes qui viennent, et « +4% » en vert ou « -3% » en rouge dit de combien
  la situation fait monter ou baisser ta proba. Elle se masque dans le menu (F2).

**Amélioré**
- La proba en direct suit maintenant la pression d'une équipe sur l'autre pendant une vingtaine de secondes, et plus
  seulement l'occasion du moment : quand une équipe enchaîne les tirs, les arrêts adverses, les démos ou que l'adversaire
  n'arrive plus à dégager, sa proba monte et celle d'en face baisse tant que ça dure. Appris sur tes propres parties.

<!-- en -->

**New**
- A “pressure” bar on the overlay shows who is on top right now: it grows to the right, in green, when your team is putting
  the pressure on, to the left, in red, when the opponents are. “CHANCE!” or “DANGER!” shows when a team has a real chance
  of scoring in the next few seconds, and “+4%” in green or “-3%” in red tells you how much the situation is raising or
  lowering your probability. It can be hidden in the menu (F2).

**Improved**
- The live probability now follows one team's pressure on the other over about twenty seconds, not just the chance of the
  moment: when a team keeps shooting, forcing saves, demolishing or the opponents can no longer clear the ball, its
  probability goes up and the other team's goes down for as long as it lasts. Learned from your own matches.

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
