import os
import time


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFileDialog,
    QMessageBox,
    QScrollArea
)



from app.components.drop_section import DropSection

from app.components.action_section import ActionSection

from app.components.image_section import ImageSection

from app.components.conversion_section import ConversionSection

from app.components.process_section import ProcessSection



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


        self.drop_section = DropSection()


        self.action_section = ActionSection()


        self.image_section = ImageSection()


        self.conversion_section = ConversionSection()


        self.process_section = ProcessSection()





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
            self.drop_section,
            self.image_section,
            self.conversion_section,
            self.action_section,
            self.process_section
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


        if self.worker:


            QMessageBox.warning(

                self,

                "Processing",

                "Conversion is already running."

            )


            return





        self.action_section.set_processing(True)


        self.process_section.reset()


        self.process_section.set_processing()



        # TIMER START

        self.start_time = time.perf_counter()



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



        # PERFORMANCE INFO


        self.process_section.set_profile(

            settings["profile"]

        )


        self.process_section.set_workers(

            self.get_worker_count()

        )



        self.worker = ConversionThread(

            images,

            settings,

            output_folder

        )



        self.worker.file_processed.connect(

            self.process_section.update_file

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


        self.action_section.set_processing(False)

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



        self.process_section.update_statistics({

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
                f"Time: {duration:.2f}s"

            )





    def conversion_failed(
            self,
            error
    ):


        self.action_section.set_processing(

            False

        )


        self.process_section.set_idle()



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