from pathlib import Path


from app.models.image_model import ImageModel



SUPPORTED_FORMAT = [

    ".jpg",

    ".jpeg",

    ".png"

]



def is_supported(file_path):

    return (

        Path(file_path)
        .suffix
        .lower()

        in SUPPORTED_FORMAT

    )



def load_files(files):

    images = []



    for file in files:


        if not is_supported(file):

            continue



        try:


            images.append(

                ImageModel(file)

            )



        except Exception as error:


            print(
                f"Failed loading image {file}: {error}"
            )



    return images



def load_folder(folder):

    folder_path = Path(folder)


    files = []



    for file in folder_path.rglob("*"):


        if (

            file.is_file()

            and is_supported(file)

        ):

            files.append(

                str(file)

            )



    return load_files(files)