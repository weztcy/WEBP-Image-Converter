from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QLabel,
    QSlider
)


from PySide6.QtCore import Qt, Signal



class SettingsPanel(QWidget):


    settings_changed = Signal(dict)



    def __init__(self):

        super().__init__()


        self.init_ui()



    def init_ui(self):

        layout = QVBoxLayout()



        self.lossless_radio = QRadioButton(
            "Lossless"
        )


        self.lossy_radio = QRadioButton(
            "Lossy"
        )



        self.lossless_radio.setChecked(
            True
        )



        self.quality_label = QLabel(
            "Quality: 80"
        )


        self.quality_slider = QSlider(
            Qt.Horizontal
        )


        self.quality_slider.setMinimum(
            1
        )


        self.quality_slider.setMaximum(
            100
        )


        self.quality_slider.setValue(
            80
        )


        self.quality_slider.setEnabled(
            False
        )



        self.lossless_radio.clicked.connect(
            self.update_state
        )


        self.lossy_radio.clicked.connect(
            self.update_state
        )


        self.quality_slider.valueChanged.connect(
            self.update_quality
        )



        layout.addWidget(
            self.lossless_radio
        )


        layout.addWidget(
            self.lossy_radio
        )


        layout.addWidget(
            self.quality_label
        )


        layout.addWidget(
            self.quality_slider
        )



        self.setLayout(
            layout
        )


        self.emit_settings()



    def update_state(self):

        is_lossy = self.lossy_radio.isChecked()



        self.quality_slider.setEnabled(
            is_lossy
        )


        self.emit_settings()



    def update_quality(self, value):

        self.quality_label.setText(
            f"Quality: {value}"
        )


        self.emit_settings()



    def build_settings(self):

        return {

            "mode":
                "lossy"
                if self.lossy_radio.isChecked()
                else "lossless",


            "quality":
                self.quality_slider.value()

        }



    def emit_settings(self):

        self.settings_changed.emit(
            self.build_settings()
        )



    def get_settings(self):

        return self.build_settings()