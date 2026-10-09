from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton
)

from app.widgets.drop_area import DropArea


class DropSection(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):

        main = QHBoxLayout(self)


        self.drop_area = DropArea()


        button_layout = QVBoxLayout()


        self.add_image_button = QPushButton(
            "Add Image"
        )

        self.add_multiple_button = QPushButton(
            "Add Multiple Images"
        )

        self.add_folder_button = QPushButton(
            "Add Folder"
        )


        button_layout.addWidget(
            self.add_image_button
        )

        button_layout.addWidget(
            self.add_multiple_button
        )

        button_layout.addWidget(
            self.add_folder_button
        )


        main.addWidget(
            self.drop_area,
            1
        )


        main.addLayout(
            button_layout,
            1
        )