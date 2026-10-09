from pathlib import Path



class ImageModel:


    def __init__(self, path):

        self.path = Path(path)


        self.filename = self.path.name


        self.extension = (

            self.path.suffix

            .lower()

        )



    def get_size(self):

        return self.path.stat().st_size