from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton
)


from PySide6.QtCore import Signal





class ConvertToolbar(QWidget):


    # ==========================
    # SIGNALS
    # ==========================

    add_image_clicked = Signal()

    add_multiple_clicked = Signal()

    add_folder_clicked = Signal()

    remove_selected_clicked = Signal()

    delete_all_clicked = Signal()

    convert_selected_clicked = Signal()

    convert_all_clicked = Signal()



    def __init__(self):

        super().__init__()


        self.init_ui()





    def init_ui(self):


        layout = QHBoxLayout()



        # ==========================
        # BUTTONS
        # ==========================


        self.add_image_button = QPushButton(
            "Add Image"
        )


        self.add_multiple_button = QPushButton(
            "Add Multiple Images"
        )


        self.add_folder_button = QPushButton(
            "Add Folder"
        )


        self.remove_button = QPushButton(
            "Remove Selected"
        )


        self.delete_all_button = QPushButton(
            "Delete All"
        )


        self.convert_selected_button = QPushButton(
            "Convert Selected"
        )


        self.convert_all_button = QPushButton(
            "Convert All"
        )



        # ==========================
        # CONNECT SIGNAL
        # ==========================


        self.add_image_button.clicked.connect(

            self.add_image_clicked.emit

        )


        self.add_multiple_button.clicked.connect(

            self.add_multiple_clicked.emit

        )


        self.add_folder_button.clicked.connect(

            self.add_folder_clicked.emit

        )


        self.remove_button.clicked.connect(

            self.remove_selected_clicked.emit

        )


        self.delete_all_button.clicked.connect(

            self.delete_all_clicked.emit

        )


        self.convert_selected_button.clicked.connect(

            self.convert_selected_clicked.emit

        )


        self.convert_all_button.clicked.connect(

            self.convert_all_clicked.emit

        )



        # ==========================
        # ADD TO LAYOUT
        # ==========================


        buttons = [

            self.add_image_button,

            self.add_multiple_button,

            self.add_folder_button,

            self.remove_button,

            self.delete_all_button,

            self.convert_selected_button,

            self.convert_all_button

        ]



        for button in buttons:

            layout.addWidget(
                button
            )



        self.setLayout(
            layout
        )





    # ==========================
    # STATE CONTROL
    # ==========================


    def set_processing(
            self,
            state=True
    ):


        self.convert_selected_button.setEnabled(
            not state
        )


        self.convert_all_button.setEnabled(
            not state
        )