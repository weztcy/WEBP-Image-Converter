import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"


import shutil
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent

sys.path.insert(0, str(ROOT))


from PySide6.QtWidgets import QApplication

from PySide6.QtGui import QPixmap

from PIL import Image


from app.models.image_model import ImageModel
from app.widgets.image_list import ImageList
from app.widgets.image_preview import ImagePreview
from app.components.image_section import ImageSection



def make_images(n):

    folder = Path(
        tempfile.mkdtemp(
            prefix="webp_delete_test_"
        )
    )

    paths = []

    for i in range(n):

        path = folder / f"img_{i:03d}.png"

        img = Image.new(
            "RGB",
            (120, 80),
            (i * 40 % 255, 100, 200)
        )

        img.save(path)

        paths.append(path)


    models = [
        ImageModel(str(p))
        for p in paths
    ]

    return folder, models, paths



def cleanup_folder(folder):

    try:

        shutil.rmtree(
            folder,
            ignore_errors=True
        )

    except Exception:

        pass



def test_image_list_widget(app):

    print("\n=== Test A: ImageList widget ===", flush=True)

    lst = ImageList()

    folder, models, paths = make_images(5)

    lst.add_images(models)

    emitted = []

    lst.image_selected.connect(
        emitted.append
    )


    # user klik item pertama
    lst.handle_click(
        lst.item(0)
    )

    assert lst.current_selected_item is lst.item(0)

    assert lst.currentItem() is lst.item(0)


    # ---- delete pertama ----
    deleted = lst.remove_selected()

    assert deleted is models[0], "delete pertama harus menghapus gambar A"

    assert lst.count() == 4

    assert lst.current_selected_item is lst.item(0)

    assert lst.currentItem() is lst.item(0)

    assert lst.item(0).isSelected()

    assert emitted[-1] is models[1], (
        "setelah delete, harus auto-select gambar berikutnya (B)"
    )

    print("Delete pertama OK -> auto-select B, count =", lst.count(), flush=True)


    # ---- spam delete tanpa klik ulang ----
    expected = [models[1], models[2], models[3], models[4], None]

    for i in range(4):

        deleted = lst.remove_selected()

        assert deleted is expected[i], (
            f"spam delete ke-{i+2} harus menghapus gambar yg benar"
        )

        if lst.count() == 0:

            assert lst.current_selected_item is None

            assert emitted[-1] is None, (
                "list kosong harus emit None"
            )

        else:

            assert lst.current_selected_item is lst.item(0)

            assert emitted[-1] is expected[i + 1]

    assert lst.count() == 0

    assert emitted[-1] is None

    print("Spam delete OK -> list empty, emit None", flush=True)


    # delete saat list kosong = no-op aman
    assert lst.remove_selected() is None


    lst.clear()

    cleanup_folder(folder)

    print("Test A PASS", flush=True)



def test_image_section_flow(app):

    print("\n=== Test B: ImageSection end-to-end ===", flush=True)

    section = ImageSection()

    folder, models, paths = make_images(4)

    section.add_images(paths)

    assert len(section.images) == 4

    assert section.image_list.count() == 4

    assert section.count_label.text() == "4 Images"

    refs = list(
        section.images
    )


    # user klik thumbnail A
    section.image_list.handle_click(
        section.image_list.item(0)
    )

    assert section.get_selected() is refs[0]


    # ---- delete pertama : A dihapus, B otomatis terpilih ----
    section.remove_selected()

    assert len(section.images) == 3

    assert section.image_list.count() == 3

    assert section.get_selected() is refs[1], (
        "ImageSection.selected_image harus ikut pindah ke B"
    )

    assert section.image_list.current_selected_item is (
        section.image_list.item(0)
    )

    assert section.count_label.text() == "3 Images"

    print("Delete pertama OK -> counter 3, selected = B", flush=True)


    # ---- spam delete tanpa klik ulang ----
    section.remove_selected()

    assert len(section.images) == 2

    assert section.get_selected() is refs[2]

    assert section.count_label.text() == "2 Images"


    section.remove_selected()

    assert len(section.images) == 1

    assert section.get_selected() is refs[3]

    assert section.count_label.text() == "1 Images"

    print("Spam delete OK -> counter 2, 1", flush=True)


    # ---- delete saat hanya tersisa 1 gambar ----
    section.remove_selected()

    assert len(section.images) == 0

    assert section.image_list.count() == 0

    assert section.get_selected() is None

    assert section.count_label.text() == "0 Images"

    print("Delete last image OK -> counter 0, selected None", flush=True)


    # delete lagi saat kosong harus aman (no-op)
    section.remove_selected()

    assert len(section.images) == 0


    section.image_list.clear()

    # tunggu thread-thread preview selesai supaya teardown aman
    time.sleep(
        0.5
    )

    app.processEvents()

    loader = section.preview.loader

    if loader is not None:

        loader.wait()

    cleanup_folder(folder)

    print("Test B PASS", flush=True)




