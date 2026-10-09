from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QPushButton,
    QLabel,
    QFileDialog
)


from app.core.config import get_default_output



class OutputPanel(QWidget):


    def __init__(self):

        super().__init__()


        self.custom_folder = None


        self.init_ui()



    def init_ui(self):

        layout = QVBoxLayout()



        self.default_radio = QRadioButton(
            "Default (Pictures/Image2WEBP)"
        )


        self.custom_radio = QRadioButton(
            "Custom Folder"
        )



        self.default_radio.setChecked(
            True
        )



        self.folder_button = QPushButton(
            "Select Folder"
        )


        self.folder_label = QLabel(
            str(
                get_default_output()
            )
        )



        self.folder_button.clicked.connect(
            self.select_folder
        )



        layout.addWidget(
            self.default_radio
        )


        layout.addWidget(
            self.custom_radio
        )


        layout.addWidget(
            self.folder_button
        )


        layout.addWidget(
            self.folder_label
        )



        self.setLayout(
            layout
        )



    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Output Folder"

        )



        if folder:

            self.custom_folder = folder


            self.custom_radio.setChecked(
                True
            )


            self.folder_label.setText(
                folder
            )



    def get_output_folder(self):

        if self.custom_radio.isChecked():

            if self.custom_folder:

                return self.custom_folder



        return str(
            get_default_output()
        )