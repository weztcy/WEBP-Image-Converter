from PySide6.QtCore import (
    QThread,
    Signal
)


from app.core.thumbnail_cache import ThumbnailCache





class ThumbnailLoader(QThread):


    thumbnail_ready = Signal(
        object,
        object
    )



    def __init__(
            self,
            image,
            cache
    ):


        super().__init__()


        self.image = image


        self.cache = cache





    def run(self):


        try:


            pixmap = self.cache.get_pixmap(

                self.image.path

            )



            self.thumbnail_ready.emit(

                self.image,

                pixmap

            )



        except Exception as error:


            print(

                f"Thumbnail loader error: {error}"

            )