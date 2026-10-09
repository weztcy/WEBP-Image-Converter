from pathlib import Path



def create_output_path(
        source_path,
        output_folder
):


    source = Path(
        source_path
    )


    folder = Path(
        output_folder
    )


    folder.mkdir(
        parents=True,
        exist_ok=True
    )


    return folder / (
        source.stem
        + ".webp"
    )