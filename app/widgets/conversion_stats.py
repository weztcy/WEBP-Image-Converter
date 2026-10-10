from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)



class ConversionStats(QWidget):


    def __init__(self):

        super().__init__()

        self.init_ui()



    # =====================================
    # UI
    # =====================================

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

                border-radius:20px;

            }



            QFrame#metricCard {

                background:#181D27;

                border-radius:14px;

            }



            QFrame#successCard {

                background:#10251D;

                border:1px solid #166534;

                border-radius:14px;

            }



            QFrame#failedCard {

                background:#25151A;

                border:1px solid #7F1D1D;

                border-radius:14px;

            }



            QFrame#savedCard {

                background:#10251D;

                border:1px solid #1F9D68;

                border-radius:14px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:16px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#metricValue {

                color:#F9FAFB;

                font-size:24px;

                font-weight:900;

            }



            QLabel#metricLabel {

                color:#98A2B3;

                font-size:11px;

                font-weight:700;

            }



            QLabel#successValue {

                color:#34D399;

                font-size:18px;

                font-weight:900;

            }



            QLabel#failedValue {

                color:#F87171;

                font-size:18px;

                font-weight:900;

            }



            QLabel#detailTitle {

                color:#98A2B3;

                font-size:11px;

                font-weight:700;

            }



            QLabel#detailValue {

                color:#DCE6FF;

                font-size:14px;

                font-weight:800;

            }



            QLabel#savedValue {

                color:#34D399;

                font-size:22px;

                font-weight:900;

            }

            """
        )



        root = QVBoxLayout(self)


        root.setContentsMargins(
            0,
            0,
            0,
            0
        )



        card = QFrame()

        card.setObjectName(
            "card"
        )



        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            18,
            18,
            18,
            18
        )


        layout.setSpacing(
            14
        )



        # ==============================
        # HEADER
        # ==============================


        title = QLabel(
            "📈 Conversion Statistics"
        )

        title.setObjectName(
            "title"
        )



        subtitle = QLabel(
            "Summary of the latest conversion process."
        )

        subtitle.setObjectName(
            "subtitle"
        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            subtitle
        )



        # ==============================
        # MAIN METRIC
        # ==============================


        metrics = QHBoxLayout()

        metrics.setSpacing(
            12
        )


        total_card, self.total_value = self.create_metric(
            "0",
            "Files"
        )


        saved_card, self.saved_metric = self.create_metric(
            "0%",
            "Saved"
        )


        metrics.addWidget(
            total_card
        )


        metrics.addWidget(
            saved_card
        )


        layout.addLayout(
            metrics
        )



        # ==============================
        # STATUS
        # ==============================


        status = QHBoxLayout()

        status.setSpacing(
            12
        )


        success_card, self.success_value = self.create_status(
            "✓ Success",
            "0 Files",
            True
        )


        failed_card, self.failed_value = self.create_status(
            "✕ Failed",
            "0 Errors",
            False
        )


        status.addWidget(
            success_card
        )


        status.addWidget(
            failed_card
        )


        layout.addLayout(
            status
        )



        # ==============================
        # DETAILS
        # ==============================


        details = QHBoxLayout()

        details.setSpacing(
            12
        )


        left = QVBoxLayout()

        right = QVBoxLayout()



        self.duration = self.create_detail(
            "Duration",
            "-"
        )


        self.input_size = self.create_detail(
            "Input Size",
            "-"
        )


        self.speed = self.create_detail(
            "Speed",
            "-"
        )


        self.output_size = self.create_detail(
            "Output Size",
            "-"
        )



        left.addWidget(
            self.duration
        )

        left.addWidget(
            self.input_size
        )


        right.addWidget(
            self.speed
        )

        right.addWidget(
            self.output_size
        )


        details.addLayout(
            left
        )


        details.addLayout(
            right
        )


        layout.addLayout(
            details
        )



        # ==============================
        # SAVING
        # ==============================


        saved = QFrame()

        saved.setObjectName(
            "savedCard"
        )


        saved_layout = QHBoxLayout(saved)


        saved_layout.setContentsMargins(
            14,
            10,
            14,
            10
        )



        saved_title = QLabel(
            "💾 Compression Saved"
        )

        saved_title.setObjectName(
            "detailTitle"
        )



        self.saved_value = QLabel(
            "0%"
        )

        self.saved_value.setObjectName(
            "savedValue"
        )



        saved_layout.addWidget(
            saved_title
        )


        saved_layout.addStretch()


        saved_layout.addWidget(
            self.saved_value
        )



        layout.addWidget(
            saved
        )



        root.addWidget(
            card
        )



    # =====================================
    # COMPONENT
    # =====================================


    def create_metric(
            self,
            value,
            label
    ):


        frame = QFrame()

        frame.setObjectName(
            "metricCard"
        )


        layout = QVBoxLayout(frame)


        layout.setContentsMargins(
            14,
            12,
            14,
            12
        )



        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "metricValue"
        )


        text = QLabel(
            label
        )

        text.setObjectName(
            "metricLabel"
        )


        layout.addWidget(
            value_label
        )


        layout.addWidget(
            text
        )


        return frame, value_label




    def create_status(
            self,
            title,
            value,
            success
    ):


        frame = QFrame()


        frame.setObjectName(

            "successCard"
            if success
            else
            "failedCard"

        )


        layout = QVBoxLayout(frame)


        layout.setContentsMargins(
            14,
            10,
            14,
            10
        )


        label = QLabel(
            title
        )

        label.setObjectName(
            "detailTitle"
        )



        value_label = QLabel(
            value
        )


        value_label.setObjectName(

            "successValue"
            if success
            else
            "failedValue"

        )


        layout.addWidget(
            label
        )


        layout.addWidget(
            value_label
        )


        return frame, value_label




    def create_detail(
            self,
            title,
            value
    ):


        frame = QFrame()

        frame.setObjectName(
            "metricCard"
        )


        layout = QVBoxLayout(frame)


        layout.setContentsMargins(
            12,
            10,
            12,
            10
        )



        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "detailTitle"
        )



        value_label = QLabel(
            value
        )

        value_label.setObjectName(
            "detailValue"
        )


        layout.addWidget(
            title_label
        )


        layout.addWidget(
            value_label
        )


        frame.value_label = value_label


        return frame



    # =====================================
    # UPDATE
    # =====================================


    def update_stats(
            self,
            data
    ):


        self.total_value.setText(
            str(data["total"])
        )


        self.saved_metric.setText(
            f"{data['saved_percent']:.1f}%"
        )


        self.success_value.setText(
            f"{data['success']} Files"
        )


        self.failed_value.setText(
            f"{data['failed']} Errors"
        )


        self.duration.value_label.setText(
            f"{data['duration']:.2f}s"
        )


        self.speed.value_label.setText(
            f"{data['speed']:.2f} img/s"
        )


        self.input_size.value_label.setText(
            f"{data['input_mb']:.2f} MB"
        )


        self.output_size.value_label.setText(
            f"{data['output_mb']:.2f} MB"
        )


        self.saved_value.setText(
            f"{data['saved_percent']:.2f}%"
        )