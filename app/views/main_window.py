from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QLabel,
    QFrame,
    QPushButton
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

from app.views.home_page import HomePage
from app.views.convert_page import ConvertPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.init_window()
        self.init_ui()



    # ==================================
    # WINDOW CONFIG
    # ==================================

    def init_window(self):

        self.setWindowTitle(
            "WEBP Converter Pro"
        )

        self.setMinimumSize(
            1100,
            720
        )
        
        # OPEN MAXIMIZED
        self.showMaximized()


        self.pages = QStackedWidget()

        self.setStyleSheet(
            """
            QMainWindow {

                background-color: #0F1115;

            }


            QWidget {

                font-family: "Inter", "Segoe UI";

            }


            QFrame#header {

                background-color: #151922;

                border-bottom: 1px solid #242938;

            }


            QFrame#footer {

                background-color: #11141A;

                border-top: 1px solid #242938;

            }


            QLabel#brand {

                color: #F9FAFB;

                font-size: 16px;

                font-weight: 800;

            }


            QLabel#version {

                color: #8F98A8;

                font-size: 12px;

            }


            QLabel#status {

                color: #34D399;

                font-size: 12px;

                font-weight: 600;

            }


            QPushButton#iconButton {

                background-color: transparent;

                border: none;

                color: #9CA3AF;

                font-size: 18px;

                padding: 6px;

            }


            QPushButton#iconButton:hover {

                color: #FFFFFF;

                background-color: #202633;

                border-radius: 8px;

            }

            """
        )



    # ==================================
    # UI BUILD
    # ==================================

    def init_ui(self):

        container = QWidget()

        root = QVBoxLayout(container)

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root.setSpacing(
            0
        )


        # ==============================
        # HEADER
        # ==============================

        header = QFrame()

        header.setObjectName(
            "header"
        )


        header_layout = QHBoxLayout(header)

        header_layout.setContentsMargins(
            28,
            16,
            28,
            16
        )


        brand_container = QHBoxLayout()

        brand_icon = QLabel(
            "✨"
        )

        brand_icon.setAlignment(
            Qt.AlignCenter
        )


        brand_icon.setFixedSize(
            36,
            36
        )


        brand_icon.setStyleSheet(
            """
            QLabel {

                background-color: #4F8CFF;

                color:white;

                border-radius:18px;

                font-size:16px;

                font-weight:800;

            }
            """
        )


        brand_text = QVBoxLayout()

        brand = QLabel(
            "WEBP Converter Pro"
        )

        brand.setObjectName(
            "brand"
        )


        version = QLabel(
            "Professional WEBP Conversion Workspace"
        )

        version.setObjectName(
            "version"
        )


        brand_text.addWidget(
            brand
        )

        brand_text.addWidget(
            version
        )


        brand_container.addWidget(
            brand_icon
        )

        brand_container.addLayout(
            brand_text
        )


        header_layout.addLayout(
            brand_container
        )


        header_layout.addStretch()


        settings_button = QPushButton(
            "⚙"
        )

        settings_button.setObjectName(
            "iconButton"
        )


        header_layout.addWidget(
            settings_button
        )


        root.addWidget(
            header
        )



        # ==============================
        # PAGE CONTENT
        # ==============================

        self.pages = QStackedWidget()


        self.home_page = HomePage(
            self.show_convert_page
        )


        self.convert_page = ConvertPage()


        self.pages.addWidget(
            self.home_page
        )


        self.pages.addWidget(
            self.convert_page
        )


        content_frame = QFrame()

        content_layout = QVBoxLayout(
            content_frame
        )


        content_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        content_layout.addWidget(
            self.pages
        )


        root.addWidget(
            content_frame,
            1
        )



        # ==============================
        # FOOTER
        # ==============================

        footer = QFrame()

        footer.setObjectName(
            "footer"
        )


        footer_layout = QHBoxLayout(
            footer
        )


        footer_layout.setContentsMargins(
            28,
            10,
            28,
            10
        )


        status = QLabel(
            "●  Ready"
        )

        status.setObjectName(
            "status"
        )


        footer_text = QLabel(
            "WEBP Converter Pro • Premium Desktop Utility"
        )

        footer_text.setStyleSheet(
            """
            QLabel {

                color:#7F8898;

                font-size:12px;

            }
            """
        )


        footer_layout.addWidget(
            status
        )

        footer_layout.addStretch()

        footer_layout.addWidget(
            footer_text
        )


        root.addWidget(
            footer
        )


        self.setCentralWidget(
            container
        )



    # ==================================
    # NAVIGATION
    # ==================================

    def show_convert_page(self):

        self.pages.setCurrentWidget(
            self.convert_page
        )