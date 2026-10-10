from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QSizePolicy
)

from PySide6.QtGui import (
    QIcon,
    QPixmap
)

from PySide6.QtCore import (
    QSize,
    Signal,
    Qt
)


from functools import partial


from app.core.thumbnail_cache import ThumbnailCache
from app.core.thumbnail_loader import ThumbnailLoader





class ImageList(QListWidget):


    image_selected = Signal(object)



    def __init__(self):

        super().__init__()

        self.columns = 4

        self.current_selected_item = None


        self.thumbnail_cache = ThumbnailCache(
            size=90
        )


        self.loading_threads = {}

        self.loaded_paths = set()



        self.setup_ui()



        self.itemClicked.connect(
            self.handle_click
        )

    def resizeEvent(
            self,
            event
    ):


        item_size = self.calculate_item_size()


        self.setGridSize(
            QSize(
                item_size.width()+12,
                item_size.height()+12
            )
        )


        for i in range(self.count()):

            item = self.item(i)

            item.setSizeHint(
                item_size
            )


        super().resizeEvent(event)


    # ==================================
    # UI
    # ==================================

    def setup_ui(self):


        self.setViewMode(
            QListWidget.IconMode
        )


        self.setFlow(
            QListWidget.LeftToRight
        )


        self.setWrapping(
            True
        )


        self.setResizeMode(
            QListWidget.Adjust
        )


        self.setSpacing(
            12
        )
        self.setViewportMargins(
            0,
            0,
            0,
            0
        )

        self.setIconSize(
            QSize(
                90,
                90
            )
        )


        self.setUniformItemSizes(
            False
        )


        self.setMovement(
            QListWidget.Static
        )


        self.setStyleSheet(
            """

            QListWidget {

                background:transparent;

                border:none;

                outline:none;

            }


            QListWidget::item {

                background:#151922;

                border:1px solid #242938;

                border-radius:16px;

                padding:10px;

                margin:4px;

            }



            QListWidget::item:hover {

                border-color:#4F8CFF;

                background:#192131;

            }



            QListWidget::item:selected {

                background:#17243A;

                border:1px solid #4F8CFF;

            }

            """
        )



    def calculate_item_size(self):


        viewport_width = self.viewport().width()


        spacing = self.spacing()


        # total jarak antar card
        total_spacing = (
            spacing * (self.columns + 1)
        )


        card_width = (
            viewport_width - total_spacing
        ) // self.columns



        # batas minimum supaya tidak rusak
        card_width = max(
            180,
            card_width
        )


        return QSize(
            card_width,
            115
        )

    # ==================================
    # ADD IMAGE
    # ==================================

    def add_images(
            self,
            images
    ):


        for image in images:


            path = str(
                image.path
            )



            if path in self.loaded_paths:

                continue



            self.loaded_paths.add(
                path
            )



            item = QListWidgetItem()



            item.setSizeHint(
                self.calculate_item_size()
            )


            item.setData(
                100,
                image
            )



            widget = ImageCard()



            widget.set_data(
                image
            )



            item.setData(
                200,
                widget
            )



            self.addItem(
                item
            )


            self.setItemWidget(
                item,
                widget
            )



            self.load_thumbnail(
                item,
                image
            )





    # ==================================
    # THUMBNAIL
    # ==================================

    def load_thumbnail(
            self,
            item,
            image
    ):


        key = str(
            image.path
        )


        loader = ThumbnailLoader(

            image,

            self.thumbnail_cache

        )



        loader.thumbnail_ready.connect(

            lambda image, pixmap, item=item:

            self.set_thumbnail(
                item,
                pixmap
            )

        )



        loader.finished.connect(

            partial(
                self.remove_loader,
                key,
                loader
            )

        )



        self.loading_threads[key] = loader


        loader.start()





    def set_thumbnail(
            self,
            item,
            pixmap
    ):


        if pixmap.isNull():

            return



        widget = item.data(
            200
        )


        if widget:

            widget.set_thumbnail(
                pixmap
            )





    def remove_loader(
            self,
            key,
            loader
    ):


        if key in self.loading_threads:

            del self.loading_threads[key]


        loader.deleteLater()





    # ==================================
    # CLICK
    # ==================================

    def handle_click(
            self,
            item
    ):


        if self.current_selected_item:

            old = self.current_selected_item

            old.setSelected(False)



        self.current_selected_item = item



        self.image_selected.emit(

            item.data(100)

        )





    # ==================================
    # REMOVE
    # ==================================

    def remove_selected(self):


        item = self.currentItem()


        if item:


            image = item.data(100)


            if image:

                self.loaded_paths.discard(

                    str(image.path)

                )



            self.takeItem(

                self.row(item)

            )


            self.current_selected_item = None





    # ==================================
    # CLEAR
    # ==================================

    def clear(self):


        for loader in self.loading_threads.values():

            loader.quit()

            loader.wait()



        self.loading_threads.clear()


        self.loaded_paths.clear()



        super().clear()


        self.current_selected_item = None





    # ==================================
    # FORMAT
    # ==================================

    def format_size(
            self,
            size
    ):


        kb = size / 1024

        mb = kb / 1024


        if mb >= 1:

            return f"{mb:.2f} MB"


        return f"{kb:.2f} KB"







