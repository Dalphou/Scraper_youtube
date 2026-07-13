from config import MIN_ABONNES
from utils import convertir_nombre_abonnes


def conserver_chaine(youtube_channel):

    nb_abonnes = convertir_nombre_abonnes(
        youtube_channel.youtube_subscribers
    )

    if nb_abonnes < MIN_ABONNES:

        print(
            f"✘ {youtube_channel.pseudo} ignorée "
            f"({nb_abonnes} abonnés)"
        )

        return False

    print(
        f"✔ {youtube_channel.pseudo} conservée "
        f"({nb_abonnes} abonnés)"
    )

    return True