"""Annonce une version dans le salon #annonces du Discord de la communauté, avec ses notes (français puis anglais).

Ce fichier est autonome (bibliothèque standard seulement) : il est copié dans le dépôt PUBLIC (.github/scripts/) par release.yml,
et c'est le workflow annonce-discord.yml de ce dépôt public qui le lance quand une release y est publiée (les minutes de
GitHub Actions y sont gratuites, et rien du programme n'y est lu : seulement le texte de la release).

    python annoncer_discord.py          (tout vient de variables d'environnement)

  DISCORD_ANNONCES_WEBHOOK   secret : l'adresse du webhook de #annonces
  TAG, NOTES, URL, PRERELEASE   la release : son tag (v1.2.1), son texte, son adresse, "true" pour une bêta
  SITE_URL (facultatif)      https://domaine : ajoute les liens vers le site
  DISCORD_ROLE_VERSIONS (facultatif)   identifiant du rôle « Notifications de versions », prévenu par l'annonce

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
LIMITE_DESCRIPTION = 3800      # un embed accepte 4096 caractères : on garde de la marge pour la coupe


def analyser(notes):
    """Texte d'une release -> (français, anglais ou None). Le pied de page « Télécharge… » (après ---) est retiré."""
    notes = (notes or "").replace("\r\n", "\n").split("\n---\n")[0].strip()
    francais, _, anglais = notes.partition(SEPARATEUR_ANGLAIS)
    return francais.strip(), anglais.strip() or None


def couper(texte, lien):
    if len(texte) <= LIMITE_DESCRIPTION:
        return texte
    suite = f"[Tout lire / Read more]({lien})" if lien else "…"
    return texte[:LIMITE_DESCRIPTION].rsplit("\n", 1)[0] + "\n…\n" + suite


def charge(version, fr, en, lien, site=None, role=None):
    adresse = {"url": lien} if lien else {}
    embeds = [{"title": f"Prédiction RL {version} est disponible", **adresse, "color": 0x4C8DFF, "description": couper(fr, lien)}]
    if en:
        embeds.append({"title": f"Prédiction RL {version} is out", **adresse, "color": 0x2FBF71, "description": couper(en, lien)})
    contenu = ("Le programme se met à jour tout seul quand Rocket League est fermé. · "
               "The program updates itself when Rocket League is closed.")
    if site:     # liens vers le site : télécharger à la main, lire la documentation, toutes les nouveautés
        contenu += (f"\n**[Télécharger / Download]({site}/)** · [Documentation]({site}/documentation.html) · "
                    f"[Nouveautés / What's new]({site}/nouveautes.html)")
    mentions = {"parse": []}
    if role:      # le rôle « Notifications de versions » n'est pas mentionnable par les membres : seul ce message le prévient
        contenu, mentions = f"<@&{role}> {contenu}", {"parse": [], "roles": [role]}
    return {"content": contenu, "embeds": embeds, "allowed_mentions": mentions}


def envoyer(webhook, donnees, ouvrir=urllib.request.urlopen):
    requete = urllib.request.Request(webhook, data=json.dumps(donnees).encode("utf-8"), method="POST",
                                     headers={"Content-Type": "application/json", "User-Agent": "PredictionRL-annonces"})
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
    try:
        envoyer(webhook, charge(version, fr, en, lien, site or None, role or None), ouvrir)
    except (urllib.error.URLError, OSError, ValueError) as e:        # jamais l'adresse du webhook dans le message
        print(f"Annonce Discord non envoyée : {type(e).__name__}.")
        return 0
    print(f"Annonce Discord envoyée pour {version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
