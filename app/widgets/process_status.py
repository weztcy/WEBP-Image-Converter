from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton
)

from PySide6.QtCore import Signal


class ProcessStatus(QWidget):

    open_folder_clicked = Signal()


    def __init__(self):
        super().__init__()

        self.init_ui()


    # ==========================
    # UI
    # ==========================

    def init_ui(self):

        layout = QVBoxLayout(self)


        self.title_label = QLabel(
            "Processing Status: Idle"
        )


        self.current_file_label = QLabel(
            "Current File: -"
        )


        self.progress_bar = QProgressBar()

        self.progress_bar.setRange(
            0,
            100
        )

        self.progress_bar.setValue(
            0
        )


        self.success_label = QLabel(
            "Success: 0"
        )


        self.failed_label = QLabel(
            "Failed: 0"
        )


        self.open_folder_button = QPushButton(
            "Open Folder"
        )

        self.open_folder_button.setEnabled(
            False
        )


        self.open_folder_button.clicked.connect(
            self.open_folder_clicked.emit
        )


        widgets = [
            self.title_label,
            self.current_file_label,
            self.progress_bar,
            self.success_label,
            self.failed_label,
            self.open_folder_button
        ]


        for widget in widgets:
            layout.addWidget(widget)



    # ==========================
    # STATUS
    # ==========================

    def set_processing(self):

        self.title_label.setText(
            "Processing Status: Processing"
        )


        self.open_folder_button.setEnabled(
            False
        )



    def set_completed(self):

        self.title_label.setText(
            "Processing Status: Completed"
        )


        self.open_folder_button.setEnabled(
            True
        )



    def set_cancelled(self):

        self.title_label.setText(
            "Processing Status: Cancelled"
        )


        self.open_folder_button.setEnabled(
            True
        )



    def set_idle(self):

        self.title_label.setText(
            "Processing Status: Idle"
        )


        self.open_folder_button.setEnabled(
            False
        )



    # ==========================
    # UPDATE
    # ==========================

    def update_file(self, filename):

        if filename:

            self.current_file_label.setText(
                f"Current File: {filename}"
            )

        else:

            self.current_file_label.setText(
                "Current File: -"
            )



    def update_progress(self, value):

        value = max(
            0,
            min(value, 100)
        )

        self.progress_bar.setValue(
            value
        )



    def update_result(self, success, failed):

        self.success_label.setText(
            f"Success: {success}"
        )

        self.failed_label.setText(
            f"Failed: {failed}"
        )



    def update_status(
        self,
        progress,
        success,
        failed
    ):

        self.update_progress(progress)

        self.update_result(
            success,
            failed
        )



    # ==========================
    # RESET
    # ==========================

    def reset(self):

        self.set_idle()


        self.current_file_label.setText(
            "Current File: -"
        )


        self.progress_bar.setValue(
            0
        )


        self.update_result(
            0,
            0
        )