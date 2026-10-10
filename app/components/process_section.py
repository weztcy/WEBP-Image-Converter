from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import Signal


from app.widgets.process_status import ProcessStatus
from app.widgets.performance_panel import PerformancePanel
from app.widgets.conversion_stats import ConversionStats



class ProcessSection(QWidget):


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


        # menggunakan chart performance
        self.performance = PerformancePanel()


        self.stats = ConversionStats()



    # ==================================
    # UI
    # ==================================

    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }


            QFrame#monitorCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }


            QFrame#innerCard {

                background:#10141C;

                border-radius:18px;

            }


            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }


            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }


            QLabel#sectionLabel {

                color:#7EA6FF;

                font-size:11px;

                font-weight:700;

                letter-spacing:1px;

            }

            """
        )



        root = QVBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )


        card = QFrame()

        card.setObjectName(
            "monitorCard"
        )


        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            22,
            22,
            22,
            22
        )


        layout.setSpacing(
            16
        )



        # HEADER

        title = QLabel(
            "📊 Processing Monitor"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Track conversion progress, performance, and output statistics."
        )

        subtitle.setObjectName(
            "subtitle"
        )


        layout.addWidget(title)

        layout.addWidget(subtitle)



        # STATUS

        status_label = QLabel(
            "CURRENT PROCESS"
        )

        status_label.setObjectName(
            "sectionLabel"
        )


        layout.addWidget(
            status_label
        )


        status_card = QFrame()

        status_card.setObjectName(
            "innerCard"
        )


        status_layout = QVBoxLayout(
            status_card
        )


        status_layout.setContentsMargins(
            14,
            14,
            14,
            14
        )


        status_layout.addWidget(
            self.process_status
        )


        layout.addWidget(
            status_card
        )



        # PERFORMANCE + STATISTICS

        dashboard_label = QLabel(
            "PERFORMANCE & STATISTICS"
        )

        dashboard_label.setObjectName(
            "sectionLabel"
        )


        layout.addWidget(
            dashboard_label
        )



        bottom = QHBoxLayout()

        bottom.setSpacing(
            16
        )



        # LEFT : PERFORMANCE PANEL

        performance_card = QFrame()

        performance_card.setObjectName(
            "innerCard"
        )


        performance_layout = QVBoxLayout(
            performance_card
        )


        performance_layout.setContentsMargins(
            14,
            14,
            14,
            14
        )


        performance_layout.addWidget(
            self.performance
        )



        # RIGHT : STATISTICS

        stats_card = QFrame()

        stats_card.setObjectName(
            "innerCard"
        )


        stats_layout = QVBoxLayout(
            stats_card
        )


        stats_layout.setContentsMargins(
            14,
            14,
            14,
            14
        )


        stats_layout.addWidget(
            self.stats
        )



        bottom.addWidget(
            performance_card,
            1
        )


        bottom.addWidget(
            stats_card,
            1
        )



        layout.addLayout(
            bottom
        )


        root.addWidget(
            card
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

            "total":0,

            "success":0,

            "failed":0,

            "duration":0,

            "speed":0,

            "input_mb":0,

            "output_mb":0,

            "saved_percent":0

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

        self.process_status.update_file(filename)



    def update_progress(self, progress):

        self.process_status.update_progress(progress)



    def update_result(self, success, failed):

        self.process_status.update_result(
            success,
            failed
        )



    # ==================================
    # STATISTICS
    # ==================================

    def update_statistics(self, data):

        self.stats.update_stats(data)



    # ==================================
    # PERFORMANCE
    # ==================================

    def set_profile(self, profile):

        if hasattr(
            self.performance,
            "set_profile"
        ):
            self.performance.set_profile(profile)



    def set_workers(self, workers):

        if hasattr(
            self.performance,
            "set_worker_info"
        ):
            self.performance.set_worker_info(workers)

        elif hasattr(
            self.performance,
            "set_workers"
        ):
            self.performance.set_workers(workers)