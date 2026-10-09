from pathlib import Path

from PySide6.QtCore import (
    QThread,
    Signal
)


from app.models.image_model import ImageModel



SUPPORTED_FORMAT = {
    ".jpg",
    ".jpeg",
    ".png"
}





class ImageScanner(QThread):


    image_found = Signal(object)


    scan_finished = Signal()



    def __init__(
            self,
            folder
    ):

        super().__init__()

        self.folder = Path(folder)

        self.cancelled = False




    def run(self):


        try:


            for file in self.folder.rglob("*"):


                if self.cancelled:

                    break



                if (

                    file.is_file()

                    and

                    file.suffix.lower()
                    in SUPPORTED_FORMAT

                ):


                    image = ImageModel(
                        file
                    )


                    self.image_found.emit(

                        image

                    )



        finally:


            self.scan_finished.emit()





    def cancel(self):


        self.cancelled = True