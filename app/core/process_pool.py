from pathlib import Path


from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)


from app.core.conversion_worker import (
    process_single_image
)


from app.core.performance_config import (
    PerformanceConfig
)


from app.core.webp_profile import (
    get_webp_method
)


from app.utils.file_utils import (
    create_output_path
)





class ProcessPoolManager:


    def __init__(
            self,
            workers=None
    ):

        if workers is None:

            config = PerformanceConfig()

            workers = config.calculate_workers()


            print(
                "Hardware Profile:"
            )


            print(
                config.get_info()
            )


        else:

            print(
                "Manual worker override"
            )


        self.workers = workers


        # worker yang sedang dipakai job sekarang
        self.active_workers = 0


        self.cancelled = False


        self.executor = None


        self.futures = []





    # ==================================
    # CANCEL
    # ==================================

    def cancel(self):


        self.cancelled = True



        for future in self.futures:

            future.cancel()





    # ==================================
    # FILE SIZE
    # ==================================

    def get_file_size(
            self,
            path
    ):


        try:


            return Path(
                path
            ).stat().st_size



        except Exception:


            return 0





    # ==================================
    # ACTIVE WORKER COUNT
    # ==================================

    def update_worker_status(
            self,
            callback
    ):

        if callback:

            callback(

                self.active_workers,

                self.workers

            )





    # ==================================
    # CREATE TASK
    # ==================================

    def create_task(
            self,
            image,
            settings,
            output_folder
    ):


        output_path = create_output_path(

            str(image.path),

            output_folder

        )



        method = get_webp_method(

            settings.get(

                "profile",

                "fast"

            )

        )



        return (

            str(image.path),

            str(output_path),

            settings["mode"],

            settings["quality"],

            method

        )


    # ==================================
    # PROCESS
    # ==================================

    def process(
            self,
            images,
            settings,
            output_folder,
            on_file=None,
            on_progress=None,
            on_worker_update=None
    ):


        self.cancelled = False


        self.futures.clear()



        total = len(images)



        if total == 0:


            return {


                "success":0,


                "failed":0,


                "cancelled":False,


                "input_bytes":0,


                "output_bytes":0,


                "saved_percent":0


            }





        success = 0


        failed = 0


        input_bytes = 0


        output_bytes = 0





        # ==================================
        # WORKER LIMIT
        # ==================================

        active_workers = min(

            self.workers,

            total

        )



        print(

            f"Active workers limit: {active_workers}"

        )





        # ==================================
        # CREATE TASK
        # ==================================

        tasks = [

            self.create_task(

                image,

                settings,

                output_folder

            )

            for image in images

        ]





        for task in tasks:


            input_bytes += self.get_file_size(

                task[0]

            )





        # ==================================
        # PROCESS POOL
        # ==================================

        self.executor = ProcessPoolExecutor(

            max_workers=active_workers

        )


        self.active_workers = active_workers


        self.update_worker_status(

            on_worker_update

        )



        try:


            # ==============================
            # SUBMIT JOB
            # ==============================

            for task in tasks:


                if self.cancelled:

                    break



                future = self.executor.submit(

                    process_single_image,

                    task

                )



                self.futures.append(

                    future

                )




            # ==============================
            # COLLECT RESULT
            # ==============================

            for index, future in enumerate(

                    as_completed(self.futures),

                    start=1

            ):



                if self.cancelled:

                    break




                try:


                    result = future.result()



                except Exception as error:


                    print(

                        f"Worker failed: {error}"

                    )


                    failed += 1


                    self.update_worker_status(

                        on_worker_update

                    )


                    continue





                if result.success:


                    success += 1



                    output_bytes += self.get_file_size(

                        result.output

                    )



                else:


                    failed += 1





                # update worker setelah selesai

                self.update_worker_status(

                    on_worker_update

                )





                # ==========================
                # FILE CALLBACK
                # ==========================

                if on_file:


                    on_file(

                        result.file

                    )





                # ==========================
                # PROGRESS CALLBACK
                # ==========================

                if on_progress:


                    progress = int(

                        (

                            index

                            /

                            total

                        )

                        *

                        100

                    )



                    on_progress(

                        progress,

                        success,

                        failed

                    )





        finally:



            if self.executor:


                self.executor.shutdown(

                    wait=False,

                    cancel_futures=True

                )


                self.executor = None





            # reset UI
            self.active_workers = 0


            if on_worker_update:

                on_worker_update(

                    0,

                    self.workers

                )







        # ==================================
        # COMPRESSION STATISTIC
        # ==================================

        saved_percent = 0



        if input_bytes > 0:


            saved_percent = (

                (

                    input_bytes

                    -

                    output_bytes

                )

                /

                input_bytes

            ) * 100





        return {


            "success":

                success,


            "failed":

                failed,


            "cancelled":

                self.cancelled,


            "input_bytes":

                input_bytes,


            "output_bytes":

                output_bytes,


            "saved_percent":

                saved_percent

        }