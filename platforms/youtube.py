from utils import accepter_cookies_youtube

from parsers.youtube_channel_parser import parser_page_chaine

from playwright.sync_api import sync_playwright

from models import YoutubeChannel
from config import HEADLESS, TEMPS_CHARGEMENT, MAX_RESULTATS
from parsers.youtube_parsers import parser_chaine

from extractors.youtube_links import ouvrir_panneau_liens



def scraper_page_chaine(page, youtube_channel):

    if not youtube_channel.youtube_url:
        print("Pas de lien pour", youtube_channel.pseudo)
        return

    print(f"Visite de {youtube_channel.pseudo}")

    page.goto(youtube_channel.youtube_url)

    accepter_cookies_youtube(page)

    page.wait_for_load_state("networkidle")

    parser_page_chaine(page, youtube_channel)

    print()
    print(page.url)
    print(page.title())
    print()

    print("Retour à la recherche")


def rechercher_youtube(mot_cle):

    resultats = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=HEADLESS
        )

        search_page = browser.new_page()

        channel_page = browser.new_page()

        url = (
            f"https://www.youtube.com/results?"
            f"search_query={mot_cle}"
            f"&sp=EgIQAg%253D%253D"
        )

        print("Ouverture de YouTube...")

        search_page.goto(url)

        search_page.wait_for_load_state("networkidle")

        print(search_page.url)
        print(search_page.title())

        chaines = search_page.locator("ytd-channel-renderer")

        nombre_chaines = chaines.count()

        print(f"\n{chaines.count()} chaînes trouvées\n")

        nombre_resultats = min(chaines.count(), MAX_RESULTATS)

        for i in range(nombre_resultats):

            chaine = chaines.nth(i)

            print("=" * 80)

            elements = chaine.locator("yt-formatted-string")

            print("Nombre :", elements.count())

            for j in range(elements.count()):
                print(j, "->", elements.nth(j).inner_text())

            texte = chaine.inner_text()

            pseudo, handle, abonnes, videos = parser_chaine(texte)

            lien = ""

            liens = chaine.locator("a")

            print("----- Tous les liens -----")

            for j in range(liens.count()):

                href = liens.nth(j).get_attribute("href")

                print(href)

                if not href:
                    continue

                if (
                        href.startswith("/@")
                        or href.startswith("/channel/")
                        or href.startswith("/c/")
                        or href.startswith("/user/")
                ):
                    lien = "https://www.youtube.com" + href
                    break

            print("--------------------------")

            youtube_channel = YoutubeChannel(

                pseudo=pseudo,
                handle=handle,
                youtube_url=lien,
                youtube_subscribers=abonnes,
                videos=videos,
                description=""

            )

            resultats.append(youtube_channel)

            scraper_page_chaine(channel_page, youtube_channel)


        browser.close()

    return resultats