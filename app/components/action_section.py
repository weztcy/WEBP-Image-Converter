from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Signal


class ActionSection(QWidget):

    convert_selected_clicked = Signal()
    convert_all_clicked = Signal()
    cancel_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)

        self.convert_selected_button = QPushButton("Convert Selected")
        self.convert_all_button = QPushButton("Convert All")
        self.cancel_button = QPushButton("Cancel")

        self.cancel_button.hide()

        self.convert_selected_button.clicked.connect(
            self.convert_selected_clicked.emit
        )
        self.convert_all_button.clicked.connect(
            self.convert_all_clicked.emit
        )
        self.cancel_button.clicked.connect(
            self.cancel_clicked.emit
        )

        layout.addWidget(self.convert_selected_button)
        layout.addWidget(self.convert_all_button)
        layout.addWidget(self.cancel_button)

    def set_processing(self, state=True):
        self.convert_selected_button.setVisible(not state)
        self.convert_all_button.setVisible(not state)
        self.cancel_button.setVisible(state)

        if state:
            self.layout().setStretch(0, 0)
            self.layout().setStretch(1, 0)
            self.layout().setStretch(2, 1)
        else:
            self.layout().setStretch(0, 1)
            self.layout().setStretch(1, 1)
            self.layout().setStretch(2, 0)