def test_preview_no_stale_override(app):

    print("\n=== Test C: preview menolak hasil loader basi ===", flush=True)

    preview = ImagePreview()

    folder, models, paths = make_images(4)

    key_a = str(models[0].path)

    key_b = str(models[1].path)



    # klik A lalu cepat pindah ke B sebelum A selesai dimuat

    preview.show_image(models[0])

    preview.show_image(models[1])



    # tunggu B (bukan A) selesai dimuat

    for _ in range(200):

        app.processEvents()

        if key_b in preview.pixmap_cache:

            break

        time.sleep(0.02)


    time.sleep(0.2)

    app.processEvents()


    assert key_b in preview.pixmap_cache


    b_pix = preview.pixmap_cache[key_b]


    # preview harus menampilkan gambar yang sedang dipilih (B)

    assert preview.current_pixmap is b_pix, (

        "preview harus menampilkan gambar yang sedang dipilih (B)"

    )



    # lalu hasil loader A yang basi muncul belakangan

    stale = QPixmap(
        5,
        5
    )


    preview.set_preview(
        key_a,
        stale
    )


    # tidak boleh menimpa preview yang sedang menampilkan B

    assert preview.current_pixmap is b_pix, (

        "hasil basi tidak boleh menimpa preview gambar lain"

    )



    # hasil basi tetap boleh masuk cache

    assert preview.pixmap_cache.get(
        key_a
    ) is stale



    # pilih A lagi -> sekarang pakai cache, preview berganti ke A

    preview.show_image(
        models[0]
    )


    assert preview.current_pixmap is stale, (

        "pilih ulang A harus langsung tampil dari cache"

    )



    # ============================================================
    # reproduksi crash RuntimeError yang dulu muncul di main.py:
    # loader selesai -> di-deleteLater -> self.loader masih
    # menunjuk objek mati -> seleksi gambar baru crash di quit()
    # ============================================================

    key_c = str(models[2].path)

    key_d = str(models[3].path)



    # pilih C yang belum pernah dimuat -> loader baru berjalan

    preview.show_image(
        models[2]
    )

    assert preview.current_key == key_c



    # tunggu sampai loader C selesai & dibersihkan

    for _ in range(200):

        app.processEvents()

        if key_c in preview.pixmap_cache:

            break

        time.sleep(0.02)


    time.sleep(0.3)

    app.processEvents()


    assert key_c in preview.pixmap_cache

    assert preview.loader is None, (

        "loader yang selesai harus dilepas dari self.loader"

    )



    # pilih D (belum di-cache) -> dulu crash RuntimeError di sini

    preview.show_image(
        models[3]
    )



    # tunggu D selesai -> preview harus menampilkan D

    for _ in range(200):

        app.processEvents()

        if key_d in preview.pixmap_cache:

            break

        time.sleep(0.02)


    time.sleep(0.2)

    app.processEvents()


    d_pix = preview.pixmap_cache[key_d]

    assert preview.current_pixmap is d_pix, (

        "preview akhir harus menampilkan D"

    )



    # bersihkan thread yang masih berjalan

    time.sleep(0.3)

    app.processEvents()


    loader = preview.loader

    if loader is not None:

        loader.wait()


    cleanup_folder(folder)

    print("Test C PASS", flush=True)



if __name__ == "__main__":

    app = QApplication(
        sys.argv
    )

    only_b = "--only-b" in sys.argv

    if not only_b:
        test_image_list_widget(app)

        test_image_section_flow(app)

        test_preview_no_stale_override(app)

    else:

        test_image_section_flow(app)

    print("\nALL TESTS PASSED", flush=True)