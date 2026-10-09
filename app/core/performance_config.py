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


        self.available_ram_mb = (
            self.available_ram_gb
            *
            1024
        )


        self.system = platform.system()



    def calculate_workers(self):


        cpu = self.cpu_threads


        # =================================
        # CPU FIRST STRATEGY
        # =================================
        #
        # WEBP conversion:
        # - image decode
        # - encoding
        # - compression
        #
        # scaling terbaik mengikuti logical CPU
        #


        workers = max(
            2,
            cpu - 1
        )



        # =================================
        # RAM SAFETY BRAKE
        # =================================
        #
        # RAM hanya membatasi jika benar-benar
        # rendah.
        #
        # Normal:
        # biarkan CPU bekerja penuh.
        #


        ram_mb = self.available_ram_mb



        # RAM sangat kritis
        # < 3GB tersedia

        if ram_mb < 3072:


            workers = min(
                workers,
                4
            )



        # RAM rendah
        # 3-5GB tersedia

        elif ram_mb < 5120:


            workers = min(
                workers,
                cpu - 2
            )



        # RAM cukup
        # jangan dibatasi



        # =================================
        # DEVICE SAFETY LIMIT
        # =================================


        workers = max(
            2,
            workers
        )


        workers = min(
            workers,
            32
        )


        return workers



    def get_info(self):


        return {


            "system":
                self.system,


            "cpu_threads":
                self.cpu_threads,


            "cpu_cores":
                self.cpu_cores,


            "ram_gb":
                round(
                    self.total_ram_gb,
                    2
                ),


            "available_ram_gb":
                round(
                    self.available_ram_gb,
                    2
                ),


            "recommended_workers":
                self.calculate_workers()

        }