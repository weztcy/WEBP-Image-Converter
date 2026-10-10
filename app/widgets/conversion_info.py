from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QSizePolicy
)

from PySide6.QtCore import Qt



class ConversionInfo(QWidget):


    def __init__(self):

        super().__init__()

        self.init_ui()



    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#mainCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }



            QFrame#infoCard {

                background:#10141C;

                border:1px solid #252D3D;

                border-radius:18px;

            }



            QFrame#recommendedCard {

                background:#101B18;

                border:1px solid #1F9D68;

                border-radius:18px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#cardTitle {

                color:#E5E7EB;

                font-size:14px;

                font-weight:800;

            }



            QLabel#itemTitle {

                color:#F9FAFB;

                font-size:13px;

                font-weight:700;

            }



            QLabel#itemDesc {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#badgeGreen {

                background:#123D2D;

                color:#34D399;

                border-radius:8px;

                padding:4px 10px;

                font-size:10px;

                font-weight:800;

            }



            QLabel#tip {

                color:#A7F3D0;

                background:#10251D;

                border-radius:12px;

                padding:10px;

                font-size:12px;

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


        main = QFrame()

        main.setObjectName(
            "mainCard"
        )


        layout = QVBoxLayout(main)


        layout.setContentsMargins(
            22,
            22,
            22,
            22
        )


        layout.setSpacing(
            16
        )


        # HEADER

        title = QLabel(
            "📘 Conversion Guide"
        )

        title.setObjectName(
            "title"
        )


        subtitle = QLabel(
            "Choose the right balance between quality, size, and speed."
        )

        subtitle.setObjectName(
            "subtitle"
        )


        layout.addWidget(title)

        layout.addWidget(subtitle)



        # TWO CARD

        cards = QHBoxLayout()

        cards.setSpacing(
            16
        )



        cards.addWidget(
            self.create_compression_card(),
            1
        )


        cards.addWidget(
            self.create_performance_card(),
            1
        )



        layout.addLayout(
            cards
        )



        tip = QLabel(
            "💡 Recommended: Standard Quality provides the best balance for everyday WEBP conversion."
        )


        tip.setObjectName(
            "tip"
        )


        tip.setWordWrap(
            True
        )


        layout.addWidget(
            tip
        )



        root.addWidget(
            main
        )



    # ======================================
    # LEFT CARD
    # ======================================

    def create_compression_card(self):


        card = QFrame()

        card.setObjectName(
            "infoCard"
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


        title = QLabel(
            "🖼 Compression Mode"
        )

        title.setObjectName(
            "cardTitle"
        )


        layout.addWidget(
            title
        )


        # ==========================
        # LOSSLESS
        # ==========================

        layout.addWidget(
            self.create_item(
                "🔒 Lossless",
                "Original quality preserved with no quality reduction."
            )
        )


        # ==========================
        # LOSSY
        # ==========================

        lossy = QFrame()

        lossy.setObjectName(
            "infoCard"
        )

        lossy_layout = QVBoxLayout(
            lossy
        )

        lossy_layout.setContentsMargins(
            12,
            10,
            12,
            10
        )

        lossy_layout.setSpacing(
            8
        )

        header = QLabel(
            "🎚 Lossy"
        )

        header.setObjectName(
            "itemTitle"
        )

        desc = QLabel(
            "Adjust quality level to control output file size."
        )

        desc.setObjectName(
            "itemDesc"
        )

        badge = QLabel(
            "⭐ Recommended Quality: 80"
        )

        badge.setObjectName(
            "badgeGreen"
        )

        badge.setSizePolicy(
            QSizePolicy.Fixed,
            QSizePolicy.Fixed
        )
        
        badge.adjustSize()
        
        note = QLabel(
            "Lower quality produces smaller files. "
            "Higher quality preserves more image details."
        )

        note.setObjectName(
            "note"
        )

        note.setWordWrap(
            True
        )

        lossy_layout.addWidget(
            header
        )

        lossy_layout.addWidget(
            desc
        )

        lossy_layout.addWidget(
            badge
        )

        lossy_layout.addWidget(
            note
        )

        layout.addWidget(
            lossy
        )


        layout.addStretch()


        return card



    # ======================================
    # RIGHT CARD
    # ======================================

    def create_performance_card(self):


        wrapper = QFrame()

        wrapper.setObjectName(
            "infoCard"
        )


        layout = QVBoxLayout(wrapper)

        layout.setContentsMargins(
            18,
            18,
            18,
            18
        )


        layout.setSpacing(
            12
        )


        title = QLabel(
            "⚡ Performance Profile"
        )

        title.setObjectName(
            "cardTitle"
        )


        layout.addWidget(
            title
        )


        layout.addWidget(
            self.create_item(
                "🚀 Fast Conversion",
                "Prioritize speed for large batch processing."
            )
        )


        recommended = self.create_item(
            "⭐ Standard Quality",
            "Balanced speed and compression. Best choice for most users.",
            True
        )


        layout.addWidget(
            recommended
        )


        layout.addWidget(
            self.create_item(
                "🗜 Maximum Compression",
                "Smallest file size with longer processing time."
            )
        )


        return wrapper



    # ======================================
    # ITEM COMPONENT
    # ======================================

    def create_item(
            self,
            title,
            desc,
            recommended=False
    ):


        frame = QFrame()


        if recommended:

            frame.setObjectName(
                "recommendedCard"
            )

        else:

            frame.setObjectName(
                "infoCard"
            )



        layout = QVBoxLayout(frame)

        layout.setContentsMargins(
            12,
            10,
            12,
            10
        )


        header = QHBoxLayout()


        title_label = QLabel(
            title
        )

        title_label.setObjectName(
            "itemTitle"
        )


        header.addWidget(
            title_label
        )


        if recommended:

            badge = QLabel(
                "RECOMMENDED"
            )


            badge.setObjectName(
                "badgeGreen"
            )


            header.addStretch()


            header.addWidget(
                badge
            )



        desc_label = QLabel(
            desc
        )


        desc_label.setObjectName(
            "itemDesc"
        )


        desc_label.setWordWrap(
            True
        )


        layout.addLayout(
            header
        )


        layout.addWidget(
            desc_label
        )


        return frame