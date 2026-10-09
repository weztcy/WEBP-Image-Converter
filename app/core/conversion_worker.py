from app.core.converter import convert_image

from app.models.process_result import ProcessResult





def process_single_image(task):
    """
    High performance WEBP conversion worker.

    Task format:

    (
        input_path,
        output_path,
        mode,
        quality,
        method
    )

    Worker:
        input image
        ↓
        WEBP encoding
        ↓
        return result
    """



    image_path = None


    try:


        (
            image_path,
            output_path,
            mode,
            quality,
            method

        ) = task



        success = convert_image(

            source_path=image_path,

            output_path=output_path,

            mode=mode,

            quality=quality,

            method=method

        )



        return ProcessResult(

            success=success,

            file=image_path,

            output=output_path

        )



    except Exception as error:


        return ProcessResult(

            success=False,

            file=image_path,

            output=str(error)

        )