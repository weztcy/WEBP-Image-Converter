from PySide6.QtWidgets import QWidget,QVBoxLayout
from app.widgets.settings_panel import SettingsPanel
from app.widgets.conversion_info import ConversionInfo
from app.widgets.output_panel import OutputPanel

class ConversionSection(QWidget):
    def __init__(self):
        super().__init__()
        l=QVBoxLayout(self)
        self.settings_panel=SettingsPanel()
        self.info=ConversionInfo()
        self.output_panel=OutputPanel()
        l.addWidget(self.info)
        l.addWidget(self.settings_panel)
        l.addWidget(self.output_panel)
    def get_settings(self): return self.settings_panel.get_settings()
    def get_output_folder(self): return self.output_panel.get_output_folder()
    def set_profile(self, profile):

        self.settings_panel.set_profile(
            profile
        )


    def set_workers(self, workers):

        self.settings_panel.set_workers(
            workers
        )


    def update_statistics(self, data):

        if hasattr(self, "stats"):
            self.stats.update_stats(data)


    def reset(self):

        self.settings_panel.reset()

        self.output_panel.reset()