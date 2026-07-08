from openpyxl import Workbook


def export_to_excel(resultats, nom_fichier):

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "YouTube"

    sheet.append([
        "Pseudo",
        "Handle",
        "URL YouTube",
        "Abonnés YouTube",
        "Description",
        "Twitter",
        "facebook",
        "Instagram",
        "TikTok",
        "Twitch",
        "Discord",
        "Website",
        "lien_divers",
        "Contact 1",
        "Contact 2"
    ])

    for chaine in resultats:

        sheet.append([

            chaine.pseudo,

            chaine.handle,

            chaine.youtube_url,

            chaine.youtube_subscribers,

            chaine.description,

            chaine.twitter,

            chaine.facebook,

            chaine.instagram,

            chaine.tiktok,

            chaine.twitch,

            chaine.discord,

            chaine.website,

            chaine.contact_1,

            chaine.contact_2

        ])

    workbook.save(nom_fichier)