from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QRadioButton,
    QLabel,
    QSlider,
    QFrame
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
        
        self.last_lossy_quality = 80



    # =================================
    # UI
    # =================================

    def init_ui(self):


        self.setStyleSheet(

        """

        QWidget {

            font-family:
            "Inter",
            "Segoe UI";

        }



        QFrame#card {

            background:#10141C;

            border:1px solid #242938;

            border-radius:18px;

        }



        QLabel#title {

            color:#F9FAFB;

            font-size:15px;

            font-weight:800;

        }



        QLabel#description {

            color:#98A2B3;

            font-size:12px;

        }



        QLabel#value {

            color:#F9FAFB;

            font-size:26px;

            font-weight:800;

        }



        QLabel#value[status="lossless"] {

            color:#EF4444;

        }



        QLabel#qualityStatus {

            color:#7EA6FF;

            font-size:12px;

            font-weight:700;

        }



        QLabel#qualityStatus[status="lossless"] {

            color:#EF4444;

        }



        QRadioButton {

            color:#D1D5DB;

            spacing:10px;

            font-size:13px;

            font-weight:600;

        }



        QRadioButton::indicator {

            width:16px;

            height:16px;

            border-radius:8px;

            border:2px solid #4B5563;

        }



        QRadioButton::indicator:checked {

            background:#4F8CFF;

            border:2px solid #4F8CFF;

        }




        /* ===============================
        DEFAULT = LOSSY (BLUE)
        =============================== */


        QSlider::groove:horizontal {

            height:6px;

            background:#30384A;

            border-radius:3px;

        }


        QSlider::sub-page:horizontal {

            background:#4F8CFF;

            border-radius:3px;

        }


        QSlider::handle:horizontal {

            background:#FFFFFF;

            border:3px solid #4F8CFF;

            width:18px;

            height:18px;

            margin:-7px 0;

            border-radius:9px;

        }



        /* ===============================
        LOSSLESS (RED)
        =============================== */


        QSlider[mode="lossless"]::sub-page:horizontal {

            background:#EF4444;

        }



        QSlider[mode="lossless"]::handle:horizontal {

            border:3px solid #EF4444;

        }



        QLabel#qualityStatus[status="lossless"] {

            color:#EF4444;

        }



        QLabel#value[status="lossless"] {

            color:#EF4444;

        }


        """

        )
        
        layout = QVBoxLayout(self)

        layout.setSpacing(
            16
        )



        # ===============================
        # COMPRESSION MODE
        # ===============================


        mode_card = QFrame()

        mode_card.setObjectName(
            "card"
        )


        mode_layout = QVBoxLayout(
            mode_card
        )


        title = QLabel(
            "Compression Mode"
        )

        title.setObjectName(
            "title"
        )


        desc = QLabel(
            "Select the compression method for WEBP output."
        )

        desc.setObjectName(
            "description"
        )



        mode_row = QHBoxLayout()



        self.lossy_radio = QRadioButton(
            "Lossy"
        )


        self.lossless_radio = QRadioButton(
            "Lossless"
        )


        self.lossy_radio.setChecked(
            True
        )



        mode_row.addWidget(
            self.lossy_radio
        )


        mode_row.addWidget(
            self.lossless_radio
        )


        mode_row.addStretch()



        mode_layout.addWidget(
            title
        )


        mode_layout.addWidget(
            desc
        )


        mode_layout.addLayout(
            mode_row
        )



        layout.addWidget(
            mode_card
        )





        # ===============================
        # QUALITY
        # ===============================


        quality_card = QFrame()

        quality_card.setObjectName(
            "card"
        )


        self.quality_group = quality_card



        quality_layout = QVBoxLayout(
            quality_card
        )



        header = QHBoxLayout()



        quality_title = QLabel(
            "Quality"
        )

        quality_title.setObjectName(
            "title"
        )



        self.quality_label = QLabel(
            "80"
        )

        self.quality_label.setObjectName(
            "value"
        )



        header.addWidget(
            quality_title
        )


        header.addStretch()


        header.addWidget(
            self.quality_label
        )



        self.quality_status = QLabel(
            "High Quality"
        )


        self.quality_status.setObjectName(
            "qualityStatus"
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


        self.quality_slider.setProperty(
            "mode",
            "lossy"
        )



        quality_layout.addLayout(
            header
        )


        quality_layout.addWidget(
            self.quality_status
        )


        quality_layout.addWidget(
            self.quality_slider
        )



        layout.addWidget(
            quality_card
        )
        
        # ===============================
        # PERFORMANCE
        # ===============================


        profile_card = QFrame()

        profile_card.setObjectName(
            "card"
        )


        profile_layout = QVBoxLayout(
            profile_card
        )


        title = QLabel(
            "Performance Profile"
        )

        title.setObjectName(
            "title"
        )


        desc = QLabel(
            "Balance speed and compression efficiency."
        )

        desc.setObjectName(
            "description"
        )



        self.fast_radio = QRadioButton(
            "Fast Conversion"
        )


        self.standard_radio = QRadioButton(
            "Standard Quality"
        )


        self.compression_radio = QRadioButton(
            "Maximum Compression"
        )


        self.standard_radio.setChecked(
            True
        )



        for w in [

            title,
            desc,
            self.fast_radio,
            self.standard_radio,
            self.compression_radio

        ]:

            profile_layout.addWidget(
                w
            )



        layout.addWidget(
            profile_card
        )



        # SIGNAL


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


        self.update_state()




    # =================================
    # STATE
    # =================================


    def update_state(self):

        is_lossy = self.lossy_radio.isChecked()


        if is_lossy:

            # ======================
            # LOSSY MODE
            # ======================

            self.quality_slider.blockSignals(True)


            # selalu kembali ke default Lossy
            self.quality_slider.setValue(
                80
            )


            self.quality_slider.blockSignals(False)


            self.quality_slider.setProperty(
                "mode",
                "lossy"
            )


            self.quality_slider.setAttribute(
                Qt.WA_TransparentForMouseEvents,
                False
            )


            self.quality_label.setText(
                "80"
            )


            self.quality_status.setText(
                "High Quality"
            )


            self.quality_label.setProperty(
                "status",
                "lossy"
            )


            self.quality_status.setProperty(
                "status",
                "lossy"
            )



        else:

            # ======================
            # LOSSLESS MODE
            # ======================

            self.quality_slider.blockSignals(True)


            # hanya visual
            self.quality_slider.setValue(
                100
            )


            self.quality_slider.blockSignals(False)


            self.quality_slider.setProperty(
                "mode",
                "lossless"
            )


            self.quality_slider.setAttribute(
                Qt.WA_TransparentForMouseEvents,
                True
            )


            self.quality_label.setText(
                "100"
            )


            self.quality_status.setText(
                "Unavailable in Lossless Mode"
            )


            self.quality_label.setProperty(
                "status",
                "lossless"
            )


            self.quality_status.setProperty(
                "status",
                "lossless"
            )


        # refresh style

        for widget in [

            self.quality_slider,
            self.quality_label,
            self.quality_status

        ]:

            widget.style().unpolish(widget)

            widget.style().polish(widget)


        self.emit_settings()





    def update_quality(
            self,
            value
    ):


        self.quality_label.setText(
            str(value)
        )



        if value >= 80:

            self.quality_status.setText(
                "High Quality"
            )


        elif value >= 50:

            self.quality_status.setText(
                "Balanced Quality"
            )


        else:

            self.quality_status.setText(
                "Small File Size"
            )


        self.emit_settings()




    def get_profile(self):

        if self.standard_radio.isChecked():

            return "balanced"


        if self.compression_radio.isChecked():

            return "compression"


        return "fast"




    def build_settings(self):


        mode = (

            "lossy"

            if self.lossy_radio.isChecked()

            else "lossless"

        )


        return {

            "mode":mode,


            "quality":

                self.quality_slider.value()

                if mode=="lossy"

                else None,


            "profile":

                self.get_profile()

        }




    def emit_settings(self):

        self.settings_changed.emit(

            self.build_settings()

        )



    def get_settings(self):

        return self.build_settings()