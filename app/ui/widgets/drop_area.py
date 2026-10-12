from PySide6.QtWidgets import QLabel


from PySide6.QtCore import (
    Qt,
    Signal
)



class DropArea(QLabel):


    files_dropped = Signal(list)



    def __init__(self):

        super().__init__()


        self.setText(
            "Drag & Drop Image or Folder Here"
        )


        self.setAlignment(
            Qt.AlignCenter
        )


        self.setAcceptDrops(
            True
        )



    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():

            event.acceptProposedAction()



    def dropEvent(self, event):

        urls = event.mimeData().urls()



        paths = [

            url.toLocalFile()

            for url in urls

        ]



        self.files_dropped.emit(
            paths
        )


        event.acceptProposedAction()