import os


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QMessageBox,
    QScrollArea,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt


from app.ui.widgets.drop_section import DropSection
from app.ui.widgets.action_section import ActionSection
from app.ui.widgets.image_section import ImageSection
from app.ui.widgets.conversion_section import ConversionSection
from app.ui.widgets.process_section import ProcessSection

from app.services.conversion_service import ConversionService



from app.styles.theme import THEME

class ConvertPage(QWidget):


    def __init__(self):

        super().__init__()


        self.conversion = ConversionService(
            self
        )


        self.init_components()

        self.init_ui()

        self.connect_signals()
    



    # ==================================================
    # COMPONENTS
    # ==================================================

    def init_components(self):

        self.drop_section = DropSection()

        self.action_section = ActionSection()

        self.image_section = ImageSection()

        self.conversion_section = ConversionSection()

        self.process_section = ProcessSection()
        



    # ==================================================
    # UI PREMIUM WORKSPACE
    # ==================================================

    def init_ui(self):


        self.setStyleSheet(
            THEME["convert_page"]
        )


        self.setObjectName(
            "convertPage"
        )


        root = QVBoxLayout(self)


        root.setContentsMargins(
            24,
            24,
            24,
            24
        )


        root.setSpacing(
            0
        )



        # ===============================
        # PAGE HEADER
        # ===============================


        header = QVBoxLayout()

        header.setSpacing(
            8
        )


        title = QLabel(
            "⚡ Conversion Workspace"
        )

        title.setObjectName(
            "pageTitle"
        )

        title.setAlignment(
            Qt.AlignCenter
        )



        subtitle = QLabel(
            "Transform your images into optimized WEBP files with a professional workflow."
        )

        subtitle.setObjectName(
            "pageSubtitle"
        )

        subtitle.setAlignment(
            Qt.AlignCenter
        )



        steps = QHBoxLayout()

        steps.setSpacing(
            10
        )


        for text in [

            "① Import Images",

            "② Configure Settings",

            "③ Convert & Optimize"

        ]:

            badge = QLabel(
                text
            )

            badge.setObjectName(
                "step"
            )

            badge.setAlignment(
                Qt.AlignCenter
            )

            steps.addWidget(
                badge
            )


        # membuat group badge tetap di tengah
        steps.setAlignment(
            Qt.AlignCenter
        )



        header.addWidget(
            title
        )

        header.addWidget(
            subtitle
        )

        header.addSpacing(
            6
        )

        header.addLayout(
            steps
        )


        # membuat seluruh header center
        header.setAlignment(
            Qt.AlignCenter
        )



        # ===============================
        # SCROLL AREA
        # ===============================


        self.scroll_area = QScrollArea()


        self.scroll_area.setWidgetResizable(
            True
        )


        self.scroll_area.setFrameShape(
            QFrame.NoFrame
        )


        # HIDE SCROLLBAR
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )


        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.scroll_area.setStyleSheet(
            """

            QScrollArea {

                background:transparent;

                border:none;

            }


            QScrollArea QWidget {

                background:transparent;

            }


            QScrollArea > QWidget > QWidget {

                background:transparent;

            }


            QScrollBar:vertical {

                background:transparent;

                width:6px;

                margin:0px;

            }


            QScrollBar::handle:vertical {

                background:#30384A;

                border-radius:3px;

            }


            QScrollBar::handle:vertical:hover {

                background:#4F8CFF;

            }


            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {

                height:0px;

            }

            """
        )



        self.content_widget = QWidget()

        self.content_widget.setStyleSheet(
            """
            QWidget {
                background:transparent;
            }
            """
        )


        content_layout = QVBoxLayout(
            self.content_widget
        )


        content_layout.setContentsMargins(
            0,
            10,
            0,
            20
        )


        content_layout.setSpacing(
            18
        )


        content_layout.addSpacing(
            24
        )


        content_layout.addLayout(
            header
        )


        content_layout.addSpacing(
            12
        )



        # ==================================
        # PREMIUM FULL PAGE WORKSPACE
        # ==================================

        sections = [

            (
                "",
                self.drop_section
            ),

            (
                "",
                self.image_section
            ),

            (
                "",
                self.conversion_section
            ),

            (
                "",
                self.action_section
            ),

            (
                "",
                self.process_section
            ),

        ]


        for title_text, widget in sections:

            section_layout = QVBoxLayout()

            section_layout.setSpacing(
                10
            )


            label = QLabel(
                title_text
            )


            label.setObjectName(
                "sectionTitle"
            )


            label.setStyleSheet(
                """

                QLabel {

                    color:#7EA6FF;

                    font-size:13px;

                    font-weight:800;

                    letter-spacing:1px;

                }

                """
            )


            section_layout.addWidget(
                label
            )


            section_layout.addWidget(
                widget
            )


            content_layout.addLayout(
                section_layout
            )



        self.scroll_area.setWidget(
            self.content_widget
        )


        root.addWidget(
            self.scroll_area
        )


    # ==================================================
    # SIGNAL CONNECTION
    # ==================================================

    def connect_signals(self):


        self.drop_section.drop_area.files_dropped.connect(
            self.image_section.add_paths
        )


        self.drop_section.add_image_button.clicked.connect(
            self.add_single_image
        )


        self.drop_section.add_multiple_button.clicked.connect(
            self.add_multiple_images
        )


        self.drop_section.add_folder_button.clicked.connect(
            self.add_folder
        )


        self.action_section.convert_selected_clicked.connect(
            self.convert_selected
        )


        self.action_section.convert_all_clicked.connect(
            self.convert_all
        )


        self.process_section.open_folder_clicked.connect(
            self.open_output_folder
        )
        


        self.action_section.cancel_clicked.connect(
            self.cancel_processing
        )


        self.conversion.progress_changed.connect(
            self.update_progress
        )


        self.conversion.file_processed.connect(
            self.process_section.update_file
        )


        self.conversion.worker_changed.connect(
            self.process_section.performance.update_worker
        )


        self.conversion.finished.connect(
            self.conversion_finished
        )


        self.conversion.failed.connect(
            self.conversion_failed
        )


        self.conversion.state_changed.connect(
            self.action_section.set_processing
        )


    # ==================================================
    # IMAGE INPUT
    # ==================================================

    def add_single_image(self):


        file, _ = QFileDialog.getOpenFileName(

            self,

            "Select Image",

            "",

            "Images (*.jpg *.jpeg *.png *.webp)"

        )


        if file:

            self.image_section.add_images(
                [file]
            )



    def add_multiple_images(self):


        files, _ = QFileDialog.getOpenFileNames(

            self,

            "Select Images",

            "",

            "Images (*.jpg *.jpeg *.png *.webp)"

        )


        if files:

            self.image_section.add_images(
                files
            )



    def add_folder(self):


        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Folder"

        )


        if folder:

            self.image_section.add_folder(
                folder
            )



    def delete_all(self):


        self.image_section.clear()


        self.process_section.reset()


        self.conversion_section.reset()



    # ==================================================
    # CONVERSION REQUEST
    # ==================================================

    def convert_selected(self):


        image = self.image_section.get_selected()



        if image is None:


            QMessageBox.warning(

                self,

                "No Image",

                "Please select an image first."

            )


            return



        self.start_conversion(

            [image]

        )



    def convert_all(self):


        images = self.image_section.get_images()



        if not images:


            QMessageBox.warning(

                self,

                "No Image",

                "No images available."

            )


            return



        self.start_conversion(

            images

        )



    # ==================================================
    # START CONVERSION
    # ==================================================

    def start_conversion(

            self,

            images

    ):



        if self.conversion.is_running():

            QMessageBox.warning(

                self,

                "Processing",

                "Conversion is already running."

            )

            return


        self.process_section.reset()


        self.process_section.set_processing()


        settings = (

            self.conversion_section.get_settings()

        )


        output_folder = (

            self.conversion_section.get_output_folder()

        )



        print(

            "Conversion Settings:",

            settings

        )


        print(

            "Output:",

            output_folder

        )



        self.process_section.set_profile(

            settings["profile"]

        )


        self.process_section.set_workers(

            self.conversion.get_worker_count()

        )


        self.conversion.start(

            images,

            settings,

            output_folder

        )




    # ==================================================
    # THREAD UPDATE
    # ==================================================

    def update_progress(

            self,

            progress,

            success,

            failed

    ):


        self.process_section.update_progress(

            progress

        )


        self.process_section.update_result(

            success,

            failed

        )



    # ==================================================
    # FINISHED
    # ==================================================

    def conversion_finished(

            self,

            result

    ):

        self.process_section.update_statistics(
            result
        )



        if result.get(

            "cancelled",

            False

        ):



            self.process_section.set_cancelled()



            QMessageBox.information(

                self,

                "Cancelled",

                "Conversion cancelled."

            )



        else:



            self.process_section.set_completed()



            QMessageBox.information(

                self,

                "Conversion Complete",

                f"Success: {result['success']}\n"

                f"Failed: {result['failed']}\n"

                f"Time: {result['duration']:.2f}s"

            )




    def conversion_failed(

            self,

            error

    ):


        self.process_section.set_idle()



        QMessageBox.critical(

            self,

            "Conversion Failed",

            error

        )


    # ==================================================
    # CANCEL
    # ==================================================

    def cancel_processing(self):


        if self.conversion.is_running():


            self.conversion.cancel()


            self.process_section.set_cancelled()



    # ==================================================
    # OUTPUT
    # ==================================================

    def open_output_folder(self):


        folder = (

            self.conversion_section.get_output_folder()

        )



        if os.path.exists(folder):


            os.startfile(folder)
            
    def closeEvent(self, event):

        event.accept()