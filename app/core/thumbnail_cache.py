from pathlib import Path
from PIL import Image
from PySide6.QtGui import QPixmap

import hashlib



class ThumbnailCache:


    def __init__(
            self,
            cache_folder=None,
            size=100
    ):

        self.size = size


        if cache_folder is None:

            cache_folder = (
                Path.home()
                /
                ".webp_converter_cache"
                /
                "thumbnails"
            )


        self.cache_folder = Path(
            cache_folder
        )


        self.cache_folder.mkdir(
            parents=True,
            exist_ok=True
        )



    def get_cache_path(
            self,
            image_path
    ):


        """
        Membuat nama cache unik
        berdasarkan path gambar
        """


        key = hashlib.md5(
            str(image_path)
            .encode()
        ).hexdigest()


        return (
            self.cache_folder
            /
            f"{key}.jpg"
        )



    def create_thumbnail(
            self,
            image_path
    ):


        image_path = Path(
            image_path
        )


        cache_path = self.get_cache_path(
            image_path
        )


        # Jika sudah ada cache
        if cache_path.exists():

            return cache_path



        try:


            with Image.open(
                    image_path
            ) as image:


                image.thumbnail(
                    (
                        self.size,
                        self.size
                    )
                )


                # Thumbnail cukup RGB
                if image.mode != "RGB":

                    image = image.convert(
                        "RGB"
                    )


                image.save(
                    cache_path,
                    "JPEG",
                    quality=85,
                    optimize=True
                )


            return cache_path



        except Exception as error:


            print(
                f"Thumbnail failed {image_path}: {error}"
            )


            return None



    def get_pixmap(
            self,
            image_path
    ):


        thumbnail = self.create_thumbnail(
            image_path
        )


        if thumbnail is None:

            return QPixmap()



        return QPixmap(
            str(thumbnail)
        )
    
    def create_preview(
            self,
            image_path,
            size=800
    ):

        image_path = Path(image_path)


        cache_path = (
            self.cache_folder
            /
            f"preview_{self.get_cache_path(image_path).name}"
        )


        if cache_path.exists():

            return cache_path



        try:


            with Image.open(image_path) as image:


                image.thumbnail(
                    (
                        size,
                        size
                    )
                )


                if image.mode not in (
                    "RGB",
                    "RGBA"
                ):

                    image = image.convert(
                        "RGBA"
                    )


                image.save(
                    cache_path,
                    "PNG",
                    optimize=True
                )


            return cache_path



        except Exception as error:


            print(
                f"Preview failed: {error}"
            )


            return None