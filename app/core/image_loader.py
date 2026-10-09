from pathlib import Path

from app.models.image_model import ImageModel



# Set lebih cepat untuk pengecekan
SUPPORTED_FORMAT = {
    ".jpg",
    ".jpeg",
    ".png"
}



def is_supported(file_path):

    try:

        return (
            Path(file_path)
            .suffix
            .lower()
            in SUPPORTED_FORMAT
        )

    except Exception:

        return False



def load_files(files):

    images = []


    for file in files:


        path = Path(file)


        if not is_supported(path):

            continue


        try:

            images.append(
                ImageModel(
                    str(path.resolve())
                )
            )


        except Exception as error:


            print(
                f"Failed loading image {file}: {error}"
            )


    return images



def load_folder(folder):

    folder_path = Path(folder)


    images = []


    if not folder_path.exists():

        return images



    # Scan hanya file dengan extension target
    for extension in SUPPORTED_FORMAT:


        for file in folder_path.rglob(
                f"*{extension}"
        ):


            if not file.is_file():

                continue



            try:


                images.append(

                    ImageModel(
                        str(file.resolve())
                    )

                )


            except Exception as error:


                print(
                    f"Failed loading image {file}: {error}"
                )



    return images