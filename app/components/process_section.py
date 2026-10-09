from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Signal

from app.widgets.process_status import ProcessStatus
from app.widgets.performance_monitor import PerformanceMonitor
from app.widgets.conversion_stats import ConversionStats


class ProcessSection(QWidget):

    # expose signal agar ConvertPage tetap kompatibel
    open_folder_clicked = Signal()


    def __init__(self):
        super().__init__()

        self.init_components()
        self.init_ui()
        self.connect_signals()


    # ==================================
    # COMPONENTS
    # ==================================

    def init_components(self):

        self.process_status = ProcessStatus()

        self.performance = PerformanceMonitor()

        self.stats = ConversionStats()



    # ==================================
    # UI
    # ==================================

    def init_ui(self):

        layout = QVBoxLayout()


        # Status utama
        layout.addWidget(
            self.process_status
        )


        # Monitor + Statistik
        bottom_layout = QHBoxLayout()


        bottom_layout.addWidget(
            self.performance
        )


        bottom_layout.addWidget(
            self.stats
        )


        layout.addLayout(
            bottom_layout
        )


        self.setLayout(
            layout
        )



    # ==================================
    # SIGNAL
    # ==================================

    def connect_signals(self):

        self.process_status.open_folder_clicked.connect(
            self.open_folder_clicked.emit
        )



    # ==================================
    # STATUS API
    # ==================================

    def reset(self):

        self.process_status.reset()


        self.stats.update_stats({
            "total": 0,
            "success": 0,
            "failed": 0,
            "duration": 0,
            "speed": 0,
            "input_mb": 0,
            "output_mb": 0,
            "saved_percent": 0
        })


    def set_processing(self):

        self.process_status.set_processing()


    def set_completed(self):

        self.process_status.set_completed()


    def set_cancelled(self):

        self.process_status.set_cancelled()


    def set_idle(self):

        self.process_status.set_idle()



    # ==================================
    # PROCESS UPDATE
    # ==================================

    def update_file(self, filename):

        self.process_status.update_file(
            filename
        )



    def update_progress(self, progress):

        self.process_status.update_progress(
            progress
        )



    def update_result(self, success, failed):

        self.process_status.update_result(
            success,
            failed
        )



    # ==================================
    # STATISTICS
    # ==================================

    def update_statistics(self, data):

        self.stats.update_stats(
            data
        )



    # ==================================
    # PERFORMANCE
    # ==================================

    def set_profile(self, profile):

        self.performance.set_profile(
            profile
        )



    def set_workers(self, workers):

        self.performance.set_worker_info(
            workers
        )