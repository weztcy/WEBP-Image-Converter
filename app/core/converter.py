from pathlib import Path

from PIL import Image



DEFAULT_WEBP_METHOD = 2



SUPPORTED_MODES = (
    "lossless",
    "lossy"
)



def convert_image(
        source_path,
        output_path,
        mode="lossless",
        quality=80,
        method=DEFAULT_WEBP_METHOD
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


        source_path = Path(
            source_path
        )


        output_path = Path(
            output_path
        )



        # ==========================
        # VALIDATION
        # ==========================


        if mode not in SUPPORTED_MODES:

            raise ValueError(
                f"Invalid mode: {mode}"
            )



        method = max(

            0,

            min(

                int(method),

                6

            )

        )



        if mode == "lossy":

            quality = max(

                1,

                min(

                    int(quality),

                    100

                )

            )



        # ==========================
        # OUTPUT
        # ==========================


        output_path.parent.mkdir(

            parents=True,

            exist_ok=True

        )



        # ==========================
        # LOAD IMAGE
        # ==========================


        image = Image.open(

            source_path

        )



        # ==========================
        # COLOR OPTIMIZATION
        # ==========================


        if image.mode not in (

            "RGB",

            "RGBA"

        ):


            if "transparency" in image.info:


                converted = image.convert(

                    "RGBA"

                )


            else:


                converted = image.convert(

                    "RGB"

                )



            image.close()


            image = converted





        # ==========================
        # WEBP OPTIONS
        # ==========================


        options = {

            "format":
                "WEBP",

            "method":
                method

        }



        if mode == "lossless":


            options.update({

                "lossless": True

            })



        else:


            options.update({

                "lossless": False,

                "quality": quality

            })



        # ==========================
        # SAVE
        # ==========================


        image.save(

            output_path,

            **options

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