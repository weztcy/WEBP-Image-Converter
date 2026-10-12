from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QSizePolicy
)

from PySide6.QtCore import (
    QSize,
    Signal,
    Qt
)


from functools import partial


from app.core.thumbnail_cache import ThumbnailCache
from app.core.thumbnail_loader import ThumbnailLoader
from app.styles.dimensions import DIMENSIONS





from app.styles.theme import THEME

class ImageList(QListWidget):


    image_selected = Signal(object)



    def __init__(self):

        super().__init__()

        self.columns = DIMENSIONS["image_list"]["columns"]

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
            THEME["image_list"]
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
            DIMENSIONS["image_list"]["card_width_min"],
            card_width
        )


        return QSize(
            card_width,
            DIMENSIONS["image_list"]["card_height"]
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



        # sinkronkan currentItem (fokus keyboard) dengan item yang
        # benar-benar diklik, supaya remove_selected selalu konsisten
        self.setCurrentItem(
            item
        )


        self.current_selected_item = item



        self.image_selected.emit(

            item.data(100)

        )





    # ==================================
    # REMOVE
    # ==================================

    def remove_selected(self):


        # gunakan item yang benar-benar aktif (hasil klik terakhir),
        # bukan currentItem() yang hanya menandai fokus keyboard
        item = self.current_selected_item or self.currentItem()


        if item is None:

            return None


        image = item.data(100)

        row = self.row(
            item
        )


        if image:

            self.loaded_paths.discard(

                str(image.path)

            )


        self.takeItem(

            row

        )


        self.current_selected_item = None



        # ----------------------------------------------------
        # Tentukan gambar berikutnya yang otomatis terpilih :
        # - item yang sekarang menempati index yang sama
        #   (item "berikutnya" yang bergeser ke posisi item
        #   yang dihapus)
        # - atau item terakhir jika yang dihapus adalah item
        #   paling akhir di list
        # ----------------------------------------------------

        next_item = None


        if self.count() > 0:

            next_index = min(
                row,
                self.count() - 1
            )

            next_item = self.item(
                next_index
            )

            next_item.setSelected(
                True
            )

            self.setCurrentItem(
                next_item
            )

            self.scrollToItem(
                next_item
            )

            self.current_selected_item = next_item


        # Sinkronkan state consumer (ImageSection.selected_image
        # dan preview) ke gambar baru secara langsung
        if next_item is not None:

            self.image_selected.emit(

                next_item.data(100)

            )

        else:

            self.image_selected.emit(
                None
            )


        # kembalikan gambar yang dihapus supaya caller bisa
        # menghapusnya dari datasource
        return image



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
            THEME["image_card"]
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