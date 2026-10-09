from pathlib import Path



class ImageModel:


    def __init__(self, path):


        self.path = Path(path)


        self.filename = self.path.name


        self.extension = (
            self.path.suffix
            .lower()
        )


        # Cache metadata file
        self._size = self._get_file_size()


    def _get_file_size(self):

        try:

            return self.path.stat().st_size


        except Exception:

            return 0



    def get_size(self):

        return self._size