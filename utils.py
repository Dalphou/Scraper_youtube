from playwright.sync_api import TimeoutError


import re


def convertir_nombre_abonnes(texte: str) -> int:

    texte = texte.lower().replace("abonnés", "").replace("abonné", "").strip()

    texte = texte.replace(",", ".")

    match = re.search(r"([\d.]+)\s*([km]?)", texte)

    if not match:
        return 0

    nombre = float(match.group(1))
    unite = match.group(2)

    if unite == "k":
        nombre *= 1000

    elif unite == "m":
        nombre *= 1_000_000

    return int(nombre)

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