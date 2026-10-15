from pathlib import Path



APP_NAME = "WEBP Converter Pro"

APP_VERSION = "1.0.0"



def get_default_output():

    pictures = Path.home() / "Pictures"


    output = pictures / "WEBP"



    output.mkdir(

        parents=True,

        exist_ok=True

    )



    return output