from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from app.widgets.settings_panel import SettingsPanel
from app.widgets.conversion_info import ConversionInfo
from app.widgets.output_panel import OutputPanel



class ConversionSection(QWidget):


    def __init__(self):

        super().__init__()


        self.settings_panel = SettingsPanel()

        self.info = ConversionInfo()

        self.output_panel = OutputPanel()


        self.init_ui()



    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#controlCard {

                background-color:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }



            QLabel#sectionLabel {

                color:#7EA6FF;

                font-size:12px;

                font-weight:700;

                letter-spacing:1px;

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

        root.setSpacing(
            0
        )



        card = QFrame()

        card.setObjectName(
            "controlCard"
        )


        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            24,
            24,
            24,
            24
        )


        layout.setSpacing(
            18
        )



        # =====================================
        # HEADER
        # =====================================


        header = QVBoxLayout()

        header.setSpacing(
            6
        )


        title = QLabel(
            "⚙ Conversion Control Center"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Configure compression settings, conversion profile, and output destination."
        )

        subtitle.setObjectName(
            "subtitle"
        )


        header.addWidget(
            title
        )

        header.addWidget(
            subtitle
        )



        layout.addLayout(
            header
        )



        # =====================================
        # INFO SECTION
        # =====================================


        info_title = QLabel(
            "CONVERSION OVERVIEW"
        )

        info_title.setObjectName(
            "sectionLabel"
        )


        layout.addWidget(
            info_title
        )


        layout.addWidget(
            self.info
        )



        # =====================================
        # SETTINGS + OUTPUT GRID
        # =====================================


        middle = QHBoxLayout()

        middle.setSpacing(
            18
        )



        settings_card = QFrame()

        settings_card.setStyleSheet(
            """
            QFrame {

                background:#10141C;

                border-radius:18px;

            }
            """
        )


        settings_layout = QVBoxLayout(
            settings_card
        )

        settings_layout.setContentsMargins(
            16,
            16,
            16,
            16
        )


        settings_title = QLabel(
            "Compression Settings"
        )

        settings_title.setStyleSheet(
            """
            QLabel {

                color:#F3F4F6;

                font-size:14px;

                font-weight:700;

            }
            """
        )


        settings_layout.addWidget(
            settings_title
        )


        settings_layout.addWidget(
            self.settings_panel
        )



        output_card = QFrame()


        output_card.setStyleSheet(
            """
            QFrame {

                background:#10141C;

                border-radius:18px;

            }

            """
        )


        output_layout = QVBoxLayout(
            output_card
        )


        output_layout.setContentsMargins(
            16,
            16,
            16,
            16
        )


        output_title = QLabel(
            "Output Destination"
        )


        output_title.setStyleSheet(
            """
            QLabel {

                color:#F3F4F6;

                font-size:14px;

                font-weight:700;

            }

            """
        )


        output_layout.addWidget(
            output_title
        )


        output_layout.addWidget(
            self.output_panel
        )



        middle.addWidget(
            settings_card,
            3
        )


        middle.addWidget(
            output_card,
            2
        )



        layout.addLayout(
            middle
        )


        root.addWidget(
            card
        )



    # =====================================
    # EXISTING API
    # =====================================


    def get_settings(self):

        return self.settings_panel.get_settings()



    def get_output_folder(self):

        return self.output_panel.get_output_folder()



    def set_profile(self, profile):

        self.settings_panel.set_profile(
            profile
        )



    def set_workers(self, workers):

        self.settings_panel.set_workers(
            workers
        )



    def update_statistics(self, data):

        if hasattr(self, "stats"):

            self.stats.update_stats(
                data
            )



    def reset(self):

        self.settings_panel.reset()

        self.output_panel.reset()