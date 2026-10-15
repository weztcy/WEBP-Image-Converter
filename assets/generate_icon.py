"""Generate the application icon (app_icon.ico) used by the PyInstaller build."""


from pathlib import Path

from PIL import (
    Image,
    ImageDraw,
    ImageFont
)



OUT_PATH = (
    Path(__file__).resolve().parent
    / "app_icon.ico"
)


SIZE = 512




def _lerp(
        start,
        end,
        t
):

    return int(

        start
        +
        (end - start)
        * t

    )




def build_icon():


    image = Image.new(
        "RGBA",
        (SIZE, SIZE),
        (0, 0, 0, 0)
    )


    draw = ImageDraw.Draw(
        image
    )


    # ==========================
    # LATAR GRADASI BIRU-UNGU
    # ==========================


    for y in range(SIZE):

        t = y / SIZE


        draw.line(

            [(0, y), (SIZE, y)],

            fill=(

                _lerp(0x4F, 0x7A, t),

                _lerp(0x8C, 0x5C, t),

                0xFF,

                255

            )

        )



    # ==========================
    # SUDUT MEMBULAT (MASK)
    # ==========================


    mask = Image.new(
        "L",
        (SIZE, SIZE),
        0
    )


    ImageDraw.Draw(
        mask
    ).rounded_rectangle(

        [0, 0, SIZE - 1, SIZE - 1],

        radius=SIZE // 5,

        fill=255

    )


    image.putalpha(
        mask
    )



    # ==========================
    # MONOGRAM "W"
    # ==========================


    try:

        font = ImageFont.truetype(

            "C:/Windows/Fonts/arialbd.ttf",

            int(SIZE * 0.6)

        )


    except Exception:

        font = ImageFont.load_default()


    bbox = draw.textbbox(
        (0, 0),
        "W",
        font=font
    )


    text_w = bbox[2] - bbox[0]

    text_h = bbox[3] - bbox[1]


    x = (
        (SIZE - text_w)
        / 2
        - bbox[0]
    )


    y = (
        (SIZE - text_h)
        / 2
        - bbox[1]
    )


    draw.text(

        (x, y),

        "W",

        font=font,

        fill=(255, 255, 255, 255)

    )




    OUT_PATH.parent.mkdir(

        parents=True,

        exist_ok=True

    )


    image.save(

        OUT_PATH,

        format="ICO",

        sizes=[

            (256, 256),

            (128, 128),

            (64, 64),

            (48, 48),

            (32, 32),

            (16, 16)

        ]

    )


    print(
        f"Icon written: {OUT_PATH}"
    )




if __name__ == "__main__":

    build_icon()