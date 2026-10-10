from PySide6.QtCore import (
    QObject,
    Signal,
    QTimer
)

import psutil



class SystemMonitor(QObject):


    updated = Signal(dict)



    def __init__(
            self,
            interval=1000
    ):

        super().__init__()


        self.interval = interval


        self.timer = QTimer()


        self.timer.timeout.connect(
            self.collect
        )


        # inisialisasi cpu counter
        psutil.cpu_percent(
            interval=None
        )


    # ==================================
    # START MONITOR
    # ==================================

    def start(self):

        self.timer.start(
            self.interval
        )



    # ==================================
    # STOP MONITOR
    # ==================================

    def stop(self):

        self.timer.stop()



    # ==================================
    # COLLECT DATA
    # ==================================

    def collect(self):


        cpu = psutil.cpu_percent(
            interval=None
        )


        ram = psutil.virtual_memory()


        data = {

            "cpu": cpu,

            "ram": ram.percent,

            "ram_used": ram.used,

            "ram_total": ram.total

        }


        self.updated.emit(
            data
        )