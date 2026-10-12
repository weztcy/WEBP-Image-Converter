"""
Image library service.

Owns the collection of loaded images and exposes pure file-loading
helpers. Kept free of Qt widget code so the UI layer can focus on
rendering and interaction.
"""

from pathlib import Path

from PySide6.QtCore import QObject, Signal

from app.core.image_scanner import ImageScanner
from app.models.image_model import ImageModel


#: File extensions accepted by the converter.
SUPPORTED_FORMAT = {
    ".jpg",
    ".jpeg",
    ".png",
}


def is_supported(file_path) -> bool:
    """Return True when the file has a supported image extension."""
    try:
        return (
            Path(file_path).suffix.lower() in SUPPORTED_FORMAT
        )
    except Exception:
        return False


def load_files(files) -> list:
    """Build ImageModel instances for every supported path."""
    images = []
    for file in files:
        path = Path(file)
        if not is_supported(path):
            continue
        try:
            images.append(
                ImageModel(str(path.resolve()))
            )
        except Exception as error:
            print(f"Failed loading image {file}: {error}")
    return images


def load_folder(folder) -> list:
    """Build ImageModel instances for every supported file in the folder."""
    folder_path = Path(folder)
    if not folder_path.exists():
        return []

    images = []
    for extension in SUPPORTED_FORMAT:
        for file in folder_path.rglob(f"*{extension}"):
            if not file.is_file():
                continue
            try:
                images.append(
                    ImageModel(str(file.resolve()))
                )
            except Exception as error:
                print(f"Failed loading image {file}: {error}")
    return images


class ImageLibrary(QObject):
    """
    Domain store for the currently loaded image collection.

    Signals let the UI layer react to data changes without the widgets
    having to reach into the service internals.
    """

    #: A single image produced by a background folder scan.
    image_added = Signal(object)

    #: The collection changed (added / removed / cleared).
    changed = Signal()

    #: The active selection changed. Emits ImageModel or None.
    selection_changed = Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.images: list = []
        self.selected_image = None
        self.scanner = None

    # ------------------------------------------------------------------
    # ADD
    # ------------------------------------------------------------------

    def add_files(self, files) -> list:
        """Load the given files and append them to the collection."""
        images = load_files(files)
        self.images.extend(images)
        self.changed.emit()
        return images

    def add_paths(self, paths):
        """Add each path individually (mirrors drag & drop behaviour)."""
        for path in paths:
            self.add_files([path])

    def add_folder(self, folder):
        """Start a background scan of the folder using ImageScanner."""
        self.scanner = ImageScanner(folder)
        self.scanner.image_found.connect(self._append_scanned)
        self.scanner.start()

    def _append_scanned(self, image):
        self.images.append(image)
        self.image_added.emit(image)
        self.changed.emit()

    # ------------------------------------------------------------------
    # SELECTION
    # ------------------------------------------------------------------

    def set_selected(self, image):
        self.selected_image = image
        self.selection_changed.emit(image)

    def get_selected(self):
        return self.selected_image

    # ------------------------------------------------------------------
    # REMOVE / CLEAR
    # ------------------------------------------------------------------

    def remove_selected(self):
        """Drop the current selection from the collection."""
        deleted = self.selected_image
        if deleted is None:
            return None
        if deleted in self.images:
            self.images.remove(deleted)
        self.changed.emit()
        return deleted

    def clear(self):
        """Empty the collection and reset the selection."""
        self.images.clear()
        self.set_selected(None)
        self.changed.emit()

    # ------------------------------------------------------------------
    # QUERIES
    # ------------------------------------------------------------------

    def get_images(self) -> list:
        return self.images

    def count(self) -> int:
        return len(self.images)