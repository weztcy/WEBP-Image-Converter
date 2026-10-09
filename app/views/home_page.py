from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)


from PySide6.QtCore import Qt



class HomePage(QWidget):


    def __init__(self, start_convert_callback):

        super().__init__()


        self.start_convert_callback = start_convert_callback


        self.init_ui()



    def init_ui(self):

        layout = QVBoxLayout()


        layout.setAlignment(
            Qt.AlignCenter
        )



        title = QLabel(
            "Welcome to Image2WEBP Converter"
        )


        title.setAlignment(
            Qt.AlignCenter
        )



        description = QLabel(
            "Convert JPG, JPEG, and PNG images "
            "into optimized WEBP format easily."
        )


        description.setAlignment(
            Qt.AlignCenter
        )



        start_button = QPushButton(
            "Start Converting"
        )



        start_button.clicked.connect(
            self.start_convert_callback
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            description
        )


        layout.addWidget(
            start_button
        )



        self.setLayout(
            layout
        )