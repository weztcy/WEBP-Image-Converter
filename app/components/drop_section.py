from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from app.widgets.drop_area import DropArea



class DropSection(QWidget):


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



            QFrame#card {

                background-color:#151922;

                border:1px solid #242B3A;

                border-radius:24px;

            }



            QFrame#dropZone {

                background-color:#10141C;

                border:2px dashed #354156;

                border-radius:22px;

            }



            QFrame#dropZone:hover {

                border-color:#4F8CFF;

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



            QLabel#uploadIcon {

                background-color:#1D2940;

                color:#7EA6FF;

                border-radius:32px;

                font-size:28px;

                font-weight:700;

            }



            QLabel#dropText {

                color:#F3F4F6;

                font-size:16px;

                font-weight:700;

            }



            QLabel#hint {

                color:#7F8898;

                font-size:12px;

            }



            QLabel#badge {

                background-color:#1D2330;

                border:1px solid #30384A;

                border-radius:10px;

                color:#DCE6FF;

                padding:6px 10px;

                font-size:11px;

                font-weight:600;

            }



            QPushButton {

                background-color:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

                border-radius:14px;

                text-align:left;

                padding:14px 16px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background-color:#242E42;

                border-color:#4F8CFF;

            }



            QPushButton:pressed {

                background-color:#151B27;

            }

            """
        )



        main = QHBoxLayout(self)

        main.setContentsMargins(
            0,
            0,
            0,
            0
        )

        main.setSpacing(
            18
        )



        # ==================================================
        # LEFT DROP WORKSPACE
        # ==================================================


        drop_card = QFrame()

        drop_card.setObjectName(
            "card"
        )


        drop_layout = QVBoxLayout(
            drop_card
        )

        drop_layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        drop_layout.setSpacing(
            14
        )


        title = QLabel(
            "Import Images"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Drag your images into the workspace or choose files manually."
        )

        subtitle.setObjectName(
            "subtitle"
        )



        # DROP AREA


        self.drop_area = DropArea()


        self.drop_area.setMinimumHeight(
            240
        )


        self.drop_area.setObjectName(
            "dropZone"
        )


        self.drop_area.setText(
            ""
        )


        drop_area_layout = QVBoxLayout(
            self.drop_area
        )


        drop_area_layout.setAlignment(
            Qt.AlignCenter
        )

        drop_area_layout.setSpacing(
            12
        )



        icon = QLabel(
            "↑"
        )

        icon.setObjectName(
            "uploadIcon"
        )


        icon.setFixedSize(
            64,
            64
        )


        icon.setAlignment(
            Qt.AlignCenter
        )



        drop_text = QLabel(
            "Drop images here"
        )

        drop_text.setObjectName(
            "dropText"
        )


        drop_text.setAlignment(
            Qt.AlignCenter
        )



        drop_hint = QLabel(
            "or select images from your computer"
        )

        drop_hint.setObjectName(
            "hint"
        )


        drop_hint.setAlignment(
            Qt.AlignCenter
        )



        drop_area_layout.addWidget(
            icon,
            0,
            Qt.AlignCenter
        )

        drop_area_layout.addWidget(
            drop_text
        )

        drop_area_layout.addWidget(
            drop_hint
        )



        badge_row = QHBoxLayout()

        badge_row.setAlignment(
            Qt.AlignCenter
        )

        badge_row.setSpacing(
            8
        )


        for text in [
            "JPG",
            "JPEG",
            "PNG",
            "WEBP"
        ]:

            badge = QLabel(
                text
            )

            badge.setObjectName(
                "badge"
            )

            badge_row.addWidget(
                badge
            )


        drop_layout.addWidget(
            title
        )

        drop_layout.addWidget(
            subtitle
        )

        drop_layout.addWidget(
            self.drop_area
        )

        drop_layout.addLayout(
            badge_row
        )



        # ==================================================
        # RIGHT ACTION PANEL
        # ==================================================


        action_card = QFrame()

        action_card.setObjectName(
            "card"
        )


        action_layout = QVBoxLayout(
            action_card
        )


        action_layout.setContentsMargins(
            20,
            24,
            20,
            24
        )


        action_layout.setSpacing(
            14
        )


        action_title = QLabel(
            "Quick Import"
        )

        action_title.setObjectName(
            "title"
        )


        action_desc = QLabel(
            "Choose the fastest way to load your images."
        )

        action_desc.setObjectName(
            "subtitle"
        )


        self.add_image_button = QPushButton(
            "＋   Add Single Image"
        )


        self.add_multiple_button = QPushButton(
            "▦   Add Multiple Images"
        )


        self.add_folder_button = QPushButton(
            "▣   Import Folder"
        )



        info = QLabel(
            "✓ Batch conversion ready\n"
            "✓ Folder scanning supported\n"
            "✓ Optimized workflow"
        )

        info.setObjectName(
            "hint"
        )



        action_layout.addWidget(
            action_title
        )

        action_layout.addWidget(
            action_desc
        )

        action_layout.addSpacing(
            10
        )

        action_layout.addWidget(
            self.add_image_button
        )

        action_layout.addWidget(
            self.add_multiple_button
        )

        action_layout.addWidget(
            self.add_folder_button
        )

        action_layout.addStretch()

        action_layout.addWidget(
            info
        )



        main.addWidget(
            drop_card,
            3
        )


        main.addWidget(
            action_card,
            1
        )