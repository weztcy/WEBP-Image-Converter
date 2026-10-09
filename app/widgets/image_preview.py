from PySide6.QtWidgets import QLabel


from PySide6.QtGui import QPixmap


from PySide6.QtCore import Qt


from app.core.thumbnail_cache import ThumbnailCache

from app.core.preview_loader import PreviewLoader





class ImagePreview(QLabel):


    def __init__(self):

        super().__init__()



        self.preview_cache = ThumbnailCache(

            size=400

        )


        self.loader = None



        self.pixmap_cache = {}



        self.setAlignment(

            Qt.AlignCenter

        )


        self.setMinimumHeight(

            300

        )


        self.show_empty()





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



        # ==========================
        # MEMORY CACHE
        # ==========================


        if key in self.pixmap_cache:


            self.setPixmap(

                self.pixmap_cache[key]

            )

            return





        # ==========================
        # ASYNC LOAD
        # ==========================


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





    def set_preview(
            self,
            key,
            pixmap
    ):


        if pixmap.isNull():

            self.show_empty()

            return



        self.pixmap_cache[key] = pixmap



        self.setPixmap(

            pixmap

        )





    def show_empty(self):


        self.clear()


        self.setText(

            "Image Preview"

        )