import re

from urllib.parse import urlparse, parse_qs, unquote

from playwright.sync_api import TimeoutError



def nettoyer_url(url):

        if url is None:
            return ""

        if "youtube.com/redirect" not in url:
            return url

        query = parse_qs(urlparse(url).query)

        if "q" not in query:
            return url

        return unquote(query["q"][0])


def classer_liens(liens, youtube_channel):

        for lien in liens:

            url = lien.lower()

            if "twitter.com" in url or "x.com" in url:

                youtube_channel.twitter = lien

            elif "facebook.com" in url:

                youtube_channel.facebook = lien

            elif "spotify.com" in url:

                youtube_channel.spotify = lien

            elif "whatsapp.com" in url:

                youtube_channel.whatsapp = lien

            elif "instagram.com" in url:

                youtube_channel.instagram = lien

            elif "tiktok.com" in url:

                youtube_channel.tiktok = lien

            elif "discord.gg" in url or "discord.com" in url:

                youtube_channel.discord = lien

            elif "twitch.tv" in url:

                youtube_channel.twitch = lien

            else:

                if youtube_channel.website == "":
                    youtube_channel.website = lien
                else:
                    if youtube_channel.autres_liens == "":
                        youtube_channel.autres_liens = lien
                    else:
                        youtube_channel.autres_liens += "\n" + lien


def ouvrir_panneau_liens(page):

        print()
        print("=" * 80)
        print("Ouverture du panneau")
        print("=" * 80)

        try:

            page.get_by_role("button",name=re.compile("Afficher plus|Show more")).click(timeout=3000)

            page.wait_for_timeout(1000)

            popup = page.locator("tp-yt-paper-dialog")

            print()
            print("=" * 80)
            print("CONTENU DE LA POPUP")
            print("=" * 80)

            print(popup.inner_text())

            print("Panneau ouvert.")

        except TimeoutError:

            print("Impossible d'ouvrir le panneau.")

            return False

        elements = page.locator("yt-channel-external-link-view-model")

        print()
        print("Nombre de blocs :", elements.count())

        for i in range(elements.count()):

            print("=" * 60)
            print(elements.nth(i).inner_text())

        return True

def recuperer_liens(page):

        print()
        print("=" * 80)
        print("Récupération des liens")
        print("=" * 80)

        liens = page.locator("yt-channel-external-link-view-model a")

        print("Nombre de liens :", liens.count())

        liste_liens = []

        for i in range(liens.count()):

            lien = liens.nth(i).get_attribute("href")

            lien = nettoyer_url(lien)

            print(lien)

            liste_liens.append(lien)

        return liste_liens

def remplir_liens(page, youtube_channel):

        if not ouvrir_panneau_liens(page):
            return

        liens = recuperer_liens(page)

        classer_liens(
            liens,
            youtube_channel)