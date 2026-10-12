from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QPushButton,
    QFrame
)

from PySide6.QtCore import Signal



from app.styles.theme import THEME

class ProcessStatus(QWidget):


    open_folder_clicked = Signal()



    def __init__(self):

        super().__init__()

        self.init_ui()



    # ==========================
    # UI
    # ==========================

    def init_ui(self):


        self.setStyleSheet(
            THEME["process_status"]
        )



        root = QVBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )

        root.setSpacing(
            0
        )



        card = QFrame()

        card.setObjectName(
            "card"
        )


        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        layout.setSpacing(
            14
        )



        # HEADER

        header = QHBoxLayout()


        self.title_label = QLabel(
            "⚙ Processing Status"
        )

        self.title_label.setObjectName(
            "title"
        )


        self.status_label = QLabel(
            "Idle"
        )

        self.status_label.setObjectName(
            "status"
        )


        header.addWidget(
            self.title_label
        )


        header.addStretch()


        header.addWidget(
            self.status_label
        )


        layout.addLayout(
            header
        )



        # FILE

        file_title = QLabel(
            "Current File"
        )

        file_title.setObjectName(
            "label"
        )


        self.current_file_label = QLabel(
            "-"
        )

        self.current_file_label.setObjectName(
            "value"
        )


        layout.addWidget(
            file_title
        )

        layout.addWidget(
            self.current_file_label
        )



        # PROGRESS

        self.progress_bar = QProgressBar()


        self.progress_bar.setRange(
            0,
            100
        )


        self.progress_bar.setValue(
            0
        )


        layout.addWidget(
            self.progress_bar
        )



        # RESULT

        result_layout = QHBoxLayout()


        success_box = QFrame()

        success_box.setObjectName(
            "successBox"
        )


        success_layout = QVBoxLayout(
            success_box
        )


        self.success_label = QLabel(
            "✓ Success: 0"
        )

        self.success_label.setObjectName(
            "value"
        )


        success_layout.addWidget(
            self.success_label
        )



        failed_box = QFrame()

        failed_box.setObjectName(
            "failedBox"
        )


        failed_layout = QVBoxLayout(
            failed_box
        )


        self.failed_label = QLabel(
            "✕ Failed: 0"
        )

        self.failed_label.setObjectName(
            "value"
        )


        failed_layout.addWidget(
            self.failed_label
        )



        result_layout.addWidget(
            success_box
        )


        result_layout.addWidget(
            failed_box
        )


        layout.addLayout(
            result_layout
        )



        # BUTTON

        self.open_folder_button = QPushButton(
            "📂 Open Output Folder"
        )


        self.open_folder_button.setEnabled(
            False
        )


        self.open_folder_button.clicked.connect(
            self.open_folder_clicked.emit
        )


        layout.addWidget(
            self.open_folder_button
        )



        root.addWidget(
            card
        )



    # ==========================
    # STATUS
    # ==========================

    def set_processing(self):

        self.status_label.setText(
            "Processing"
        )

        self.status_label.setStyleSheet(
            "color:#4F8CFF;"
        )


        self.open_folder_button.setEnabled(
            False
        )



    def set_completed(self):

        self.status_label.setText(
            "Completed"
        )


        self.status_label.setStyleSheet(
            "color:#34D399;"
        )


        self.open_folder_button.setEnabled(
            True
        )



    def set_cancelled(self):

        self.status_label.setText(
            "Cancelled"
        )


        self.status_label.setStyleSheet(
            "color:#F59E0B;"
        )


        self.open_folder_button.setEnabled(
            True
        )



    def set_idle(self):

        self.status_label.setText(
            "Idle"
        )


        self.status_label.setStyleSheet(
            "color:#98A2B3;"
        )


        self.open_folder_button.setEnabled(
            False
        )



    # ==========================
    # UPDATE
    # ==========================

    def update_file(
            self,
            filename
    ):

        self.current_file_label.setText(
            filename if filename else "-"
        )



    def update_progress(
            self,
            value
    ):

        value = max(
            0,
            min(value,100)
        )


        self.progress_bar.setValue(
            value
        )



    def update_result(
            self,
            success,
            failed
    ):

        self.success_label.setText(
            f"✓ Success: {success}"
        )


        self.failed_label.setText(
            f"✕ Failed: {failed}"
        )



    def update_status(
            self,
            progress,
            success,
            failed
    ):

        self.update_progress(
            progress
        )


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
            "-"
        )


        self.progress_bar.setValue(
            0
        )


        self.update_result(
            0,
            0
        )