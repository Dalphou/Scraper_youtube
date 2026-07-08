import re
import json

from extractors.youtube_links import remplir_liens
from extractors.youtube_metadata import remplir_metadata
from extractors.youtube_description import remplir_description

from utils_json import rechercher_cle


def parser_page_chaine(page, youtube_channel):

    print(f"Analyse de la chaîne : {youtube_channel.pseudo}")



    html = page.content()

    resultat = re.search(
        r"var ytInitialData = (.*?);</script>",
        html,
        re.DOTALL
    )

    if resultat is None:

        print("ytInitialData introuvable.")
        return

    try:

        data = json.loads(
            resultat.group(1)
        )

        remplir_metadata(
            data,
            youtube_channel
        )

        remplir_description(
            data,
            youtube_channel
        )

        remplir_liens(
            page,
            youtube_channel
        )


        print()
        print("=" * 80)
        print("Métadonnées de la chaîne")
        print("=" * 80)

        print(f"Pseudo      : {youtube_channel.pseudo}")
        print(f"Handle      : {youtube_channel.handle}")
        print(f"Abonnés     : {youtube_channel.youtube_subscribers}")
        print(f"Vidéos      : {youtube_channel.videos}")
        print(f"Description : {youtube_channel.description}")

    except Exception as erreur:

        print("Erreur :", erreur)