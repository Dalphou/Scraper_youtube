def charger_plus_de_resultats(page, nb_resultats):

    while page.locator("ytd-channel-renderer").count() < nb_resultats:

        print(f"Chaînes chargées : {page.locator('ytd-channel-renderer').count()}")

        page.mouse.wheel(0, 5000)

        page.wait_for_timeout(1000)