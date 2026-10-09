from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QLabel,
    QSlider,
    QGroupBox
)


from PySide6.QtCore import (
    Qt,
    Signal
)





class SettingsPanel(QWidget):


    settings_changed = Signal(dict)



    def __init__(self):

        super().__init__()


        self.init_ui()





    # =================================
    # UI INITIALIZATION
    # =================================


    def init_ui(self):


        layout = QVBoxLayout()



        # =================================
        # COMPRESSION MODE
        # =================================


        mode_group = QGroupBox(
            "Compression Mode"
        )


        mode_layout = QVBoxLayout()



        self.lossy_radio = QRadioButton(
            "Lossy"
        )


        self.lossless_radio = QRadioButton(
            "Lossless"
        )


        self.lossy_radio.setChecked(
            True
        )



        mode_layout.addWidget(
            self.lossy_radio
        )


        mode_layout.addWidget(
            self.lossless_radio
        )


        mode_group.setLayout(
            mode_layout
        )





        # =================================
        # QUALITY CONTROL
        # =================================


        quality_group = QGroupBox(
            "Quality"
        )


        quality_layout = QVBoxLayout()



        self.quality_label = QLabel(
            "Quality: 80"
        )


        self.quality_slider = QSlider(
            Qt.Horizontal
        )


        self.quality_slider.setRange(
            1,
            100
        )


        self.quality_slider.setValue(
            80
        )


        self.quality_slider.setEnabled(
            True
        )



        quality_layout.addWidget(
            self.quality_label
        )


        quality_layout.addWidget(
            self.quality_slider
        )


        quality_group.setLayout(
            quality_layout
        )





        # =================================
        # PERFORMANCE PROFILE
        # =================================


        profile_group = QGroupBox(
            "Performance Profile"
        )


        profile_layout = QVBoxLayout()



        self.fast_radio = QRadioButton(
            "Fast Conversion"
        )


        self.standard_radio = QRadioButton(
            "Standard Quality"
        )


        self.compression_radio = QRadioButton(
            "Maximum Compression"
        )



        self.fast_radio.setChecked(
            True
        )



        profile_layout.addWidget(
            self.fast_radio
        )


        profile_layout.addWidget(
            self.standard_radio
        )


        profile_layout.addWidget(
            self.compression_radio
        )


        profile_group.setLayout(
            profile_layout
        )





        # =================================
        # SIGNAL CONNECTION
        # =================================


        self.lossy_radio.toggled.connect(
            self.update_state
        )


        self.lossless_radio.toggled.connect(
            self.update_state
        )



        self.quality_slider.valueChanged.connect(
            self.update_quality
        )



        self.fast_radio.toggled.connect(
            self.emit_settings
        )


        self.standard_radio.toggled.connect(
            self.emit_settings
        )


        self.compression_radio.toggled.connect(
            self.emit_settings
        )





        # =================================
        # ADD COMPONENT
        # =================================


        layout.addWidget(
            mode_group
        )


        layout.addWidget(
            quality_group
        )


        layout.addWidget(
            profile_group
        )


        self.setLayout(
            layout
        )



        self.emit_settings()





    # =================================
    # STATE UPDATE
    # =================================


    def update_state(self):


        is_lossy = (

            self.lossy_radio.isChecked()

        )



        self.quality_slider.setEnabled(
            is_lossy
        )


        self.emit_settings()





    def update_quality(
            self,
            value
    ):


        self.quality_label.setText(

            f"Quality: {value}"

        )


        self.emit_settings()





    # =================================
    # PROFILE
    # =================================


    def get_profile(self):


        if self.standard_radio.isChecked():

            return "balanced"



        if self.compression_radio.isChecked():

            return "compression"



        return "fast"





    # =================================
    # SETTINGS BUILDER
    # =================================


    def build_settings(self):


        mode = (

            "lossy"

            if self.lossy_radio.isChecked()

            else "lossless"

        )



        return {


            "mode": mode,



            # Quality hanya berlaku untuk lossy

            "quality":

                self.quality_slider.value()

                if mode == "lossy"

                else None,



            "profile":

                self.get_profile()

        }





    # =================================
    # SIGNAL EMIT
    # =================================


    def emit_settings(self):


        self.settings_changed.emit(

            self.build_settings()

        )





    # =================================
    # PUBLIC API
    # =================================


    def get_settings(self):


        return self.build_settings()