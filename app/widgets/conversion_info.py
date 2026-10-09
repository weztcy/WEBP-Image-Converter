from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox
)


from PySide6.QtCore import Qt





class ConversionInfo(QWidget):


    def __init__(self):

        super().__init__()

        self.init_ui()





    def init_ui(self):


        layout = QVBoxLayout()



        info_box = QGroupBox(
            "Conversion Guide"
        )


        info_layout = QVBoxLayout()



        self.info_label = QLabel(
            """
<b>Compression Mode</b>

<br>

<b>Lossless Mode</b><br>
• Tidak mengurangi kualitas gambar.<br>
• Semua detail gambar dipertahankan.<br>
• Quality slider tidak digunakan.<br>
• Ukuran file biasanya lebih besar.<br>

<br>

<b>Lossy Mode</b><br>
• Menggunakan pengaturan Quality.<br>
• Quality tinggi (mendekati 100):
kualitas lebih baik, ukuran file lebih besar.<br>
• Quality rendah:
ukuran file lebih kecil, kualitas lebih berkurang.<br>

<br>

<b>Performance Profile</b>

<br>

<b>Fast Conversion (Method 2)</b><br>
• Prioritas kecepatan proses.<br>
• Cocok untuk konversi banyak gambar.<br>
• Ukuran file dapat sedikit lebih besar.<br>

<br>

<b>Standard Quality (Method 4)</b><br>
• Keseimbangan antara kecepatan dan ukuran file.<br>
• Pilihan terbaik untuk penggunaan umum.<br>

<br>

<b>Maximum Compression (Method 6)</b><br>
• Optimasi ukuran file lebih maksimal.<br>
• Membutuhkan waktu proses lebih lama.<br>

<br>

<b>Note:</b><br>
Performance Profile berlaku untuk proses encoding WEBP baik Lossy maupun Lossless.
            """
        )



        self.info_label.setWordWrap(
            True
        )


        self.info_label.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )



        info_layout.addWidget(
            self.info_label
        )



        info_box.setLayout(
            info_layout
        )



        layout.addWidget(
            info_box
        )


        self.setLayout(
            layout
        )