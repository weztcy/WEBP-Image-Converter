from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame
)

from PySide6.QtCore import Signal



class ActionSection(QWidget):


    convert_selected_clicked = Signal()

    convert_all_clicked = Signal()

    cancel_clicked = Signal()



    def __init__(self):

        super().__init__()

        self.init_ui()



    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#actionCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:22px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:16px;

                font-weight:800;

            }



            QLabel#desc {

                color:#98A2B3;

                font-size:12px;

            }



            QPushButton {

                height:48px;

                border-radius:14px;

                font-size:14px;

                font-weight:700;

            }



            QPushButton#primary {

                background:#4F8CFF;

                color:white;

                border:none;

            }



            QPushButton#primary:hover {

                background:#669BFF;

            }



            QPushButton#secondary {

                background:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

            }



            QPushButton#secondary:hover {

                background:#273147;

                border-color:#4F8CFF;

            }



            QPushButton#cancel {

                background:#2B1820;

                color:#FCA5A5;

                border:1px solid #7F1D1D;

            }



            QPushButton#cancel:hover {

                background:#401C26;

            }

            """
        )



        root = QHBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )



        card = QFrame()

        card.setObjectName(
            "actionCard"
        )


        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            22,
            20,
            22,
            20
        )


        layout.setSpacing(
            12
        )



        # =================================
        # HEADER
        # =================================


        title = QLabel(
            "🚀 Conversion Actions"
        )

        title.setObjectName(
            "title"
        )


        desc = QLabel(
            "Start converting selected images or process the complete library."
        )

        desc.setObjectName(
            "desc"
        )


        layout.addWidget(
            title
        )


        layout.addWidget(
            desc
        )



        # =================================
        # BUTTON AREA
        # =================================


        buttons = QHBoxLayout()

        buttons.setSpacing(
            12
        )



        self.convert_selected_button = QPushButton(
            "✓  Convert Selected"
        )

        self.convert_selected_button.setObjectName(
            "secondary"
        )



        self.convert_all_button = QPushButton(
            "⚡  Convert All"
        )

        self.convert_all_button.setObjectName(
            "primary"
        )



        self.cancel_button = QPushButton(
            "✕  Cancel Conversion"
        )

        self.cancel_button.setObjectName(
            "cancel"
        )


        self.cancel_button.hide()



        buttons.addWidget(
            self.convert_selected_button
        )


        buttons.addWidget(
            self.convert_all_button
        )


        buttons.addWidget(
            self.cancel_button
        )



        layout.addLayout(
            buttons
        )



        root.addWidget(
            card
        )



        # =================================
        # SIGNALS
        # =================================


        self.convert_selected_button.clicked.connect(
            self.convert_selected_clicked.emit
        )


        self.convert_all_button.clicked.connect(
            self.convert_all_clicked.emit
        )


        self.cancel_button.clicked.connect(
            self.cancel_clicked.emit
        )



    # =================================
    # PROCESS STATE
    # =================================


    def set_processing(
            self,
            state=True
    ):


        self.convert_selected_button.setVisible(
            not state
        )


        self.convert_all_button.setVisible(
            not state
        )


        self.cancel_button.setVisible(
            state
        )



        if state:


            self.cancel_button.setMinimumWidth(
                280
            )


        else:


            self.convert_selected_button.setMinimumWidth(
                220
            )


            self.convert_all_button.setMinimumWidth(
                220
            )