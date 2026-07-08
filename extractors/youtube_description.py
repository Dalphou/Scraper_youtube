def extraire_description(data):

    page_view = (
        data["header"]
            ["pageHeaderRenderer"]
            ["content"]
            ["pageHeaderViewModel"]
    )

    return (
        page_view["description"]
                 ["descriptionPreviewViewModel"]
                 ["description"]
                 ["content"]
    )


def remplir_description(data, youtube_channel):

    youtube_channel.description = (
        extraire_description(data)
    )