from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from app.widgets.image_list import ImageList
from app.widgets.image_preview import ImagePreview
from app.core.image_loader import load_files

class ImageSection(QWidget):
    def __init__(self):
        super().__init__()
        self.images=[]
        self.selected_image=None
        self.image_list=ImageList()
        self.preview=ImagePreview()
        self.remove_button=QPushButton("Remove Selected")
        self.delete_button=QPushButton("Delete All")
        self.init_ui()
        self.image_list.image_selected.connect(self._selected)
    def init_ui(self):
        root=QVBoxLayout(self)
        row=QHBoxLayout()
        row.addWidget(self.image_list,2)
        row.addWidget(self.preview,1)
        actions=QHBoxLayout()
        actions.addWidget(self.remove_button)
        actions.addWidget(self.delete_button)
        root.addLayout(row)
        root.addLayout(actions)
        self.remove_button.clicked.connect(self.remove_selected)
        self.delete_button.clicked.connect(self.clear)
    def _selected(self,img):
        self.selected_image=img
        self.preview.show_image(img)
    def add_images(self, files):
        imgs=load_files(files)
        self.images.extend(imgs)
        self.image_list.add_images(imgs)
    def add_paths(self, paths):
        for p in paths:
            self.add_images([p])
    def add_folder(self, folder):
        from app.core.image_scanner import ImageScanner
        self.scanner=ImageScanner(folder)
        self.scanner.image_found.connect(lambda x:(self.images.append(x),self.image_list.add_images([x])))
        self.scanner.start()
    def get_selected(self): return self.selected_image
    def get_images(self): return self.images
    def remove_selected(self):
        if self.selected_image in self.images: self.images.remove(self.selected_image)
        self.image_list.remove_selected()
        self.preview.show_empty()
        self.selected_image=None
    def clear(self):
        self.images.clear()
        self.image_list.clear()
        self.preview.show_empty()
        self.selected_image=None
