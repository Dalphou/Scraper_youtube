from playwright.sync_api import TimeoutError


def accepter_cookies_youtube(page):

    print("Vérification des cookies...")

    boutons = [

        "button:has-text('Tout accepter')",
        "button:has-text('Accept all')",
        "button:has-text('Accepter tout')",

    ]

    for bouton in boutons:

        try:

            page.locator(bouton).first.click(timeout=3000)

            print("Cookies acceptés.")

            page.wait_for_load_state("networkidle")

            return True

        except TimeoutError:

            pass

    print("Aucun popup détecté.")

    return False