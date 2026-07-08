import re


def parser_chaine(texte: str):

    lignes = texte.split("\n")

    pseudo = ""
    handle = ""
    abonnes = ""
    videos = ""

    for ligne in lignes:

        ligne = ligne.strip()

        if not ligne:
            continue

        if ligne.startswith("@"):
            handle = ligne
            continue

        if re.search(r"\babonn", ligne.lower()):
            abonnes = ligne
            continue

        if re.search(r"\bvidéo", ligne.lower()):
            videos = ligne
            continue

        if pseudo == "":
            pseudo = ligne

    return pseudo, handle, abonnes, videos