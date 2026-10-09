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



class ProcessPoolManager:


    def __init__(
            self,
            workers=None
    ):


        # ==================================
        # HARDWARE DETECTION
        # ==================================

        if workers is None:


            config = PerformanceConfig()


            workers = (
                config.calculate_workers()
            )


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


        print(
            f"Workers active: {self.workers}"
        )



    def create_task(
            self,
            image,
            settings,
            output_folder
    ):


        """
        Lightweight task object.

        Tuple lebih ringan dibanding dictionary
        untuk multiprocessing serialization.
        """


        return (

            str(image.path),

            str(output_folder),

            settings["mode"],

            settings["quality"]

        )



    def process(
            self,
            images,
            settings,
            output_folder,
            on_file=None,
            on_progress=None
    ):


        total = len(images)



        if total == 0:


            return {

                "success": 0,

                "failed": 0

            }



        success = 0

        failed = 0



        # ==================================
        # ADAPTIVE WORKER COUNT
        # ==================================

        active_workers = min(
            self.workers,
            total
        )


        print(
            f"Active workers for job: {active_workers}"
        )



        # ==================================
        # CREATE TASKS
        # ==================================

        tasks = [

            self.create_task(
                image,
                settings,
                output_folder
            )

            for image in images

        ]



        # ==================================
        # PROCESS EXECUTION
        # ==================================

        with ProcessPoolExecutor(
                max_workers=active_workers
        ) as executor:



            futures = [

                executor.submit(
                    process_single_image,
                    task
                )

                for task in tasks

            ]



            # ==================================
            # COLLECT RESULT
            # ==================================

            for index, future in enumerate(
                    as_completed(futures),
                    start=1
            ):


                try:


                    result = future.result()



                except Exception as error:


                    print(
                        f"Worker failed: {error}"
                    )


                    failed += 1

                    continue



                # ==================================
                # RESULT FORMAT:
                #
                # (
                #    success,
                #    file_path,
                #    output_path/error
                # )
                #
                # ==================================


                result_success = result[0]

                file_path = result[1]



                if result_success:

                    success += 1


                else:

                    failed += 1



                # ==================================
                # FILE CALLBACK
                # ==================================

                if on_file:


                    on_file(
                        file_path
                    )



                # ==================================
                # PROGRESS CALLBACK
                # ==================================

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



        return {


            "success": success,


            "failed": failed

        }