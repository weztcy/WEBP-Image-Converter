from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem
)


from PySide6.QtGui import (
    QIcon
)


from PySide6.QtCore import (
    QSize,
    Signal
)


from functools import partial


from app.core.thumbnail_cache import (
    ThumbnailCache
)


from app.core.thumbnail_loader import (
    ThumbnailLoader
)





class ImageList(QListWidget):


    image_selected = Signal(object)



    def __init__(self):

        super().__init__()


        self.current_selected_item = None


        self.thumbnail_cache = ThumbnailCache(

            size=70

        )


        self.loading_threads = {}


        self.loaded_paths = set()



        self.setIconSize(

            QSize(
                70,
                70
            )

        )


        self.itemClicked.connect(

            self.handle_click

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


            # prevent duplicate

            if path in self.loaded_paths:

                continue



            self.loaded_paths.add(
                path
            )



            item = QListWidgetItem()



            item.setText(

                f"{image.filename} | "
                f"{image.extension.replace('.', '').upper()} | "
                f"{self.format_size(image.get_size())}"

            )



            item.setData(

                100,

                image

            )


            self.addItem(

                item

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



        item.setIcon(

            QIcon(

                pixmap

            )

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


        if self.current_selected_item == item:


            self.clearSelection()


            self.current_selected_item = None


            self.image_selected.emit(

                None

            )


            return



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
    # FORMAT SIZE
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