"""Annonce une version dans le salon #announcements du Discord de la communauté, avec ses notes (français puis anglais).

Ce fichier est autonome (bibliothèque standard seulement) : il est copié dans le dépôt PUBLIC (.github/scripts/) par
release_locale.ps1, AVANT la création de la release, et c'est le workflow annonce-discord.yml de ce dépôt public qui le lance
quand la release y est publiée (les minutes de GitHub Actions y sont gratuites, et rien du programme n'y est lu : seulement le
texte de la release).

    python annoncer_discord.py          (tout vient de variables d'environnement)

  DISCORD_ANNONCES_WEBHOOK   secret : l'adresse du webhook de #announcements
  TAG, NOTES, URL, PRERELEASE   la release : son tag (v1.2.1), son texte, son adresse, "true" pour une bêta
  SITE_URL (facultatif)      https://domaine : ajoute les boutons vers le site
  DISCORD_ROLE_VERSIONS (facultatif)   identifiant du rôle « Notifications de versions », prévenu par l'annonce
  GITHUB_REPOSITORY, GITHUB_SHA   donnés par GitHub Actions : la bannière est lue dans ce commit du dépôt public

Le message suit l'habillage du serveur (13/11/2026) : un cadre « composants V2 » de Discord avec la bannière NOUVEAUTÉS
(assets/banniere-nouveautes.png du dépôt public), un titre, les notes en français et en anglais, puis des boutons. Sans bannière
(fichier absent, GitHub injoignable), l'annonce part quand même, sans image.

Ne bloque JAMAIS une release : sans webhook, pour une version bêta ou si Discord ne répond pas, il le dit et sort sans erreur.
Le webhook est un secret : il n'est jamais affiché, ni dans les messages ni dans les erreurs.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

WEBHOOK = re.compile(r"https://discord\.com/api/webhooks/[0-9]+/[A-Za-z0-9_-]+")
SITE = re.compile(r"https://[A-Za-z0-9.-]+(:[0-9]{1,5})?")
SEPARATEUR_ANGLAIS = "\n**English**\n"
# un message en composants V2 accepte 4000 caractères de texte EN TOUT : 1600 par langue laisse la place du titre et de la mention
LIMITE_DESCRIPTION = 1600
COMPOSANTS_V2 = 1 << 15
ORANGE = 0xFF8A3D
BANNIERE = "assets/banniere-nouveautes.png"
AGENT = "PredictionRL-annonces"


def analyser(notes):
    """Texte d'une release -> (français, anglais ou None). Le pied de page « Installateur… » (après ---) est retiré."""
    notes = (notes or "").replace("\r\n", "\n").split("\n---\n")[0].strip()
    francais, _, anglais = notes.partition(SEPARATEUR_ANGLAIS)
    return francais.strip(), anglais.strip() or None


def couper(texte, lien):
    if len(texte) <= LIMITE_DESCRIPTION:
        return texte
    suite = f"[Tout lire / Read more]({lien})" if lien else "…"
    return texte[:LIMITE_DESCRIPTION].rsplit("\n", 1)[0] + "\n…\n" + suite


def charge(version, fr, en, lien, site=None, role=None, banniere=None):
    """Le message : un cadre orange (bannière, titre, notes FR puis EN, boutons). Jamais de mention hors du rôle donné."""
    def texte(contenu):
        return {"type": 10, "content": contenu}

    def trait():
        return {"type": 14, "divider": True, "spacing": 1}

    def bouton(libelle, adresse):
        return {"type": 2, "style": 5, "label": libelle, "url": adresse}

    titre = (f"## Prédiction RL {version} est sortie\n"
             "Le programme s'installe tout seul dès que Rocket League est fermé. "
             "*(The program updates itself as soon as Rocket League is closed.)*")
    if role:      # le rôle « Notifications de versions » n'est pas mentionnable par les membres : seul ce message le prévient
        titre = f"<@&{role}>\n{titre}"
    cadre = ([{"type": 12, "items": [{"media": {"url": banniere}}]}] if banniere else []) + [texte(titre), trait(),
             texte("### Nouveautés\n" + couper(fr, lien))]
    if en:
        cadre += [trait(), texte("### What's new\n" + couper(en, lien))]
    boutons = []
    if site:     # télécharger à la main, toutes les nouveautés, la documentation
        boutons += [bouton("Télécharger · Download", f"{site}/"), bouton("Nouveautés · What's new", f"{site}/nouveautes.html"),
                    bouton("Documentation", f"{site}/documentation.html")]
    if lien:
        boutons.append(bouton("Notes sur GitHub", lien))
    if boutons:
        cadre.append({"type": 1, "components": boutons})
    mentions = {"parse": [], "roles": [role]} if role else {"parse": []}
    return {"flags": COMPOSANTS_V2, "components": [{"type": 17, "accent_color": ORANGE, "components": cadre}],
            "allowed_mentions": mentions}


