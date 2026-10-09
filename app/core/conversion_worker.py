from app.core.converter import convert_image
from app.utils.file_utils import create_output_path



def process_single_image(task):
    """
    High performance multiprocessing worker.

    Task format:

    (
        image_path,
        output_folder,
        mode,
        quality
    )

    """


    image_path = None


    try:


        (
            image_path,
            output_folder,
            mode,
            quality

        ) = task



        output_path = create_output_path(
            image_path,
            output_folder
        )



        success = convert_image(
            image_path,
            output_path,
            mode=mode,
            quality=quality
        )



        return (

            success,

            image_path,

            str(output_path)

        )



    except Exception as error:


        return (

            False,

            image_path,

            str(error)

        )