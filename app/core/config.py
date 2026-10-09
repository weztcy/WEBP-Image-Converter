from pathlib import Path


def get_default_output():

    pictures = Path.home() / "Pictures"

    output = pictures / "Image2WEBP"


    output.mkdir(
        parents=True,
        exist_ok=True
    )


    return output