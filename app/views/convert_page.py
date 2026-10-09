import os
import time


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
    QScrollArea
)



from app.widgets.drop_area import DropArea

from app.widgets.convert_toolbar import ConvertToolbar

from app.widgets.image_manager import ImageManager

from app.widgets.conversion_panel import ConversionPanel

from app.widgets.process_panel import ProcessPanel



from app.core.conversion_thread import ConversionThread





class ConvertPage(QWidget):


    def __init__(self):

        super().__init__()


        self.worker = None


        self.start_time = None


        self.init_components()

        self.init_ui()

        self.connect_signals()





    # ==================================================
    # COMPONENTS
    # ==================================================


    def init_components(self):


        self.drop_area = DropArea()


        self.toolbar = ConvertToolbar()


        self.image_manager = ImageManager()


        self.conversion_panel = ConversionPanel()


        self.process_panel = ProcessPanel()





    # ==================================================
    # UI
    # ==================================================


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



        widgets = [

            self.drop_area,

            self.toolbar,

            self.image_manager,

            self.conversion_panel,

            self.process_panel

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





    # ==================================================
    # SIGNAL CONNECTION
    # ==================================================


    def connect_signals(self):


        self.drop_area.files_dropped.connect(
            self.image_manager.add_paths
        )



        self.toolbar.add_image_clicked.connect(
            self.add_single_image
        )


        self.toolbar.add_multiple_clicked.connect(
            self.add_multiple_images
        )


        self.toolbar.add_folder_clicked.connect(
            self.add_folder
        )


        self.toolbar.remove_selected_clicked.connect(
            self.image_manager.remove_selected
        )


        self.toolbar.delete_all_clicked.connect(
            self.delete_all
        )


        self.toolbar.convert_selected_clicked.connect(
            self.convert_selected
        )


        self.toolbar.convert_all_clicked.connect(
            self.convert_all
        )



        self.process_panel.open_folder_clicked.connect(
            self.open_output_folder
        )


        self.process_panel.cancel_clicked.connect(
            self.cancel_processing
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

            self.image_manager.add_images(
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

            self.image_manager.add_images(
                files
            )





    def add_folder(self):


        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Folder"

        )


        if folder:

            self.image_manager.add_folder(
                folder
            )





    def delete_all(self):


        self.image_manager.clear()


        self.process_panel.reset()


        self.conversion_panel.reset()





    # ==================================================
    # CONVERSION REQUEST
    # ==================================================


    def convert_selected(self):


        image = self.image_manager.get_selected()



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


        images = self.image_manager.get_images()



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


        if self.worker:


            QMessageBox.warning(

                self,

                "Processing",

                "Conversion is already running."

            )


            return





        self.toolbar.set_processing(
            True
        )


        self.process_panel.reset()


        self.process_panel.set_processing()



        # TIMER START

        self.start_time = time.perf_counter()



        settings = (

            self.conversion_panel.get_settings()

        )


        output_folder = (

            self.conversion_panel.get_output_folder()

        )



        print(
            "Conversion Settings:",
            settings
        )


        print(
            "Output:",
            output_folder
        )



        # PERFORMANCE INFO


        self.conversion_panel.set_profile(

            settings["profile"]

        )


        self.conversion_panel.set_workers(

            self.get_worker_count()

        )



        self.worker = ConversionThread(

            images,

            settings,

            output_folder

        )



        self.worker.file_processed.connect(

            self.process_panel.update_file

        )


        self.worker.progress_changed.connect(

            self.update_progress

        )


        self.worker.conversion_finished.connect(

            self.conversion_finished

        )


        self.worker.conversion_failed.connect(

            self.conversion_failed

        )


        self.worker.finished.connect(

            self.cleanup_worker

        )



        self.worker.start()





    # ==================================================
    # PERFORMANCE
    # ==================================================


    def get_worker_count(self):


        try:


            from app.core.performance_config import (

                PerformanceConfig

            )


            config = PerformanceConfig()


            return config.calculate_workers()



        except Exception:


            return 0





    # ==================================================
    # THREAD UPDATE
    # ==================================================


    def update_progress(
            self,
            progress,
            success,
            failed
    ):


        self.process_panel.update_progress(

            progress

        )


        self.process_panel.update_result(

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


        self.toolbar.set_processing(

            False

        )


        duration = 0



        if self.start_time:


            duration = (

                time.perf_counter()

                -

                self.start_time

            )



        total = (

            result["success"]

            +

            result["failed"]

        )



        speed = 0



        if duration > 0:


            speed = total / duration



        self.conversion_panel.update_statistics({

            "total": total,

            "success": result["success"],

            "failed": result["failed"],

            "duration": duration,

            "speed": speed,

            "input_mb": result["input_bytes"] / (1024 * 1024),

            "output_mb": result["output_bytes"] / (1024 * 1024),

            "saved_percent": result["saved_percent"]

        })





        if result.get(
            "cancelled",
            False
        ):


            self.process_panel.set_cancelled()



            QMessageBox.information(

                self,

                "Cancelled",

                "Conversion cancelled."

            )



        else:


            self.process_panel.set_completed()



            QMessageBox.information(

                self,

                "Conversion Complete",

                f"Success: {result['success']}\n"
                f"Failed: {result['failed']}\n"
                f"Time: {duration:.2f}s"

            )





    def conversion_failed(
            self,
            error
    ):


        self.toolbar.set_processing(

            False

        )


        self.process_panel.set_idle()



        QMessageBox.critical(

            self,

            "Conversion Failed",

            error

        )





    # ==================================================
    # CLEANUP
    # ==================================================


    def cleanup_worker(self):


        worker = self.worker


        self.worker = None



        if worker:


            worker.deleteLater()





    # ==================================================
    # CANCEL
    # ==================================================


    def cancel_processing(self):


        if self.worker:


            self.worker.cancel()



            self.process_panel.set_cancelled()





    # ==================================================
    # OUTPUT
    # ==================================================


    def open_output_folder(self):


        folder = (

            self.conversion_panel.get_output_folder()

        )



        if os.path.exists(folder):


            os.startfile(folder)