import psutil


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox
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



    def init_ui(self):


        layout = QVBoxLayout()


        box = QGroupBox(
            "System Monitor"
        )


        box_layout = QVBoxLayout()



        self.cpu_label = QLabel(
            "CPU: 0%"
        )


        self.ram_label = QLabel(
            "RAM: 0%"
        )


        self.process_label = QLabel(
            "Workers: -"
        )


        self.webp_label = QLabel(
            "WEBP Profile: -"
        )



        for widget in [

            self.cpu_label,

            self.ram_label,

            self.process_label,

            self.webp_label

        ]:

            box_layout.addWidget(
                widget
            )


        box.setLayout(
            box_layout
        )


        layout.addWidget(
            box
        )


        self.setLayout(
            layout
        )



    def update_monitor(self):


        cpu = psutil.cpu_percent()


        ram = psutil.virtual_memory().percent



        self.cpu_label.setText(
            f"CPU Usage: {cpu}%"
        )


        self.ram_label.setText(
            f"RAM Usage: {ram}%"
        )



    def set_worker_info(
            self,
            workers
    ):


        self.process_label.setText(
            f"Workers: {workers}"
        )



    def set_profile(
            self,
            profile
    ):


        self.webp_label.setText(
            f"WEBP Profile: {profile}"
        )