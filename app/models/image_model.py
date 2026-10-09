from pathlib import Path



class ImageModel:


    def __init__(
            self,
            path
    ):


        self.path = Path(path)


        # ==========================
        # BASIC INFO
        # ==========================

        self.filename = (
            self.path.name
        )


        self.extension = (
            self.path.suffix
            .lower()
        )



        # ==========================
        # FILE CACHE
        # ==========================

        self._size = None

        self._modified = None



        self.load_file_metadata()



        # ==========================
        # IMAGE METADATA
        # LAZY
        # ==========================

        self._width = None

        self._height = None

        self._mode = None





    # ==================================
    # FILE METADATA
    # ==================================


    def load_file_metadata(self):


        try:


            stat = self.path.stat()


            self._size = stat.st_size


            self._modified = stat.st_mtime



        except Exception:


            self._size = 0

            self._modified = 0





    # ==================================
    # SIZE
    # ==================================


    def get_size(self):


        return self._size





    def get_modified_time(self):


        return self._modified





    # ==================================
    # IMAGE INFO
    # ==================================


    def load_image_metadata(self):


        if self._width is not None:

            return



        try:

            from PIL import Image



            with Image.open(
                self.path
            ) as image:


                self._width = image.width


                self._height = image.height


                self._mode = image.mode



        except Exception:


            self._width = 0

            self._height = 0

            self._mode = None





    def get_resolution(self):


        self.load_image_metadata()


        return (

            self._width,

            self._height

        )





    def get_mode(self):


        self.load_image_metadata()


        return self._mode





    def __repr__(self):


        return (

            f"ImageModel("
            f"{self.filename}"
            f")"

        )