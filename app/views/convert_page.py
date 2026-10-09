from pathlib import Path


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QScrollArea
)


from app.widgets.drop_area import DropArea
from app.widgets.image_list import ImageList
from app.widgets.image_preview import ImagePreview
from app.widgets.settings_panel import SettingsPanel
from app.widgets.output_panel import OutputPanel
from app.widgets.process_status import ProcessStatus


from app.core.image_loader import (
    load_files,
    load_folder
)


from app.core.process_manager import ProcessManager



class ConvertPage(QWidget):


    def __init__(self):

        super().__init__()


        self.images = []

        self.selected_image = None


        self.settings_panel = SettingsPanel()

        self.output_panel = OutputPanel()

        self.process_status = ProcessStatus()

        self.process_manager = ProcessManager()


        self.init_ui()



    def init_ui(self):

        main_layout = QVBoxLayout()



        self.scroll_area = QScrollArea()

        self.scroll_area.setWidgetResizable(
            True
        )


        self.content_widget = QWidget()


        layout = QVBoxLayout(
            self.content_widget
        )



        self.drop_area = DropArea()


        self.drop_area.files_dropped.connect(
            self.handle_drop
        )



        add_single = QPushButton(
            "Add Image"
        )


        add_multiple = QPushButton(
            "Add Multiple Images"
        )


        add_folder = QPushButton(
            "Add Folder"
        )


        remove_button = QPushButton(
            "Remove Selected"
        )


        delete_all_button = QPushButton(
            "Delete All"
        )


        self.convert_selected_button = QPushButton(
            "Convert Selected"
        )


        self.convert_all_button = QPushButton(
            "Convert All"
        )



        self.image_list = ImageList()

        self.preview = ImagePreview()



        self.image_list.image_selected.connect(
            self.handle_image_selected
        )


        self.image_list.image_selected.connect(
            self.preview.show_image
        )



        add_single.clicked.connect(
            self.add_single_image
        )


        add_multiple.clicked.connect(
            self.add_multiple_images
        )


        add_folder.clicked.connect(
            self.add_folder
        )


        remove_button.clicked.connect(
            self.remove_selected
        )


        delete_all_button.clicked.connect(
            self.delete_all
        )


        self.convert_selected_button.clicked.connect(
            self.convert_selected
        )


        self.convert_all_button.clicked.connect(
            self.convert_all
        )



        self.process_status.open_folder_clicked.connect(
            self.open_output_folder
        )


        self.process_status.cancel_clicked.connect(
            self.cancel_processing
        )



        widgets = [

            self.drop_area,

            add_single,

            add_multiple,

            add_folder,

            self.image_list,

            remove_button,

            delete_all_button,

            self.preview,

            self.settings_panel,

            self.output_panel,

            self.process_status,

            self.convert_selected_button,

            self.convert_all_button

        ]



        for widget in widgets:

            layout.addWidget(
                widget
            )



        self.scroll_area.setWidget(
            self.content_widget
        )


        main_layout.addWidget(
            self.scroll_area
        )


        self.setLayout(
            main_layout
        )

    # =========================
    # IMAGE SELECTION
    # =========================


    def handle_image_selected(self, image):

        self.selected_image = image



    # =========================
    # IMAGE INPUT
    # =========================


    def add_single_image(self):

        file, _ = QFileDialog.getOpenFileName(

            self,

            "Select Image",

            "",

            "Images (*.jpg *.jpeg *.png)"

        )


        if file:

            self.add_images(
                [file]
            )



    def add_multiple_images(self):

        files, _ = QFileDialog.getOpenFileNames(

            self,

            "Select Images",

            "",

            "Images (*.jpg *.jpeg *.png)"

        )


        if files:

            self.add_images(
                files
            )



    def add_folder(self):

        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Folder"

        )


        if folder:

            self.images.extend(

                load_folder(folder)

            )


            self.refresh()



    def handle_drop(self, paths):

        for path in paths:

            self.add_path(path)



    def add_path(self, path):

        if Path(path).is_dir():

            self.images.extend(

                load_folder(path)

            )


        else:

            self.images.extend(

                load_files(
                    [path]
                )

            )


        self.refresh()



    def add_images(self, files):

        self.images.extend(

            load_files(files)

        )


        self.refresh()



    def refresh(self):

        self.image_list.clear()


        self.image_list.add_images(

            self.images

        )



    # =========================
    # IMAGE MANAGEMENT
    # =========================


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



    def delete_all(self):

        self.images.clear()


        self.selected_image = None


        self.image_list.clear()


        self.preview.show_empty()


        self.process_status.reset()



    # =========================
    # CONVERSION
    # =========================


    def convert_selected(self):

        if self.selected_image is None:


            QMessageBox.warning(

                self,

                "No Image",

                "Please select an image first."

            )


            return



        self.convert_process(

            [
                self.selected_image
            ]

        )



    def convert_all(self):

        if not self.images:


            QMessageBox.warning(

                self,

                "No Image",

                "No images available."

            )


            return



        self.convert_process(

            self.images

        )



    def convert_process(self, images):

        try:

            self.set_processing_state()


            self.process_status.reset()


            self.process_status.set_processing()



            settings = self.settings_panel.get_settings()



            output_folder = (
                self.output_panel.get_output_folder()
            )



            result = self.process_manager.process(

                images,

                settings,

                output_folder,

                on_file=self.update_processing_file,

                on_progress=self.update_processing_progress

            )



            self.set_finished_state()



            if result["cancelled"]:


                self.process_status.set_cancelled()



                QMessageBox.information(

                    self,

                    "Conversion Cancelled",

                    f"Process cancelled.\n\n"
                    f"Success: {result['success']}\n"
                    f"Failed: {result['failed']}"

                )


            else:


                self.process_status.set_completed()



                QMessageBox.information(

                    self,

                    "Conversion Complete",

                    f"Success: {result['success']}\n"
                    f"Failed: {result['failed']}"

                )



        except Exception as error:


            self.set_finished_state()


            self.process_status.set_idle()



            QMessageBox.critical(

                self,

                "Conversion Failed",

                str(error)

            )



    # =========================
    # PROCESS STATUS
    # =========================


    def update_processing_file(self, filename):

        self.process_status.update_file(

            filename

        )



    def update_processing_progress(
            self,
            progress,
            success,
            failed
    ):


        self.process_status.update_progress(

            progress

        )


        self.process_status.update_result(

            success,

            failed

        )



    def set_processing_state(self):

        self.convert_selected_button.setEnabled(

            False

        )


        self.convert_all_button.setEnabled(

            False

        )



    def set_finished_state(self):

        self.convert_selected_button.setEnabled(

            True

        )


        self.convert_all_button.setEnabled(

            True

        )



    def cancel_processing(self):

        self.process_manager.cancel()



    # =========================
    # OUTPUT FOLDER
    # =========================


    def open_output_folder(self):

        import os


        folder = self.output_panel.get_output_folder()



        if os.path.exists(folder):

            os.startfile(folder)