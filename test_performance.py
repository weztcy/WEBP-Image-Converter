from pathlib import Path
import time
import shutil
import psutil


from app.core.process_pool import ProcessPoolManager
from app.core.image_loader import load_folder



def main():


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



    # ==========================
    # WEBP SETTINGS
    # ==========================

    settings = {

        "mode": "lossy",

        "quality": 80,

        "profile": "compression"

    }



    # ==========================
    # CLEAN OUTPUT
    # ==========================

    if output_folder.exists():

        shutil.rmtree(
            output_folder
        )



    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )



    # ==========================
    # SYSTEM MONITOR
    # ==========================

    ram_before = (
        psutil.virtual_memory()
    )



    cpu_before = (
        psutil.cpu_percent(
            interval=1
        )
    )



    start = time.perf_counter()



    manager = ProcessPoolManager()



    result = manager.process(

        images,

        settings,

        str(output_folder)

    )



    end = time.perf_counter()



    ram_after = (
        psutil.virtual_memory()
    )



    cpu_after = (
        psutil.cpu_percent(
            interval=1
        )
    )



    elapsed = end - start



    output_files = len(
        list(
            output_folder.glob("*")
        )
    )



    total_size = sum(

        file.stat().st_size

        for file in output_folder.glob("*")

    )


    total_size_mb = (
        total_size
        /
        (1024 ** 2)
    )



    print(
        "\nRESULT"
    )


    print(
        result
    )


    print(
        f"Time: {elapsed:.2f}s"
    )


    print(
        f"CPU Before: {cpu_before}%"
    )


    print(
        f"CPU After: {cpu_after}%"
    )


    print(
        f"RAM Before: {ram_before.percent}%"
    )


    print(
        f"RAM After: {ram_after.percent}%"
    )


    print(
        f"Output Files: {output_files}"
    )


    print(
        f"Output Size: {total_size_mb:.2f} MB"
    )



if __name__ == "__main__":

    main()