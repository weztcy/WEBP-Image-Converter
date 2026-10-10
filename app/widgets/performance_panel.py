from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QProgressBar
)


from app.widgets.resource_chart import ResourceChart
from app.core.system_monitor import SystemMonitor





class PerformancePanel(QWidget):


    def __init__(
            self,
            process_manager=None
    ):

        super().__init__()


        self.process_manager = process_manager


        self.monitor = SystemMonitor()


        self.monitor_running = False


        self.init_ui()
        
        self.start_monitor()





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



            QFrame#card {


                background:#10141C;

                border:1px solid #242938;

                border-radius:22px;

            }



            QLabel#title {


                color:#F9FAFB;

                font-size:16px;

                font-weight:800;

            }



            QLabel#subtitle {


                color:#98A2B3;

                font-size:12px;

            }



            QLabel#value {


                color:#F9FAFB;

                font-size:20px;

                font-weight:900;

            }



            QLabel#label {


                color:#98A2B3;

                font-size:12px;

                font-weight:700;

            }



            QProgressBar {


                background:#202633;

                border-radius:5px;

                height:8px;

                text-align:center;

            }



            QProgressBar::chunk {


                background:#4F8CFF;

                border-radius:5px;

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
            "card"
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
            "⚡ System Performance"
        )

        title.setObjectName(
            "title"
        )



        subtitle = QLabel(
            "Real-time resource monitoring"
        )

        subtitle.setObjectName(
            "subtitle"
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            subtitle
        )



        # ==============================
        # CPU RAM CHART
        # ==============================


        charts = QHBoxLayout()


        self.cpu_chart = ResourceChart(
            "CPU Usage"
        )


        self.ram_chart = ResourceChart(
            "RAM Usage"
        )


        charts.addWidget(
            self.cpu_chart
        )


        charts.addWidget(
            self.ram_chart
        )



        layout.addLayout(
            charts
        )



        # ==============================
        # INFO
        # ==============================


        info = QHBoxLayout()



        info.addWidget(
            self.create_worker_card()
        )


        info.addWidget(
            self.create_profile_card()
        )



        layout.addLayout(
            info
        )



        root.addWidget(
            card
        )





    # ==================================
    # WORKER CARD
    # ==================================

    def create_worker_card(self):


        frame = QFrame()



        frame.setStyleSheet(
            """

            QFrame {

                background:#181D27;

                border-radius:14px;

            }

            """

        )



        layout = QVBoxLayout(frame)



        title = QLabel(
            "⚙ Worker Pool"
        )

        title.setObjectName(
            "label"
        )



        self.worker_value = QLabel(
            "0 / 0 Active"
        )


        self.worker_value.setObjectName(
            "value"
        )



        self.worker_bar = QProgressBar()


        self.worker_bar.setRange(
            0,
            100
        )


        self.worker_bar.setValue(
            0
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            self.worker_value
        )


        layout.addWidget(
            self.worker_bar
        )



        return frame





    # ==================================
    # PROFILE CARD
    # ==================================

    def create_profile_card(self):


        frame = QFrame()



        frame.setStyleSheet(
            """

            QFrame {

                background:#181D27;

                border-radius:14px;

            }

            """

        )



        layout = QVBoxLayout(frame)



        title = QLabel(
            "WEBP Profile"
        )


        title.setObjectName(
            "label"
        )



        self.profile_value = QLabel(
            "⭐ Standard"
        )


        self.profile_value.setObjectName(
            "value"
        )



        self.profile_desc = QLabel(
            "Balanced speed & size"
        )


        self.profile_desc.setObjectName(
            "label"
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            self.profile_value
        )


        layout.addWidget(
            self.profile_desc
        )



        return frame





    # ==================================
    # MONITOR CONTROL
    # ==================================

    def start_monitor(self):


        if self.monitor_running:

            return



        self.monitor.updated.connect(
            self.update_resource
        )


        self.monitor.start()


        self.monitor_running = True





    def stop_monitor(self):


        if not self.monitor_running:

            return



        self.monitor.stop()


        self.monitor_running = False





    # ==================================
    # RESOURCE UPDATE
    # ==================================

    def update_resource(
            self,
            data
    ):


        self.cpu_chart.update_value(
            data["cpu"]
        )


        self.ram_chart.update_value(
            data["ram"]
        )





    # ==================================
    # WORKER UPDATE
    # ==================================

    def update_worker(
            self,
            active,
            maximum
    ):


        self.worker_value.setText(

            f"{active} / {maximum} Active"

        )



        percent = 0



        if maximum > 0:


            percent = int(

                (

                    active

                    /

                    maximum

                )

                *

                100

            )



        self.worker_bar.setValue(
            percent
        )





    # ==================================
    # PROFILE UPDATE
    # ==================================

    def update_profile(
            self,
            profile
    ):


        profiles = {


            "fast":

            (

                "⚡ Fast",

                "Fast conversion priority"

            ),



            "balanced":

            (

                "⭐ Standard",

                "Balanced speed & size"

            ),



            "compression":

            (

                "🗜 Maximum",

                "Smallest file size"

            )

        }



        title, desc = profiles.get(

            profile,

            (

                "Unknown",

                ""

            )

        )



        self.profile_value.setText(
            title
        )


        self.profile_desc.setText(
            desc
        )
        
    def set_profile(self, profile):

        self.update_profile(
            profile
        )


    def set_worker_info(self, workers):

        self.update_worker(
            workers,
            workers
        )