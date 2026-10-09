from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


from PySide6.QtCore import Signal


from app.widgets.process_status import (
    ProcessStatus
)





class ProcessPanel(QWidget):


    # ==========================
    # SIGNAL
    # ==========================


    cancel_clicked = Signal()


    open_folder_clicked = Signal()





    def __init__(self):

        super().__init__()


        self.init_components()

        self.init_ui()

        self.connect_signals()





    # ==========================
    # COMPONENT
    # ==========================


    def init_components(self):


        self.process_status = ProcessStatus()





    # ==========================
    # UI
    # ==========================


    def init_ui(self):


        layout = QVBoxLayout()



        layout.addWidget(

            self.process_status

        )



        self.setLayout(

            layout

        )





    # ==========================
    # SIGNAL
    # ==========================


    def connect_signals(self):


        self.process_status.cancel_clicked.connect(

            self.cancel_clicked.emit

        )


        self.process_status.open_folder_clicked.connect(

            self.open_folder_clicked.emit

        )





    # ==========================
    # PUBLIC API
    # ==========================


    def reset(self):


        self.process_status.reset()





    def set_processing(self):


        self.process_status.set_processing()





    def set_completed(self):


        self.process_status.set_completed()





    def set_cancelled(self):


        self.process_status.set_cancelled()





    def set_idle(self):


        self.process_status.set_idle()





    def update_file(
            self,
            filename
    ):


        self.process_status.update_file(

            filename

        )





    def update_progress(
            self,
            progress
    ):


        self.process_status.update_progress(

            progress

        )





    def update_result(
            self,
            success,
            failed
    ):


        self.process_status.update_result(

            success,

            failed

        )