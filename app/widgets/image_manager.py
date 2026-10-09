from pathlib import Path


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


from PySide6.QtCore import Signal



from app.widgets.image_list import ImageList

from app.widgets.image_preview import ImagePreview



from app.core.image_loader import (
    load_files
)


from app.core.image_scanner import (
    ImageScanner
)





class ImageManager(QWidget):


    image_selected = Signal(object)



    def __init__(self):

        super().__init__()


        self.images = []


        self.selected_image = None


        self.scanner = None



        self.init_ui()





    # ==========================
    # UI
    # ==========================


    def init_ui(self):


        layout = QVBoxLayout()



        self.image_list = ImageList()


        self.preview = ImagePreview()



        self.image_list.image_selected.connect(

            self.handle_selected

        )



        self.image_list.image_selected.connect(

            self.preview.show_image

        )



        layout.addWidget(

            self.image_list

        )


        layout.addWidget(

            self.preview

        )


        self.setLayout(

            layout

        )





    # ==========================
    # SELECTION
    # ==========================


    def handle_selected(
            self,
            image
    ):


        self.selected_image = image


        self.image_selected.emit(

            image

        )





    def get_selected(self):


        return self.selected_image





    # ==========================
    # ADD FILES
    # ==========================


    def add_images(
            self,
            files
    ):


        images = load_files(
            files
        )


        self.images.extend(

            images

        )


        self.image_list.add_images(

            images

        )





    # ==========================
    # FOLDER SCAN
    # ==========================


    def add_folder(
            self,
            folder
    ):


        # stop scanner lama

        if self.scanner:


            self.scanner.cancel()



        self.scanner = ImageScanner(

            folder

        )



        self.scanner.image_found.connect(

            self.add_scanned_image

        )



        self.scanner.start()





    def add_scanned_image(
            self,
            image
    ):


        self.images.append(

            image

        )


        self.image_list.add_images(

            [
                image
            ]

        )





    def add_path(
            self,
            path
    ):


        if Path(path).is_dir():


            self.add_folder(

                path

            )


        else:


            self.add_images(

                [
                    path
                ]

            )





    def add_paths(
            self,
            paths
    ):


        for path in paths:


            self.add_path(

                path

            )





    # ==========================
    # MANAGEMENT
    # ==========================


    def remove_selected(self):


        if self.selected_image is None:

            return



        if self.selected_image in self.images:


            self.images.remove(

                self.selected_image

            )



        self.selected_image = None


        self.preview.show_empty()


        self.refresh()





    def clear(self):


        if self.scanner:


            self.scanner.cancel()



        self.images.clear()


        self.selected_image = None


        self.image_list.clear()


        self.preview.show_empty()





    def get_images(self):


        return self.images





    # ==========================
    # REFRESH
    # ==========================


    def refresh(self):


        self.image_list.clear()


        self.image_list.add_images(

            self.images

        )