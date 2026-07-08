def rechercher_cle(objet, cle_recherchee, chemin=""):

    if isinstance(objet, dict):

        for cle, valeur in objet.items():

            nouveau_chemin = f"{chemin}.{cle}" if chemin else cle

            if cle == cle_recherchee:

                print()
                print("=" * 80)
                print("Clé trouvée !")
                print("=" * 80)
                print(nouveau_chemin)
                print()
                print(valeur)

            rechercher_cle(valeur, cle_recherchee, nouveau_chemin)

    elif isinstance(objet, list):

        for i, element in enumerate(objet):

            rechercher_cle(
                element,
                cle_recherchee,
                f"{chemin}[{i}]"
            )