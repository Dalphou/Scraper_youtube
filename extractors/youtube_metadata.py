def extraire_metadata_chaine(data):

    page_view = (
        data["header"]
            ["pageHeaderRenderer"]
            ["content"]
            ["pageHeaderViewModel"]
    )

    import pprint

    print()
    print("=" * 80)
    print("PAGE VIEW")
    print("=" * 80)

    pprint.pp(
        page_view,
        depth=8,
        width=120
    )

    return page_view["metadata"]["contentMetadataViewModel"]


def extraire_handle(metadata):

    return metadata["metadataRows"][0]["metadataParts"][0]["text"]["content"]


def extraire_abonnes(metadata):

    return metadata["metadataRows"][1]["metadataParts"][0]["text"]["content"]


def extraire_videos(metadata):

    return metadata["metadataRows"][1]["metadataParts"][1]["text"]["content"]


def remplir_metadata(data, youtube_channel):

    metadata = extraire_metadata_chaine(data)

    youtube_channel.handle = extraire_handle(metadata)
    youtube_channel.youtube_subscribers = extraire_abonnes(metadata)
    youtube_channel.videos = extraire_videos(metadata)