import sys


from PySide6.QtWidgets import QApplication


from app.views.main_window import MainWindow


from app.core.config import (
    APP_NAME,
    APP_VERSION
)



def main():

    app = QApplication(
        sys.argv
    )


    app.setApplicationName(
        APP_NAME
    )


    app.setApplicationVersion(
        APP_VERSION
    )



    window = MainWindow()


    window.show()



    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    main()