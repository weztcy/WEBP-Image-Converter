import psutil


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)


from PySide6.QtCore import QTimer




class PerformanceMonitor(QWidget):


    def __init__(self):

        super().__init__()


        self.init_ui()


        self.timer = QTimer()


        self.timer.timeout.connect(
            self.update_monitor
        )


        self.timer.start(
            1000
        )



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

                border-radius:18px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:15px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#metricTitle {

                color:#8F98A8;

                font-size:11px;

                font-weight:700;

            }



            QLabel#metricValue {

                color:#F9FAFB;

                font-size:24px;

                font-weight:800;

            }



            QLabel#infoTitle {

                color:#8F98A8;

                font-size:11px;

                font-weight:700;

            }



            QLabel#infoValue {

                color:#DCE6FF;

                font-size:13px;

                font-weight:700;

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
            18,
            18,
            18,
            18
        )


        layout.setSpacing(
            14
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



        # METRICS

        metrics = QHBoxLayout()

        metrics.setSpacing(
            12
        )


        cpu_card, self.cpu_label = self.create_metric(
            "CPU Usage"
        )


        ram_card, self.ram_label = self.create_metric(
            "RAM Usage"
        )


        metrics.addWidget(
            cpu_card
        )


        metrics.addWidget(
            ram_card
        )



        layout.addLayout(
            metrics
        )



        # INFO


        self.process_label = self.create_info(
            layout,
            "Workers"
        )


        self.webp_label = self.create_info(
            layout,
            "WEBP Profile"
        )



        root.addWidget(
            card
        )



    # ==================================
    # HELPERS
    # ==================================

    def create_metric(
            self,
            title
    ):


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


        layout.setContentsMargins(
            14,
            12,
            14,
            12
        )


        label = QLabel(
            title
        )

        label.setObjectName(
            "metricTitle"
        )


        value = QLabel(
            "0%"
        )

        value.setObjectName(
            "metricValue"
        )


        layout.addWidget(
            label
        )


        layout.addWidget(
            value
        )


        return frame, value



    def create_info(
            self,
            parent,
            title
    ):


        row = QHBoxLayout()


        label = QLabel(
            title
        )

        label.setObjectName(
            "infoTitle"
        )


        value = QLabel(
            "-"
        )

        value.setObjectName(
            "infoValue"
        )


        row.addWidget(
            label
        )


        row.addStretch()


        row.addWidget(
            value
        )


        parent.addLayout(
            row
        )


        return value



    # ==================================
    # MONITOR
    # ==================================

    def update_monitor(self):


        cpu = psutil.cpu_percent()


        ram = psutil.virtual_memory().percent



        self.cpu_label.setText(
            f"{cpu:.0f}%"
        )


        self.ram_label.setText(
            f"{ram:.0f}%"
        )



    # ==================================
    # PUBLIC API
    # ==================================

    def set_worker_info(
            self,
            workers
    ):


        self.process_label.setText(
            str(workers)
        )



    def set_profile(
            self,
            profile
    ):


        self.webp_label.setText(
            profile
        )