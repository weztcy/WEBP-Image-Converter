"""Centralized Qt stylesheet definitions.

Every widget pulls its QSS from :data:`THEME` instead of
embedding long stylesheet strings."""


MAIN_WINDOW_QSS = """
            QMainWindow {

                background-color: #0F1115;

            }


            QWidget {

                font-family: "Inter", "Segoe UI";

            }


            QFrame#header {

                background-color: #151922;

                border-bottom: 1px solid #242938;

            }


            QFrame#footer {

                background-color: #11141A;

                border-top: 1px solid #242938;

            }


            QLabel#brand {

                color: #F9FAFB;

                font-size: 16px;

                font-weight: 800;

            }


            QLabel#version {

                color: #8F98A8;

                font-size: 12px;

            }


            QLabel#status {

                color: #34D399;

                font-size: 12px;

                font-weight: 600;

            }


            QPushButton#iconButton {

                background-color: transparent;

                border: none;

                color: #9CA3AF;

                font-size: 18px;

                padding: 6px;

            }


            QPushButton#iconButton:hover {

                color: #FFFFFF;

                background-color: #202633;

                border-radius: 8px;

            }

            
"""


HOME_PAGE_QSS = """
            QWidget#homePage {
                background-color: #0F1115;
            }

            QFrame#mainCard {
                background-color: #151922;
                border: 1px solid #242938;
                border-radius: 28px;
            }

            QFrame#heroCard {
                background-color: #171B25;
                border: 1px solid #2A3142;
                border-radius: 24px;
            }

            QFrame#featureCard {
                background-color: #181D27;
                border: 1px solid #2A3040;
                border-radius: 18px;
            }

            QLabel#eyebrow {
                color: #7EA6FF;
                background-color: rgba(79, 140, 255, 0.12);
                border: 1px solid rgba(79, 140, 255, 0.28);
                border-radius: 14px;
                padding: 6px 12px;
                font-size: 11px;
                font-weight: 700;
                letter-spacing: 1px;
            }

            QLabel#logoMark {
                background-color: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #5B8CFF,
                    stop: 1 #7A5CFF
                );
                color: white;
                border-radius: 36px;
                font-size: 28px;
                font-weight: 800;
            }

            QLabel#brandTitle {
                color: #F9FAFB;
                font-size: 16px;
                font-weight: 700;
            }

            QLabel#brandSubtitle {
                color: #8D97AA;
                font-size: 12px;
                font-weight: 500;
            }

            QLabel#heroTitle {
                color: #F9FAFB;
                font-size: 34px;
                font-weight: 800;
                line-height: 1.2;
            }

            QLabel#heroDesc {
                color: #A7B0C0;
                font-size: 15px;
                line-height: 1.5;
            }

            QPushButton#primaryButton {
                background-color: #4F8CFF;
                color: white;
                border: none;
                border-radius: 14px;
                padding: 14px 24px;
                font-size: 15px;
                font-weight: 700;
            }

            QPushButton#primaryButton:hover {
                background-color: #669BFF;
            }

            QPushButton#primaryButton:pressed {
                background-color: #3C78E8;
            }

            QLabel#subHint {
                color: #7F8898;
                font-size: 12px;
                font-weight: 500;
            }

            QLabel#pill {
                color: #D8E1F0;
                background-color: #1D2330;
                border: 1px solid #30384A;
                border-radius: 12px;
                padding: 8px 14px;
                font-size: 12px;
                font-weight: 600;
            }

            QLabel#sectionTitle {
                color: #F3F4F6;
                font-size: 18px;
                font-weight: 700;
            }

            QLabel#sectionDesc {
                color: #9DA7B8;
                font-size: 13px;
            }

            QLabel#featureIcon {
                color: #8BB0FF;
                font-size: 20px;
                font-weight: 700;
            }

            QLabel#featureTitle {
                color: #F9FAFB;
                font-size: 15px;
                font-weight: 700;
            }

            QLabel#featureDesc {
                color: #9CA3AF;
                font-size: 13px;
                line-height: 1.45;
            }

            QLabel#miniStatValue {
                color: #F9FAFB;
                font-size: 18px;
                font-weight: 800;
            }

            QLabel#miniStatLabel {
                color: #8F98A8;
                font-size: 12px;
                font-weight: 500;
            }

            QFrame#miniStatCard {
                background-color: #131823;
                border: 1px solid #2A3142;
                border-radius: 16px;
            }

            QLabel#footerText {
                color: #7C8596;
                font-size: 12px;
                font-weight: 500;
            }
            
"""


CONVERT_PAGE_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }


            QWidget#convertPage {

                background-color:#0F1115;

            }


            QLabel#pageTitle {

                color:#F9FAFB;

                font-size:28px;

                font-weight:800;

            }


            QLabel#pageSubtitle {

                color:#98A2B3;

                font-size:14px;

            }


            QLabel#sectionTitle {

                color:#7EA6FF;

                font-size:13px;

                font-weight:800;

            }



            QLabel#step {

                color:#7EA6FF;

                background-color:#172033;

                border-radius:12px;

                padding:8px 14px;

                font-size:12px;

                font-weight:700;

            }

            
