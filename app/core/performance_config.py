import os
import platform

import psutil





class PerformanceConfig:


    def __init__(self):


        # ==========================
        # CPU INFORMATION
        # ==========================


        self.cpu_threads = (
            os.cpu_count()
            or 4
        )


        self.cpu_cores = (
            psutil.cpu_count(
                logical=False
            )
            or self.cpu_threads
        )



        # ==========================
        # MEMORY INFORMATION
        # ==========================


        memory = psutil.virtual_memory()



        self.total_ram_gb = (

            memory.total

            /

            (1024 ** 3)

        )



        self.available_ram_gb = (

            memory.available

            /

            (1024 ** 3)

        )



        self.used_ram_gb = (

            memory.used

            /

            (1024 ** 3)

        )



        self.system = platform.system()





    # ==================================
    # WORKER CALCULATION
    # ==================================

    def calculate_workers(self):


        cpu = self.cpu_threads



        # ==================================
        # CPU FIRST STRATEGY
        # ==================================
        #
        # WEBP conversion merupakan workload:
        #
        # - image decoding
        # - encoding
        # - compression
        #
        # scaling mengikuti logical processor
        #
        # contoh:
        #
        # 16 thread -> 15 worker
        # 8 thread  -> 7 worker
        #
        # ==================================


        workers = max(

            2,

            cpu - 1

        )



        # ==================================
        # GLOBAL SAFETY LIMIT
        # ==================================


        workers = min(

            workers,

            32

        )



        return workers





    # ==================================
    # HARDWARE INFORMATION
    # ==================================

    def get_info(self):


        return {


            "system":

                self.system,



            "cpu_threads":

                self.cpu_threads,



            "cpu_cores":

                self.cpu_cores,



            "ram_total_gb":

                round(

                    self.total_ram_gb,

                    2

                ),



            "ram_used_gb":

                round(

                    self.used_ram_gb,

                    2

                ),



            "ram_available_gb":

                round(

                    self.available_ram_gb,

                    2

                ),



            "recommended_workers":

                self.calculate_workers()

        }





    # ==================================
    # DEBUG TEXT
    # ==================================

    def get_worker_explanation(self):


        return (

            f"{self.cpu_threads} CPU threads detected, "

            f"using {self.calculate_workers()} workers"

        )