def adresse_banniere(env, ouvrir=urllib.request.urlopen):
    """L'adresse de la bannière dans le commit de la release (dépôt public), si elle y est ; sinon None : l'annonce part sans image."""
    depot, commit = env.get("GITHUB_REPOSITORY", "").strip(), env.get("GITHUB_SHA", "").strip()
    if not (re.fullmatch(r"[A-Za-z0-9._-]+/[A-Za-z0-9._-]+", depot) and re.fullmatch(r"[0-9a-f]{40}", commit)):
        return None
    adresse = f"https://raw.githubusercontent.com/{depot}/{commit}/{BANNIERE}"
    try:
        with ouvrir(urllib.request.Request(adresse, method="HEAD", headers={"User-Agent": AGENT}), timeout=10) as reponse:
            return adresse if reponse.status == 200 else None
    except (urllib.error.URLError, OSError, ValueError):
        return None


def envoyer(webhook, donnees, ouvrir=urllib.request.urlopen):
    # « with_components » : sans lui, Discord refuse les composants d'un webhook qui n'appartient pas à une application.
    # « wait » : Discord répond seulement une fois le message créé (ou refusé) ; sans lui, il a déjà répondu 204 sans que le message
    # n'apparaisse (essai du 13/11/2026)
    requete = urllib.request.Request(webhook + "?with_components=true&wait=true", data=json.dumps(donnees).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "User-Agent": AGENT})
    with ouvrir(requete, timeout=20) as reponse:
        return reponse.status


def main(env=None, ouvrir=urllib.request.urlopen):
    env = os.environ if env is None else env
    webhook = env.get("DISCORD_ANNONCES_WEBHOOK", "").strip()
    if not webhook:
        print("Annonce Discord ignorée : DISCORD_ANNONCES_WEBHOOK n'est pas défini.")
        return 0
    if not WEBHOOK.fullmatch(webhook):
        print("Annonce Discord ignorée : DISCORD_ANNONCES_WEBHOOK n'est pas une adresse de webhook Discord.")
        return 0
    version = env.get("TAG", "").strip().lstrip("v")
    if not re.fullmatch(r"[0-9]+(\.[0-9]+)*(-[0-9A-Za-z.]+)?", version):
        print("Annonce Discord ignorée : TAG n'est pas un numéro de version.")
        return 0
    if env.get("PRERELEASE", "").lower() == "true" or "-" in version:
        print(f"Annonce Discord ignorée : {version} est une version bêta.")
        return 0
    fr, en = analyser(env.get("NOTES"))
    if not fr:
        print(f"Annonce Discord ignorée : pas de notes pour {version}.")
        return 0
    lien = env.get("URL", "").strip()
    if not re.fullmatch(r"https://github\.com/[A-Za-z0-9._-]+/[A-Za-z0-9._-]+/releases/tag/[A-Za-z0-9._-]+", lien):
        lien = None
    site = env.get("SITE_URL", "").strip().rstrip("/")
    if site and not SITE.fullmatch(site):
        print("Adresse du site ignorée dans l'annonce : SITE_URL doit être de la forme https://domaine.")
        site = None
    role = env.get("DISCORD_ROLE_VERSIONS", "").strip()
    if role and not role.isdigit():
        print("Rôle ignoré dans l'annonce : DISCORD_ROLE_VERSIONS doit être un identifiant numérique.")
        role = None
    banniere = adresse_banniere(env, ouvrir)
    if not banniere:
        print(f"Bannière introuvable ({BANNIERE}) : l'annonce part sans image.")
    try:
        envoyer(webhook, charge(version, fr, en, lien, site or None, role or None, banniere), ouvrir)
    except (urllib.error.URLError, OSError, ValueError) as e:        # jamais l'adresse du webhook dans le message
        print(f"Annonce Discord non envoyée : {type(e).__name__}.")
        return 0
    print(f"Annonce Discord envoyée pour {version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
