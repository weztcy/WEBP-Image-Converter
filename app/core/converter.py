from PIL import Image
from pathlib import Path



WEBP_METHOD = 4



def convert_image(
        source_path,
        output_path,
        mode="lossless",
        quality=80
):
    """
    High performance WEBP converter.

    Optimized for:
    - multiprocessing
    - batch conversion
    - low memory usage
    """


    image = None


    try:


        # Open image
        image = Image.open(
            source_path
        )


        # ==========================
        # COLOR MODE OPTIMIZATION
        # ==========================

        if image.mode not in (
            "RGB",
            "RGBA"
        ):

            image = image.convert(
                "RGBA"
            )



        # ==========================
        # WEBP ENCODE
        # ==========================

        if mode == "lossless":


            image.save(
                output_path,
                "WEBP",
                lossless=True,
                method=WEBP_METHOD
            )


        elif mode == "lossy":


            image.save(
                output_path,
                "WEBP",
                quality=int(quality),
                lossless=False,
                method=WEBP_METHOD
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



    finally:


        if image is not None:

            image.close()