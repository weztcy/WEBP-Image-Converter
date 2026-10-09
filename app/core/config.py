from pathlib import Path



APP_NAME = "Image2WEBP Converter"

APP_VERSION = "1.0.0"



def get_default_output():

    pictures = Path.home() / "Pictures"


    output = pictures / "Image2WEBP"



    output.mkdir(

        parents=True,

        exist_ok=True

    )



    return output