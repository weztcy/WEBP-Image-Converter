from PySide6.QtWidgets import QLabel


from PySide6.QtGui import QPixmap


from PySide6.QtCore import Qt


from app.core.thumbnail_cache import ThumbnailCache




class ImagePreview(QLabel):


    def __init__(self):

        super().__init__()


        self.preview_cache = ThumbnailCache(
            size=800
        )


        self.setAlignment(
            Qt.AlignCenter
        )


        self.setMinimumHeight(
            300
        )


        self.show_empty()



    def show_image(self, image):


        if image is None:

            self.show_empty()

            return



        preview_path = (
            self.preview_cache
            .create_preview(
                image.path
            )
        )



        if preview_path is None:

            self.show_empty()

            return



        pixmap = QPixmap(
            str(preview_path)
        )



        if pixmap.isNull():

            self.show_empty()

            return



        pixmap = pixmap.scaled(

            400,

            400,

            Qt.KeepAspectRatio,

            Qt.SmoothTransformation

        )


        self.setPixmap(
            pixmap
        )



    def show_empty(self):


        self.clear()


        self.setText(
            "Image Preview"
        )