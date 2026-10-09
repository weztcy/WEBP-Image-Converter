from PIL import Image



def convert_image(
        source_path,
        output_path,
        mode="lossless",
        quality=80
):

    try:

        with Image.open(source_path) as image:


            image = image.convert(
                "RGBA"
            )


            if mode == "lossless":

                image.save(
                    output_path,
                    "WEBP",
                    lossless=True
                )


            elif mode == "lossy":

                image.save(
                    output_path,
                    "WEBP",
                    quality=quality,
                    lossless=False
                )


            else:

                raise ValueError(
                    "Invalid conversion mode"
                )


        return True



    except Exception as error:


        print(
            f"Conversion failed: {error}"
        )


        return False