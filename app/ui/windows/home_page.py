from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame,
    QSizePolicy,
    QGraphicsDropShadowEffect
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


from app.styles.theme import THEME

class HomePage(QWidget):

    def __init__(self, start_convert_callback):
        super().__init__()

        self.start_convert_callback = start_convert_callback

        self.init_ui()

    def init_ui(self):
        self.setObjectName("homePage")
        self.setStyleSheet(
            THEME["home_page"]
        )

        root = QVBoxLayout(self)
        root.setContentsMargins(36, 28, 36, 28)
        root.setSpacing(0)
        root.setAlignment(Qt.AlignCenter)

        main_card = QFrame()
        main_card.setObjectName("mainCard")
        main_card.setMaximumWidth(1080)
        main_card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 12)
        shadow.setColor(QColor(0, 0, 0, 120))
        main_card.setGraphicsEffect(shadow)

        main_layout = QVBoxLayout(main_card)
        main_layout.setContentsMargins(28, 28, 28, 28)
        main_layout.setSpacing(22)

        # =========================
        # TOP BRAND BAR
        # =========================
        top_bar = QHBoxLayout()
        top_bar.setSpacing(14)

        brand_wrap = QHBoxLayout()
        brand_wrap.setSpacing(12)

        logo_mark = QLabel("✨")
        logo_mark.setObjectName("logoMark")
        logo_mark.setFixedSize(72, 72)
        logo_mark.setAlignment(Qt.AlignCenter)

        brand_text_wrap = QVBoxLayout()
        brand_text_wrap.setSpacing(3)

        eyebrow = QLabel("PREMIUM WEBP CONVERSION WORKSPACE")
        eyebrow.setObjectName("eyebrow")
        eyebrow.setAlignment(Qt.AlignCenter)

        brand_title = QLabel("v1.2")
        brand_title.setObjectName("brandTitle")

        brand_subtitle = QLabel("Fast conversion • Clean interface • Professional workflow")
        brand_subtitle.setObjectName("brandSubtitle")

        brand_text_wrap.addWidget(eyebrow, 0, Qt.AlignLeft)
        brand_text_wrap.addWidget(brand_title)
        brand_text_wrap.addWidget(brand_subtitle)

        brand_wrap.addWidget(logo_mark, 0, Qt.AlignTop)
        brand_wrap.addLayout(brand_text_wrap, 1)

        top_bar.addLayout(brand_wrap, 1)

        # right pills
        pill_wrap = QHBoxLayout()
        pill_wrap.setSpacing(10)
        pill_wrap.addWidget(self._create_pill("🔒 Private & Secure"))
        pill_wrap.addWidget(self._create_pill("🖥️ No Upload, Just Local Processing"))
        pill_wrap.addWidget(self._create_pill("⚡ Super Fast & Easy"))
        top_bar.addLayout(pill_wrap)

        main_layout.addLayout(top_bar)

        # =========================
        # HERO SECTION
        # =========================
        hero_card = QFrame()
        hero_card.setObjectName("heroCard")

        hero_layout = QHBoxLayout(hero_card)
        hero_layout.setContentsMargins(26, 26, 26, 26)
        hero_layout.setSpacing(24)

        # left hero copy
        left_col = QVBoxLayout()
        left_col.setSpacing(16)

        hero_title = QLabel(
            "Convert images into WEBP with speed,\n"
            "clarity, and professional workflow."
        )
        hero_title.setObjectName("heroTitle")

        hero_desc = QLabel(
            "Optimized for desktop workflow, WEBP Converter Pro helps you "
            "convert JPG, JPEG, and PNG assets into efficient WEBP output "
            "through a polished interface built for speed and clarity."
        )
        hero_desc.setWordWrap(True)
        hero_desc.setObjectName("heroDesc")

        cta_row = QHBoxLayout()
        cta_row.setSpacing(14)

        start_button = QPushButton("✦  Start Converting")
        start_button.setObjectName("primaryButton")
        start_button.setCursor(Qt.PointingHandCursor)
        start_button.setMinimumHeight(50)
        start_button.setMinimumWidth(220)
        start_button.clicked.connect(self.start_convert_callback)

        hint = QLabel("No setup needed • Ready for batch workflow")
        hint.setObjectName("subHint")
        hint.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        cta_row.addWidget(start_button, 0, Qt.AlignLeft)
        cta_row.addWidget(hint, 1, Qt.AlignVCenter)

        stats_row = QHBoxLayout()
        stats_row.setSpacing(14)
        stats_row.addWidget(self._create_mini_stat("3", "Supported formats"))
        stats_row.addWidget(self._create_mini_stat("3", "WEBP profiles"))
        stats_row.addWidget(self._create_mini_stat("∞", "Batch-ready workflow"))

        left_col.addWidget(hero_title)
        left_col.addWidget(hero_desc)
        left_col.addLayout(cta_row)
        left_col.addSpacing(4)
        left_col.addLayout(stats_row)

        # right hero visual / info block
        right_col = QVBoxLayout()
        right_col.setSpacing(14)

        quick_title = QLabel("Conversion Overview")
        quick_title.setObjectName("sectionTitle")

        quick_desc = QLabel(
            "A focused workspace designed to keep essential conversion actions "
            "clear, accessible, and visually organized."
        )
        quick_desc.setWordWrap(True)
        quick_desc.setObjectName("sectionDesc")

        visual_block = QFrame()
        visual_block.setObjectName("featureCard")
        visual_layout = QVBoxLayout(visual_block)
        visual_layout.setContentsMargins(18, 18, 18, 18)
        visual_layout.setSpacing(12)

        visual_layout.addWidget(self._create_feature_line("◉", "Input", "JPG, JPEG, PNG image sources"))
        visual_layout.addWidget(self._create_feature_line("◉", "Process", "Compression mode and quality controls"))
        visual_layout.addWidget(self._create_feature_line("◉", "Output", "Optimized WEBP export destination"))
        visual_layout.addWidget(self._create_feature_line("◉", "Monitor", "Status, progress, and performance view"))

        right_col.addWidget(quick_title)
        right_col.addWidget(quick_desc)
        right_col.addWidget(visual_block)
        right_col.addStretch()

        hero_layout.addLayout(left_col, 3)
        hero_layout.addLayout(right_col, 2)

        main_layout.addWidget(hero_card)

        # =========================
        # FEATURES SECTION
        # =========================
        features_header = QVBoxLayout()
        features_header.setSpacing(4)

        section_title = QLabel("Why this workspace feels premium")
        section_title.setObjectName("sectionTitle")

        section_desc = QLabel(
            "The interface is organized into clear, polished sections so users "
            "can focus on conversion tasks without visual clutter."
        )
        section_desc.setObjectName("sectionDesc")
        section_desc.setWordWrap(True)

        features_header.addWidget(section_title)
        features_header.addWidget(section_desc)

        main_layout.addLayout(features_header)

        features_grid = QGridLayout()
        features_grid.setHorizontalSpacing(16)
        features_grid.setVerticalSpacing(16)

        features_grid.addWidget(
            self._create_feature_card(
                "⬆",
                "Streamlined Input",
                "A cleaner starting point for adding files and folders, designed to make image import feel effortless."
            ),
            0, 0
        )

        features_grid.addWidget(
            self._create_feature_card(
                "⚙",
                "Refined Control Panel",
                "Settings are visually grouped with stronger hierarchy so conversion options feel deliberate and professional."
            ),
            0, 1
        )

        features_grid.addWidget(
            self._create_feature_card(
                "⚡",
                "Focused Action Flow",
                "Primary actions are emphasized with stronger contrast, better spacing, and more confident visual cues."
            ),
            0, 2
        )

        main_layout.addLayout(features_grid)

        # =========================
        # FOOTER INFO
        # =========================
        footer_wrap = QFrame()
        footer_wrap.setObjectName("featureCard")

        footer_layout = QHBoxLayout(footer_wrap)
        footer_layout.setContentsMargins(18, 16, 18, 16)
        footer_layout.setSpacing(18)

        footer_left = QVBoxLayout()
        footer_left.setSpacing(4)

        footer_title = QLabel("Supported formats & conversion profiles")
        footer_title.setObjectName("featureTitle")

        footer_text = QLabel(
            "Input support: JPG, JPEG, PNG • Output: WEBP • Profiles: Fast, Standard Quality, Maximum Compression"
        )
        footer_text.setWordWrap(True)
        footer_text.setObjectName("footerText")

        footer_left.addWidget(footer_title)
        footer_left.addWidget(footer_text)

        footer_right = QHBoxLayout()
        footer_right.setSpacing(10)
        footer_right.addWidget(self._create_pill("Lossy"))
        footer_right.addWidget(self._create_pill("Lossless"))
        footer_right.addWidget(self._create_pill("Batch Conversion"))

        footer_layout.addLayout(footer_left, 1)
        footer_layout.addLayout(footer_right)

        main_layout.addWidget(footer_wrap)

        root.addWidget(main_card)

    def _create_pill(self, text):
        label = QLabel(text)
        label.setObjectName("pill")
        label.setAlignment(Qt.AlignCenter)
        return label

    def _create_feature_card(self, icon_text, title_text, desc_text):
        card = QFrame()
        card.setObjectName("featureCard")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(10)

        icon = QLabel(icon_text)
        icon.setObjectName("featureIcon")

        title = QLabel(title_text)
        title.setObjectName("featureTitle")

        desc = QLabel(desc_text)
        desc.setObjectName("featureDesc")
        desc.setWordWrap(True)

        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(desc)
        layout.addStretch()

        return card

    def _create_mini_stat(self, value_text, label_text):
        card = QFrame()
        card.setObjectName("miniStatCard")
        card.setFixedHeight(84)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(4)

        value = QLabel(value_text)
        value.setObjectName("miniStatValue")

        label = QLabel(label_text)
        label.setObjectName("miniStatLabel")

        layout.addWidget(value)
        layout.addWidget(label)

        return card

    def _create_feature_line(self, icon_text, title_text, desc_text):
        row = QFrame()
        row.setStyleSheet("background: transparent; border: none;")

        layout = QHBoxLayout(row)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        icon = QLabel(icon_text)
        icon.setStyleSheet(
            """
            QLabel {
                color: #7EA6FF;
                font-size: 14px;
                font-weight: 700;
                min-width: 18px;
            }
            """
        )
        icon.setAlignment(Qt.AlignTop)

        text_wrap = QVBoxLayout()
        text_wrap.setSpacing(2)

        title = QLabel(title_text)
        title.setStyleSheet(
            """
            QLabel {
                color: #F3F4F6;
                font-size: 13px;
                font-weight: 700;
            }
            """
        )

        desc = QLabel(desc_text)
        desc.setStyleSheet(
            """
            QLabel {
                color: #94A0B2;
                font-size: 12px;
            }
            """
        )
        desc.setWordWrap(True)

        text_wrap.addWidget(title)
        text_wrap.addWidget(desc)

        layout.addWidget(icon)
        layout.addLayout(text_wrap, 1)

        return row