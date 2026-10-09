from pathlib import Path
import time


from app.core.process_pool import ProcessPoolManager
from app.core.image_loader import load_folder



def main():


    # ==========================
    # INPUT TEST
    # ==========================

    input_folder = Path(
        r"D:\TEST_IMAGES"
    )


    output_folder = Path(
        r"D:\TEST_OUTPUT_WEBP"
    )



    print(
        "Loading images..."
    )


    images = load_folder(
        input_folder
    )


    print(
        f"Total images: {len(images)}"
    )



    if not images:

        print(
            "No images found"
        )

        return



    settings = {

        "mode": "lossy",

        "quality": 80

    }



    # ==========================
    # START BENCHMARK
    # ==========================


    start = time.perf_counter()



    manager = ProcessPoolManager()



    result = manager.process(

        images,

        settings,

        str(output_folder)

    )



    end = time.perf_counter()



    elapsed = end - start



    print(
        "\nRESULT"
    )


    print(
        result
    )


    print(
        f"Time: {elapsed:.2f} seconds"
    )



if __name__ == "__main__":

    main()