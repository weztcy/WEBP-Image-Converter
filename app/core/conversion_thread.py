from PySide6.QtCore import (
    QThread,
    Signal
)


from app.core.process_pool import (
    ProcessPoolManager
)





class ConversionThread(QThread):


    # ==========================
    # SIGNALS
    # ==========================


    progress_changed = Signal(
        int,
        int,
        int
    )


    file_processed = Signal(
        str
    )


    conversion_finished = Signal(
        dict
    )


    conversion_failed = Signal(
        str
    )





    def __init__(
            self,
            images,
            settings,
            output_folder
    ):


        super().__init__()



        self.images = images

        self.settings = settings

        self.output_folder = output_folder



        self.process_manager = None


        self.cancelled = False





    # ==========================
    # THREAD EXECUTION
    # ==========================


    def run(self):


        try:


            # create inside worker thread

            self.process_manager = ProcessPoolManager()



            result = self.process_manager.process(

                self.images,

                self.settings,

                self.output_folder,

                on_file=self.handle_file,

                on_progress=self.handle_progress

            )



            result["cancelled"] = (

                self.cancelled

            )



            self.conversion_finished.emit(

                result

            )



        except Exception as error:


            self.conversion_failed.emit(

                str(error)

            )



        finally:


            self.process_manager = None





    # ==========================
    # CALLBACK
    # ==========================


    def handle_file(
            self,
            filename
    ):


        if self.cancelled:

            return



        self.file_processed.emit(

            filename

        )





    def handle_progress(
            self,
            progress,
            success,
            failed
    ):


        if self.cancelled:

            return



        self.progress_changed.emit(

            progress,

            success,

            failed

        )





    # ==========================
    # CANCEL
    # ==========================


    def cancel(self):


        self.cancelled = True



        if self.process_manager:


            self.process_manager.cancel()





    def is_cancelled(self):


        return self.cancelled