from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget
)


from app.views.home_page import HomePage
from app.views.convert_page import ConvertPage



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()



        self.setWindowTitle(
            "Image2WEBP Converter"
        )


        self.setMinimumSize(
            900,
            600
        )



        self.pages = QStackedWidget()



        self.home_page = HomePage(
            self.show_convert_page
        )


        self.convert_page = ConvertPage()



        self.pages.addWidget(
            self.home_page
        )


        self.pages.addWidget(
            self.convert_page
        )



        self.setCentralWidget(
            self.pages
        )



    def show_convert_page(self):

        self.pages.setCurrentWidget(
            self.convert_page
        )