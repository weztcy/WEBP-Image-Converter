from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox
)



class ConversionStats(QWidget):


    def __init__(self):

        super().__init__()

        self.init_ui()



    def init_ui(self):

        layout = QVBoxLayout()


        box = QGroupBox(
            "Conversion Statistics"
        )


        box_layout = QVBoxLayout()


        self.total_label = QLabel(
            "Total Files: 0"
        )


        self.success_label = QLabel(
            "Success: 0"
        )


        self.failed_label = QLabel(
            "Failed: 0"
        )


        self.duration_label = QLabel(
            "Duration: 0 s"
        )


        self.speed_label = QLabel(
            "Speed: 0 img/s"
        )


        self.input_size_label = QLabel(
            "Input Size: 0 MB"
        )


        self.output_size_label = QLabel(
            "Output Size: 0 MB"
        )


        self.saved_label = QLabel(
            "Saved: 0%"
        )



        widgets = [

            self.total_label,

            self.success_label,

            self.failed_label,

            self.duration_label,

            self.speed_label,

            self.input_size_label,

            self.output_size_label,

            self.saved_label

        ]


        for widget in widgets:

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



    def update_stats(
            self,
            data
    ):


        self.total_label.setText(
            f"Total Files: {data['total']}"
        )


        self.success_label.setText(
            f"Success: {data['success']}"
        )


        self.failed_label.setText(
            f"Failed: {data['failed']}"
        )


        self.duration_label.setText(
            f"Duration: {data['duration']:.2f}s"
        )


        self.speed_label.setText(
            f"Speed: {data['speed']:.2f} img/s"
        )


        self.input_size_label.setText(
            f"Input Size: {data['input_mb']:.2f} MB"
        )


        self.output_size_label.setText(
            f"Output Size: {data['output_mb']:.2f} MB"
        )


        self.saved_label.setText(
            f"Saved: {data['saved_percent']:.2f}%"
        )