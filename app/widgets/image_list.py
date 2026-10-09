from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem
)


from PySide6.QtGui import (
    QIcon,
    QPixmap
)


from PySide6.QtCore import (
    QSize,
    Signal
)



class ImageList(QListWidget):


    image_selected = Signal(object)



    def __init__(self):

        super().__init__()


        self.current_selected_item = None



        self.setIconSize(
            QSize(70, 70)
        )


        self.itemClicked.connect(
            self.handle_click
        )



    def add_images(self, images):

        for image in images:


            item = QListWidgetItem()



            pixmap = QPixmap(
                str(image.path)
            )


            if not pixmap.isNull():

                pixmap = pixmap.scaled(
                    70,
                    70
                )


                item.setIcon(
                    QIcon(pixmap)
                )



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



    def handle_click(self, item):


        if self.current_selected_item == item:


            self.clearSelection()


            self.current_selected_item = None


            self.image_selected.emit(
                None
            )


            return



        self.current_selected_item = item


        image = item.data(100)


        self.image_selected.emit(
            image
        )



    def remove_selected(self):

        selected = self.currentItem()


        if selected:


            row = self.row(selected)


            self.takeItem(
                row
            )


            self.current_selected_item = None



    def clear(self):

        super().clear()


        self.current_selected_item = None



    def format_size(self, size):

        kb = size / 1024


        mb = kb / 1024



        if mb >= 1:

            return f"{mb:.2f} MB"



        return f"{kb:.2f} KB"