from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QPushButton,
    QLabel,
    QFileDialog,
    QFrame
)

from app.core.config import get_default_output



from app.styles.theme import THEME

class OutputPanel(QWidget):


    def __init__(self):

        super().__init__()


        self.custom_folder = None


        self.init_ui()



    def init_ui(self):


        self.setStyleSheet(
            THEME["output_panel"]
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