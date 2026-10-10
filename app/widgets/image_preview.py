from PySide6.QtWidgets import QLabel

from PySide6.QtGui import (
    QPixmap,
    QFont
)

from PySide6.QtCore import (
    Qt,
    QSize
)


from app.core.thumbnail_cache import ThumbnailCache
from app.core.preview_loader import PreviewLoader





class ImagePreview(QLabel):


    def __init__(self):

        super().__init__()



        self.preview_cache = ThumbnailCache(
            size=600
        )


        self.loader = None


        self.pixmap_cache = {}



        self.current_pixmap = None



        # ==========================
        # PREMIUM PREVIEW STYLE
        # ==========================


        self.setStyleSheet(
            """

            QLabel {

                background:#10141C;

                border:1px solid #242938;

                border-radius:18px;

                color:#667085;

                font-size:14px;

                font-weight:600;

            }

            """
        )



        self.setAlignment(
            Qt.AlignCenter
        )


        # 16:10 ratio base

        self.setMinimumSize(
            QSize(
                480,
                300
            )
        )


        self.setMaximumHeight(
            360
        )


        self.show_empty()





    # ==========================
    # SHOW IMAGE
    # ==========================


    def show_image(
            self,
            image
    ):


        if image is None:

            self.show_empty()

            return



        key = str(
            image.path
        )



        # CACHE

        if key in self.pixmap_cache:


            self.current_pixmap = (
                self.pixmap_cache[key]
            )


            self.update_preview_size()

            return





        # ASYNC LOAD


        if self.loader:

            self.loader.quit()



        self.loader = PreviewLoader(

            image,

            self.preview_cache

        )



        self.loader.preview_ready.connect(

            lambda pixmap:

            self.set_preview(

                key,

                pixmap

            )

        )


        self.loader.start()





    # ==========================
    # SET PREVIEW
    # ==========================


    def set_preview(
            self,
            key,
            pixmap
    ):


        if pixmap.isNull():

            self.show_empty()

            return



        self.pixmap_cache[key] = pixmap


        self.current_pixmap = pixmap


        self.update_preview_size()





    # ==========================
    # KEEP RATIO
    # ==========================


    def update_preview_size(self):


        if self.current_pixmap is None:

            return



        scaled = self.current_pixmap.scaled(

            self.size(),

            Qt.KeepAspectRatio,

            Qt.SmoothTransformation

        )


        self.setPixmap(
            scaled
        )





    # ==========================
    # RESIZE EVENT
    # ==========================


    def resizeEvent(
            self,
            event
    ):


        self.update_preview_size()


        super().resizeEvent(
            event
        )





    # ==========================
    # EMPTY STATE
    # ==========================


    def show_empty(self):


        self.current_pixmap = None


        self.clear()


        self.setText(
            "🖼\n\nImage Preview\n\nSelect an image to preview"
        )


        self.setAlignment(
            Qt.AlignCenter
        )