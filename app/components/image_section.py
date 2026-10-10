from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from app.widgets.image_list import ImageList
from app.widgets.image_preview import ImagePreview
from app.core.image_loader import load_files



class ImageSection(QWidget):


    def __init__(self):

        super().__init__()


        self.images = []

        self.selected_image = None


        self.image_list = ImageList()

        self.preview = ImagePreview()



        self.remove_button = QPushButton(
            "−  Remove Selected"
        )


        self.delete_button = QPushButton(
            "×  Delete All"
        )


        self.count_label = QLabel(
            "0 Images"
        )


        self.init_ui()


        self.image_list.image_selected.connect(
            self._selected
        )



    # ======================================
    # UI
    # ======================================

    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }


            QFrame#libraryCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }



            QFrame#innerPanel {

                background:#10141C;

                border:1px solid #202735;

                border-radius:18px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:18px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }



            QLabel#counter {

                background:#1D2940;

                color:#8BB0FF;

                padding:7px 14px;

                border-radius:12px;

                font-size:12px;

                font-weight:700;

            }



            QPushButton {

                background:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

                border-radius:12px;

                padding:10px 18px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background:#273147;

                border-color:#4F8CFF;

            }



            QPushButton#danger:hover {

                border-color:#EF4444;

                color:#FCA5A5;

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
            "libraryCard"
        )



        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            22,
            22,
            22,
            22
        )


        layout.setSpacing(
            16
        )



        # ======================================
        # HEADER
        # ======================================


        header = QHBoxLayout()


        text_layout = QVBoxLayout()


        title = QLabel(
            "🖼 Image Library"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Manage imported images before WEBP conversion."
        )

        subtitle.setObjectName(
            "subtitle"
        )


        text_layout.addWidget(
            title
        )


        text_layout.addWidget(
            subtitle
        )



        self.count_label.setObjectName(
            "counter"
        )


        self.count_label.setAlignment(
            Qt.AlignCenter
        )



        header.addLayout(
            text_layout
        )


        header.addStretch()


        header.addWidget(
            self.count_label
        )


        layout.addLayout(
            header
        )



        # ======================================
        # MAIN WORKSPACE
        # ======================================


        content = QHBoxLayout()


        content.setSpacing(
            16
        )



        # ======================================
        # LEFT SIDE
        # LIST + ACTION
        # ======================================


        left_side = QVBoxLayout()


        left_side.setSpacing(
            12
        )



        list_frame = QFrame()
        list_frame.setFixedHeight(
            360
        )
        list_frame.setObjectName(
            "innerPanel"
        )



        list_layout = QVBoxLayout(
            list_frame
        )


        list_layout.setContentsMargins(
            12,
            12,
            12,
            12
        )



        list_layout.addWidget(
            self.image_list
        )



        left_side.addWidget(
            list_frame,
            1
        )



        # ===============================
        # ACTION BAR
        # ===============================


        actions = QHBoxLayout()


        actions.addStretch()



        self.delete_button.setObjectName(
            "danger"
        )


        actions.addWidget(
            self.remove_button
        )


        actions.addWidget(
            self.delete_button
        )


        left_side.addLayout(
            actions
        )



        # ======================================
        # RIGHT SIDE
        # PREVIEW FULL HEIGHT
        # ======================================


        preview_frame = QFrame()

        preview_frame.setObjectName(
            "innerPanel"
        )



        preview_layout = QVBoxLayout(
            preview_frame
        )


        preview_layout.setContentsMargins(
            12,
            12,
            12,
            12
        )


        preview_layout.setSpacing(
            10
        )



        preview_title = QLabel(
            "Preview"
        )


        preview_title.setStyleSheet(
            """

            QLabel {

                color:#98A2B3;

                font-size:12px;

                font-weight:700;

            }

            """
        )


        preview_layout.addWidget(
            preview_title
        )



        preview_layout.addWidget(
            self.preview,
            1
        )



        # ======================================
        # WIDTH RATIO
        # ======================================


        content.addLayout(
            left_side,
            2
        )


        content.addWidget(
            preview_frame,
            1
        )


        layout.addLayout(
            content,
            1
        )



        root.addWidget(
            card
        )



        self.remove_button.clicked.connect(
            self.remove_selected
        )


        self.delete_button.clicked.connect(
            self.clear
        )



    # ======================================
    # COUNTER
    # ======================================

    def update_counter(self):

        self.count_label.setText(
            f"{len(self.images)} Images"
        )



    # ======================================
    # IMAGE LOGIC
    # ======================================


    def _selected(
            self,
            img
    ):

        self.selected_image = img


        self.preview.show_image(
            img
        )



    def add_images(
            self,
            files
    ):

        imgs = load_files(
            files
        )


        self.images.extend(
            imgs
        )


        self.image_list.add_images(
            imgs
        )


        self.update_counter()



    def add_paths(
            self,
            paths
    ):

        for p in paths:

            self.add_images(
                [p]
            )



    def add_folder(
            self,
            folder
    ):

        from app.core.image_scanner import ImageScanner


        self.scanner = ImageScanner(
            folder
        )


        self.scanner.image_found.connect(

            lambda x:

            (
                self.images.append(x),

                self.image_list.add_images(
                    [x]
                ),

                self.update_counter()

            )

        )


        self.scanner.start()



    def get_selected(self):

        return self.selected_image



    def get_images(self):

        return self.images



    def remove_selected(self):

        if self.selected_image in self.images:

            self.images.remove(
                self.selected_image
            )


        self.image_list.remove_selected()


        self.preview.show_empty()


        self.selected_image = None


        self.update_counter()



    def clear(self):

        self.images.clear()


        self.image_list.clear()


        self.preview.show_empty()


        self.selected_image = None


        self.update_counter()