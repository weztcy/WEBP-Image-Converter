from pathlib import Path

import hashlib

from PIL import Image

from PySide6.QtGui import QPixmap





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

            )



        self.cache_folder = Path(

            cache_folder

        )



        self.thumbnail_folder = (

            self.cache_folder

            /

            "thumbnails"

        )



        self.preview_folder = (

            self.cache_folder

            /

            "previews"

        )



        self.thumbnail_folder.mkdir(

            parents=True,

            exist_ok=True

        )


        self.preview_folder.mkdir(

            parents=True,

            exist_ok=True

        )



        # RAM cache

        self.memory_cache = {}





    # ==================================
    # CACHE KEY
    # ==================================


    def get_key(
            self,
            image_path
    ):


        image_path = Path(

            image_path

        )


        stat = image_path.stat()



        raw = (

            str(image_path)

            +

            str(stat.st_mtime)

            +

            str(stat.st_size)

        )



        return hashlib.md5(

            raw.encode()

        ).hexdigest()





    # ==================================
    # THUMBNAIL
    # ==================================


    def create_thumbnail(
            self,
            image_path
    ):


        key = self.get_key(

            image_path

        )



        cache_path = (

            self.thumbnail_folder

            /

            f"{key}.webp"

        )



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



                if image.mode != "RGB":


                    image = image.convert(

                        "RGB"

                    )



                image.save(

                    cache_path,

                    "WEBP",

                    quality=75

                )



            return cache_path



        except Exception as error:


            print(

                f"Thumbnail error: {error}"

            )


            return None





    # ==================================
    # PREVIEW
    # ==================================


    def create_preview(
            self,
            image_path,
            size=400
    ):


        key = self.get_key(

            image_path

        )



        cache_path = (

            self.preview_folder

            /

            f"{key}.webp"

        )



        if cache_path.exists():


            return cache_path




        try:


            with Image.open(

                image_path

            ) as image:



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

                    "WEBP",

                    quality=85

                )



            return cache_path



        except Exception as error:


            print(

                f"Preview error: {error}"

            )


            return None





    # ==================================
    # PIXMAP
    # ==================================


    def get_pixmap(
            self,
            image_path
    ):


        key = str(

            image_path

        )



        if key in self.memory_cache:


            return self.memory_cache[key]



        thumbnail = self.create_thumbnail(

            image_path

        )



        if thumbnail is None:


            return QPixmap()



        pixmap = QPixmap(

            str(thumbnail)

        )



        self.memory_cache[key] = pixmap



        return pixmap