from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QPushButton,
    QLabel,
    QFileDialog,
    QFrame
)

from PySide6.QtCore import Qt

from app.core.config import get_default_output



class OutputPanel(QWidget):


    def __init__(self):

        super().__init__()


        self.custom_folder = None


        self.init_ui()



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



            QLabel#description {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#path {

                background:#181F2D;

                border:1px solid #30384A;

                border-radius:12px;

                color:#DCE6FF;

                padding:12px;

                font-size:12px;

            }



            QLabel#caption {

                color:#7F8898;

                font-size:11px;

                font-weight:600;

            }



            QRadioButton {

                color:#D1D5DB;

                font-size:13px;

                font-weight:600;

                spacing:10px;

            }



            QRadioButton::indicator {

                width:16px;

                height:16px;

                border-radius:8px;

                border:2px solid #4B5563;

            }



            QRadioButton::indicator:checked {

                background:#4F8CFF;

                border-color:#4F8CFF;

            }



            QPushButton {

                background:#1B2230;

                border:1px solid #30384A;

                border-radius:12px;

                color:#E5E7EB;

                padding:12px 18px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background:#273147;

                border-color:#4F8CFF;

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
            20,
            20,
            20,
            20
        )


        layout.setSpacing(
            14
        )



        # =====================================
        # HEADER
        # =====================================


        title = QLabel(
            "📁 Output Destination"
        )


        title.setObjectName(
            "title"
        )


        desc = QLabel(
            "Choose where converted WEBP files will be stored."
        )


        desc.setObjectName(
            "description"
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            desc
        )


        layout.addSpacing(
            8
        )



        # =====================================
        # DEFAULT OPTION
        # =====================================


        self.default_radio = QRadioButton(
            "Default Location"
        )


        self.default_radio.setChecked(
            True
        )


        default_path = QLabel(
            str(
                get_default_output()
            )
        )


        default_path.setObjectName(
            "path"
        )


        layout.addWidget(
            self.default_radio
        )


        layout.addWidget(
            default_path
        )



        # =====================================
        # CUSTOM OPTION
        # =====================================


        self.custom_radio = QRadioButton(
            "Custom Folder"
        )


        layout.addWidget(
            self.custom_radio
        )


        self.folder_button = QPushButton(
            "📁 Select Folder"
        )


        self.folder_button.setMinimumHeight(
            42
        )


        layout.addWidget(
            self.folder_button
        )



        # =====================================
        # CURRENT PATH
        # =====================================


        caption = QLabel(
            "Current Output Path"
        )


        caption.setObjectName(
            "caption"
        )


        self.folder_label = QLabel(
            str(
                get_default_output()
            )
        )


        self.folder_label.setObjectName(
            "path"
        )


        self.folder_label.setWordWrap(
            True
        )



        layout.addWidget(
            caption
        )


        layout.addWidget(
            self.folder_label
        )


        layout.addStretch()



        self.folder_button.clicked.connect(
            self.select_folder
        )


        root.addWidget(
            card
        )



    # =====================================
    # LOGIC ORIGINAL
    # =====================================


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