from PySide6.QtCore import (
    QThread,
    Signal
)

from PySide6.QtGui import QPixmap


from app.core.thumbnail_cache import ThumbnailCache




class PreviewLoader(QThread):


    preview_ready = Signal(QPixmap)



    def __init__(
            self,
            image,
            cache
    ):

        super().__init__()


        self.image = image

        self.cache = cache



    def run(self):


        preview_path = (
            self.cache.create_preview(
                self.image.path
            )
        )


        if preview_path is None:

            self.preview_ready.emit(
                QPixmap()
            )

            return



        pixmap = QPixmap(
            str(preview_path)
        )


        self.preview_ready.emit(

            pixmap

        )