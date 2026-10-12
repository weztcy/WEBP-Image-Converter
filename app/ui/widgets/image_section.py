from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from app.services.image_service import ImageLibrary
from app.ui.widgets.image_list import ImageList
from app.ui.widgets.image_preview import ImagePreview



from app.styles.theme import THEME

class ImageSection(QWidget):


    def __init__(self):

        super().__init__()

        self.library = ImageLibrary()

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

        self.library.changed.connect(
            self.update_counter
        )

        self.library.image_added.connect(
            self._on_image_added
        )

        self.library.selection_changed.connect(
            self._on_selection
        )


    # ======================================
    # DATA ACCESS (backwards compatible)
    # ======================================

    @property
    def images(self):
        """Live view of the underlying image collection."""

        return self.library.images


    @property
    def selected_image(self):

        return self.library.selected_image


    @selected_image.setter
    def selected_image(self, image):

        self.library.set_selected(
            image
        )



    # ======================================
    # UI
    # ======================================

    def init_ui(self):


        self.setStyleSheet(
            THEME["image_section"]
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

        self.library.set_selected(
            img
        )


    # ======================================
    # LIBRARY EVENTS
    # ======================================

    def _on_selection(
            self,
            image
    ):

        self.preview.show_image(
            image
        )


    def _on_image_added(
            self,
            image
    ):

        self.image_list.add_images(
            [image]
        )


    def add_images(
            self,
            files
    ):

        imgs = self.library.add_files(
            files
        )


        self.image_list.add_images(
            imgs
        )


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

        self.library.add_folder(
            folder
        )


    def get_selected(self):

        return self.library.get_selected()


    def get_images(self):

        return self.library.get_images()


    def remove_selected(self):

        deleted = self.selected_image


        if deleted is None:

            return


        self.library.remove_selected()


        # ImageList.remove_selected() otomatis :
        # - menghapus item dari list widget
        # - memilih gambar berikutnya
        # - emit image_selected(gambar_baru)
        #   -> _selected() meng-update selection library + preview
        # - jika list kosong, emit None
        #   -> selection = None & preview kosong
        self.image_list.remove_selected()


    def clear(self):

        self.library.clear()


        self.image_list.clear()