"""


ACTION_SECTION_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#actionCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:22px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:16px;

                font-weight:800;

            }



            QLabel#desc {

                color:#98A2B3;

                font-size:12px;

            }



            QPushButton {

                height:48px;

                border-radius:14px;

                font-size:14px;

                font-weight:700;

            }



            QPushButton#primary {

                background:#4F8CFF;

                color:white;

                border:none;

            }



            QPushButton#primary:hover {

                background:#669BFF;

            }



            QPushButton#secondary {

                background:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

            }



            QPushButton#secondary:hover {

                background:#273147;

                border-color:#4F8CFF;

            }



            QPushButton#cancel {

                background:#2B1820;

                color:#FCA5A5;

                border:1px solid #7F1D1D;

            }



            QPushButton#cancel:hover {

                background:#401C26;

            }

            
"""


CONVERSION_INFO_QSS = """

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


CONVERSION_SECTION_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#controlCard {

                background-color:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }



            QLabel#sectionLabel {

                color:#7EA6FF;

                font-size:12px;

                font-weight:700;

                letter-spacing:1px;

            }

            
"""


CONVERSION_STATS_QSS = """

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


DROP_SECTION_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#card {

                background-color:#151922;

                border:1px solid #242B3A;

                border-radius:24px;

            }



            QFrame#dropZone {

                background-color:#10141C;

                border:2px dashed #354156;

                border-radius:22px;

            }



            QFrame#dropZone:hover {

                border-color:#4F8CFF;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }



            QLabel#uploadIcon {

                background-color:#1D2940;

                color:#7EA6FF;

                border-radius:32px;

                font-size:28px;

                font-weight:700;

            }



            QLabel#dropText {

                color:#F3F4F6;

                font-size:16px;

                font-weight:700;

            }



            QLabel#hint {

                color:#7F8898;

                font-size:12px;

            }



            QLabel#badge {

                background-color:#1D2330;

                border:1px solid #30384A;

                border-radius:10px;

                color:#DCE6FF;

                padding:6px 10px;

                font-size:11px;

                font-weight:600;

            }



            QPushButton {

                background-color:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

                border-radius:14px;

                text-align:left;

                padding:14px 16px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background-color:#242E42;

                border-color:#4F8CFF;

            }



            QPushButton:pressed {

                background-color:#151B27;

            }

            
"""


IMAGE_LIST_QSS = """

            QListWidget {

                background:transparent;

                border:none;

                outline:none;

            }


            QListWidget::item {

                background:#151922;

                border:1px solid #242938;

                border-radius:16px;

                padding:10px;

                margin:4px;

            }



            QListWidget::item:hover {

                border-color:#4F8CFF;

                background:#192131;

            }



            QListWidget::item:selected {

                background:#17243A;

                border:1px solid #4F8CFF;

            }

            
"""


IMAGE_CARD_QSS = """

            QFrame {

                background:transparent;

            }



            QLabel#name {

                color:#F9FAFB;

                font-size:12px;

                font-weight:700;

            }



            QLabel#meta {

                color:#98A2B3;

                font-size:11px;

            }



            QLabel#badge {

                background:#1D2940;

                color:#8BB0FF;

                padding:3px 8px;

                border-radius:8px;

                font-size:10px;

                font-weight:700;

            }

            
"""


IMAGE_PREVIEW_QSS = """

            QLabel {

                background:#10141C;

                border:1px solid #242938;

                border-radius:18px;

                color:#667085;

                font-size:14px;

                font-weight:600;

            }

            
"""


IMAGE_SECTION_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }


            QFrame#libraryCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }



            QFrame#innerPanel {

                background:#10141C;

                border:1px solid #202735;

                border-radius:18px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:18px;

                font-weight:800;

            }



            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }



            QLabel#counter {

                background:#1D2940;

                color:#8BB0FF;

                padding:7px 14px;

                border-radius:12px;

                font-size:12px;

                font-weight:700;

            }



            QPushButton {

                background:#1B2230;

                color:#E5E7EB;

                border:1px solid #30384A;

                border-radius:12px;

                padding:10px 18px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background:#273147;

                border-color:#4F8CFF;

            }



            QPushButton#danger:hover {

                border-color:#EF4444;

                color:#FCA5A5;

            }

            