# ==================================================
# IMAGE CARD
# ==================================================

class ImageCard(QFrame):


    def __init__(self):

        super().__init__()



        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )


        self.init_ui()



    def init_ui(self):


        self.setStyleSheet(
            """

            QFrame {

                background:transparent;

            }



            QLabel#name {

                color:#F9FAFB;

                font-size:12px;

                font-weight:700;

            }



            QLabel#meta {

                color:#98A2B3;

                font-size:11px;

            }



            QLabel#badge {

                background:#1D2940;

                color:#8BB0FF;

                padding:3px 8px;

                border-radius:8px;

                font-size:10px;

                font-weight:700;

            }

            """
        )



        layout = QHBoxLayout(
            self
        )


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout.setSpacing(
            12
        )

        layout.setStretch(0,0)
        layout.setStretch(1,1)



        self.thumbnail = QLabel()

        self.thumbnail.setMinimumSize(
            70,
            70
        )


        self.thumbnail.setMaximumSize(
            80,
            80
        )


        self.thumbnail.setAlignment(
            Qt.AlignCenter
        )


        self.thumbnail.setStyleSheet(
            """

            QLabel {

                background:#0F131B;

                border-radius:10px;

            }

            """
        )



        layout.addWidget(
            self.thumbnail
        )



        info = QVBoxLayout()


        self.name = QLabel()

        self.name.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )


        self.name.setWordWrap(
            False
        )

        self.name.setObjectName(
            "name"
        )


        self.meta = QLabel()

        self.meta.setObjectName(
            "meta"
        )


        self.badge = QLabel()

        self.badge.setObjectName(
            "badge"
        )


        info.addWidget(
            self.name
        )


        info.addWidget(
            self.badge
        )


        info.addWidget(
            self.meta
        )


        info.addStretch()



        layout.addLayout(
            info
        )



    def set_data(
            self,
            image
    ):


        self.name.setText(
            image.filename
        )


        ext = image.extension.replace(
            ".",
            ""
        ).upper()


        self.badge.setText(
            ext
        )


        self.meta.setText(
            self.format_size(
                image.get_size()
            )
        )



    def set_thumbnail(
            self,
            pixmap
    ):


        size = self.thumbnail.size()


        scaled = pixmap.scaled(

            size,

            Qt.KeepAspectRatio,

            Qt.SmoothTransformation

        )


        self.thumbnail.setPixmap(
            scaled
        )



    def format_size(
            self,
            size
    ):


        kb = size / 1024

        mb = kb / 1024


        if mb >= 1:

            return f"{mb:.2f} MB"


        return f"{kb:.2f} KB"