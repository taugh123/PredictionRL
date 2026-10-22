<p align="center"><img src="assets/icone.png" width="96" alt=""></p>

# Prédiction RL

**Français** · [English](README.en.md)

**Ta probabilité de gagner, en direct, dans Rocket League.** Gratuit, sans compte, sans publicité.

Au coup d'envoi de chaque partie, Prédiction RL lit les joueurs du match, récupère leurs stats sur tracker.gg et
calcule ta chance de victoire. Pendant le match, la proba évolue avec le score et le chrono, affichée par-dessus le
jeu. À la fin, le résultat est noté tout seul et le modèle apprend de tes games.

> Projet de fan non officiel, **non affilié à Psyonix, Epic Games ni Tracker Network**. Il utilise la
> [Stats API officielle](https://www.rocketleague.com/developer/stats-api) du jeu : rien n'est injecté dans
> Rocket League, aucun risque pour ton compte.

## Installation

1. Télécharge `PredictionRL-Setup-x.y.z.exe` dans les [Releases](../../releases/latest).
2. Lance-le. Windows peut afficher **« Windows a protégé votre ordinateur »** : le programme n'est pas signé
   (un certificat coûte de l'argent, comme pour beaucoup d'outils gratuits, BakkesMod compris). Clique sur
   **Informations complémentaires → Exécuter quand même**. Chaque version est construite automatiquement par
   GitHub et fournie avec son empreinte SHA-256 (`.sha256`, à côté de l'installateur) pour vérifier ton téléchargement.
3. C'est tout. Comme BakkesMod, **lance Prédiction RL avant de jouer** (raccourci sur le Bureau ou menu
   Démarrer) : son icône apparaît à côté de l'horloge, il attend Rocket League en fond et se met à jour tout seul
   (quand le jeu est fermé). Il peut aussi démarrer avec Windows (clic droit sur l'icône).

Au premier lancement, il active la Stats API du jeu (si Rocket League était ouvert, relance-le une fois) et
télécharge un navigateur Chromium invisible (~150 Mo) qui sert à lire tracker.gg.

## Utilisation

Lance Prédiction RL, puis une partie : rien d'autre à faire.

| | |
|---|---|
| **Icône près de l'horloge** | clic : menu ; clic droit : page web, démarrer avec Windows, aide, copier le diagnostic, quitter. L'info-bulle dit si le jeu est détecté. Windows 11 la range d'abord dans la flèche « ^ » : glisse-la dans la barre pour la garder visible |
| **Overlay** | proba en direct, score, avant-match et courbe, en haut à gauche pendant les matchs |
| **F2** (F3 si BakkesMod est installé) | menu : détail du match (joueurs, rangs, MMR, pourquoi), réglages, modèles, mises à jour, langue |
| **Ctrl+Maj+O** | masquer / afficher l'overlay |

**Mode d'affichage** : l'overlay et le menu s'affichent en **fenêtré** ou **plein écran fenêtré**. En plein écran
*exclusif*, Windows ne laisse aucune fenêtre passer devant le jeu : utilise alors l'overlay Steam
(**Maj+Tab** → navigateur web → `127.0.0.1:8765/overlay` → épingler la fenêtre), qui s'affiche en jeu.

Seules les parties **classées** (1v1, 2v2, 3v3) sont enregistrées et servent à l'entraînement ; les casual sont
prédites pour info. **Mes stats** (menu) : winrate, séries, évolution du MMR, justesse des prédictions, coéquipiers.

Le programme est en français ou en anglais (langue de Windows, modifiable dans le menu). Les **versions bêta**
(option du menu) donnent les nouveautés en avance.

## À quel point c'est fiable ?

Honnêtement :

- **Avant le match**, le facteur qui compte vraiment est l'**écart de MMR**. Le modèle teste à chaque entraînement
  s'il fait mieux en ajoutant d'autres facteurs (forme récente, peak, fatigue, heure…) et ne les utilise que si
  c'est le cas sur des games qu'il n'a jamais vues. Il faut plusieurs dizaines de games classées par mode.
- **Pendant le match**, la proba en direct (score + temps restant) est nettement plus précise que l'avant-match.
- Rocket League reste un jeu très aléatoire : à 70 %, tu perds encore 3 fois sur 10.

## Vie privée

Tout reste sur ton PC (`%APPDATA%\PredictionRL`) : historique, modèle, réglages. Aucune donnée n'est envoyée
ailleurs que les requêtes à tracker.gg (stats publiques des joueurs du match) et à GitHub (vérification des mises
à jour). Pas de compte, pas de télémétrie.

## Problèmes fréquents

- **Rien ne s'affiche** : es-tu en plein écran exclusif ? (voir *Mode d'affichage*). Sinon, regarde le journal :
  `%APPDATA%\PredictionRL\journal.log`.
- **« Rocket League non détecté »** après une mise à jour du jeu : le programme réactive la Stats API tout seul ;
  relance Rocket League.
- **Prédiction impossible** : tracker.gg peut être lent ou bloquer temporairement ; la proba en direct marche quand même.
- **Signaler un problème** : clic droit sur l'icône → « Copier le diagnostic », puis ouvre un
  [ticket](../../issues/new/choose) et colle-le.
- **Désinstaller** : Paramètres Windows → Applications → Prédiction RL. Tes données restent dans
  `%APPDATA%\PredictionRL` (supprime le dossier pour tout effacer).

## Licence

Gratuit, voir [LICENSE](LICENSE). « Rocket League » est une marque de Psyonix LLC.