"""


OUTPUT_PANEL_QSS = """

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



            QLabel#path {

                background:#181F2D;

                border:1px solid #30384A;

                border-radius:12px;

                color:#DCE6FF;

                padding:12px;

                font-size:12px;

            }



            QLabel#caption {

                color:#7F8898;

                font-size:11px;

                font-weight:600;

            }



            QRadioButton {

                color:#D1D5DB;

                font-size:13px;

                font-weight:600;

                spacing:10px;

            }



            QRadioButton::indicator {

                width:16px;

                height:16px;

                border-radius:8px;

                border:2px solid #4B5563;

            }



            QRadioButton::indicator:checked {

                background:#4F8CFF;

                border-color:#4F8CFF;

            }



            QPushButton {

                background:#1B2230;

                border:1px solid #30384A;

                border-radius:12px;

                color:#E5E7EB;

                padding:12px 18px;

                font-size:13px;

                font-weight:700;

            }



            QPushButton:hover {

                background:#273147;

                border-color:#4F8CFF;

            }


            
"""


PERFORMANCE_PANEL_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#card {


                background:#10141C;

                border:1px solid #242938;

                border-radius:22px;

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



            QLabel#value {


                color:#F9FAFB;

                font-size:20px;

                font-weight:900;

            }



            QLabel#label {


                color:#98A2B3;

                font-size:12px;

                font-weight:700;

            }



            QProgressBar {


                background:#202633;

                border-radius:5px;

                height:8px;

                text-align:center;

            }



            QProgressBar::chunk {


                background:#4F8CFF;

                border-radius:5px;

            }


            
"""


PROCESS_SECTION_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }


            QFrame#monitorCard {

                background:#151922;

                border:1px solid #242938;

                border-radius:24px;

            }


            QFrame#innerCard {

                background:#10141C;

                border-radius:18px;

            }


            QLabel#title {

                color:#F9FAFB;

                font-size:17px;

                font-weight:800;

            }


            QLabel#subtitle {

                color:#98A2B3;

                font-size:13px;

            }


            QLabel#sectionLabel {

                color:#7EA6FF;

                font-size:11px;

                font-weight:700;

                letter-spacing:1px;

            }

            
"""


PROCESS_STATUS_QSS = """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#card {

                background:#151922;

                border:1px solid #242938;

                border-radius:20px;

            }



            QLabel#title {

                color:#F9FAFB;

                font-size:16px;

                font-weight:800;

            }



            QLabel#status {

                color:#34D399;

                font-size:13px;

                font-weight:700;

            }



            QLabel#label {

                color:#98A2B3;

                font-size:12px;

            }



            QLabel#value {

                color:#E5E7EB;

                font-size:13px;

                font-weight:600;

            }



            QProgressBar {

                background:#0F141D;

                border:1px solid #283247;

                border-radius:8px;

                height:14px;

                text-align:center;

                color:#E5E7EB;

                font-size:11px;

            }



            QProgressBar::chunk {

                background:#4F8CFF;

                border-radius:7px;

            }



            QPushButton {

                background:#202A3D;

                color:#DCE6FF;

                border:1px solid #34425C;

                border-radius:12px;

                padding:10px 18px;

                font-weight:700;

            }



            QPushButton:hover {

                background:#293650;

                border-color:#4F8CFF;

            }



            QPushButton:disabled {

                color:#667085;

                background:#171B24;

            }



            QFrame#successBox {

                background:#10251D;

                border:1px solid #1F9D68;

                border-radius:12px;

            }



            QFrame#failedBox {

                background:#251518;

                border:1px solid #9D3B42;

                border-radius:12px;

            }

            
"""


RESOURCE_CHART_QSS = """

            QFrame#chartCard {

                background:#10141C;

                border:1px solid #242938;

                border-radius:18px;

            }


            QLabel#title {

                color:#F9FAFB;

                font-size:13px;

                font-weight:800;

            }


            QLabel#value {

                color:#F9FAFB;

                font-size:24px;

                font-weight:900;

            }

            
"""


SETTINGS_PANEL_QSS = """

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




THEME = {
    "main_window": MAIN_WINDOW_QSS,
    "home_page": HOME_PAGE_QSS,
    "convert_page": CONVERT_PAGE_QSS,
    "action_section": ACTION_SECTION_QSS,
    "conversion_info": CONVERSION_INFO_QSS,
    "conversion_section": CONVERSION_SECTION_QSS,
    "conversion_stats": CONVERSION_STATS_QSS,
    "drop_section": DROP_SECTION_QSS,
    "image_list": IMAGE_LIST_QSS,
    "image_card": IMAGE_CARD_QSS,
    "image_preview": IMAGE_PREVIEW_QSS,
    "image_section": IMAGE_SECTION_QSS,
    "output_panel": OUTPUT_PANEL_QSS,
    "performance_panel": PERFORMANCE_PANEL_QSS,
    "process_section": PROCESS_SECTION_QSS,
    "process_status": PROCESS_STATUS_QSS,
    "resource_chart": RESOURCE_CHART_QSS,
    "settings_panel": SETTINGS_PANEL_QSS,
}


def apply_style(widget, key):
    """Apply a named stylesheet to a widget."""
    widget.setStyleSheet(THEME[key])
