from app.core.process_pool import ProcessPoolManager



class ProcessManager:


    def __init__(self):

        self.success = 0

        self.failed = 0

        self.cancelled = False


        self.pool = ProcessPoolManager()



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



        def handle_file(filename):

            if on_file:

                on_file(filename)



        def handle_progress(
                progress,
                success,
                failed
        ):

            self.success = success

            self.failed = failed


            if on_progress:

                on_progress(
                    progress,
                    success,
                    failed
                )



        try:


            result = self.pool.process(

                images,

                settings,

                output_folder,

                on_file=handle_file,

                on_progress=handle_progress

            )


            self.success = result["success"]

            self.failed = result["failed"]



        except Exception as error:


            print(
                f"Process manager error: {error}"
            )


            self.failed = total



        return {


            "success": self.success,


            "failed": self.failed,


            "cancelled": self.cancelled

        }