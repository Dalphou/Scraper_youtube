from config import MOT_CLE

from platforms.youtube import rechercher_youtube

from exporters.excel_export import export_to_excel


resultats = rechercher_youtube(MOT_CLE)

print("=" * 70)
print("Résultat")
print("=" * 70)

for chaine in resultats:

    print()

    print("Pseudo :", chaine.pseudo)

    print("URL :", chaine.youtube_url)

    print("Abonnés :", chaine.youtube_subscribers)

export_to_excel(
    resultats,
    "output/minecraft.xlsx"
)

print("Excel créé avec succès !")