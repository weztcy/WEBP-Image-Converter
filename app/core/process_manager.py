from app.core.converter import convert_image


from app.utils.file_utils import (
    create_output_path
)



class ProcessManager:


    def __init__(self):

        self.success = 0

        self.failed = 0

        self.cancelled = False



    def cancel(self):

        self.cancelled = True



    def process(
            self,
            images,
            settings,
            output_folder,
            on_file=None,
            on_progress=None
    ):

        self.success = 0

        self.failed = 0

        self.cancelled = False



        total = len(images)



        if total == 0:

            return {

                "success": 0,

                "failed": 0,

                "cancelled": False

            }



        for index, image in enumerate(images, start=1):


            if self.cancelled:

                break



            if on_file:

                on_file(
                    image.filename
                )



            try:


                output_path = create_output_path(

                    image.path,

                    output_folder

                )



                result = convert_image(

                    image.path,

                    output_path,

                    mode=settings["mode"],

                    quality=settings["quality"]

                )



                if result:

                    self.success += 1


                else:

                    self.failed += 1



            except Exception as error:


                print(
                    f"Processing failed: {error}"
                )


                self.failed += 1



            progress = int(

                (index / total) * 100

            )



            if on_progress:

                on_progress(

                    progress,

                    self.success,

                    self.failed

                )



        return {

            "success": self.success,

            "failed": self.failed,

            "cancelled": self.cancelled

        }