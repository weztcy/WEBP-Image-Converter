from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QGridLayout
)

from PySide6.QtCore import Signal


from app.widgets.settings_panel import SettingsPanel
from app.widgets.conversion_info import ConversionInfo
from app.widgets.output_panel import OutputPanel
from app.widgets.conversion_stats import ConversionStats
from app.widgets.performance_monitor import PerformanceMonitor



class ConversionPanel(QWidget):


    settings_changed = Signal(dict)



    def __init__(self):

        super().__init__()


        self.init_components()

        self.init_ui()

        self.connect_signals()



    # ==================================================
    # COMPONENTS
    # ==================================================

    def init_components(self):


        self.settings_panel = SettingsPanel()

        self.conversion_info = ConversionInfo()

        self.output_panel = OutputPanel()

        self.conversion_stats = ConversionStats()

        self.performance_monitor = PerformanceMonitor()



    # ==================================================
    # PREMIUM WELCOME STYLE UI
    # ==================================================

    def init_ui(self):


        self.setStyleSheet(
            """

            QWidget {

                font-family:
                "Inter",
                "Segoe UI";

            }



            QFrame#heroCard {

                background-color:#151922;

                border-radius:28px;

                border:1px solid #273043;

            }



            QFrame#glassCard {

                background-color:#181D27;

                border-radius:22px;

                border:1px solid #2A3346;

            }



            QLabel#heroTitle {

                color:#F9FAFB;

                font-size:30px;

                font-weight:800;

            }



            QLabel#heroSubtitle {

                color:#98A2B3;

                font-size:14px;

            }



            QLabel#cardTitle {

                color:#8BAAFF;

                font-size:12px;

                font-weight:800;

                letter-spacing:1px;

            }



            QLabel#badge {

                color:#D8E1F0;

                background:#20283A;

                border-radius:12px;

                padding:7px 14px;

                font-size:12px;

                font-weight:600;

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


        root.setSpacing(
            20
        )



        # ==================================================
        # HERO HEADER
        # ==================================================

        hero = QFrame()

        hero.setObjectName(
            "heroCard"
        )


        hero_layout = QVBoxLayout(hero)


        hero_layout.setContentsMargins(
            28,
            26,
            28,
            26
        )


        hero_layout.setSpacing(
            12
        )



        title = QLabel(
            "⚡ Conversion Studio"
        )

        title.setObjectName(
            "heroTitle"
        )


        subtitle = QLabel(
            "Configure your image optimization workflow "
            "and prepare high-quality WEBP output."
        )

        subtitle.setObjectName(
            "heroSubtitle"
        )



        badge_row = QHBoxLayout()


        for item in [

            "JPG INPUT",

            "PNG SUPPORT",

            "WEBP OUTPUT",

            "BATCH READY"

        ]:


            badge = QLabel(
                item
            )

            badge.setObjectName(
                "badge"
            )

            badge_row.addWidget(
                badge
            )


        badge_row.addStretch()



        hero_layout.addWidget(
            title
        )


        hero_layout.addWidget(
            subtitle
        )


        hero_layout.addSpacing(
            8
        )


        hero_layout.addLayout(
            badge_row
        )


        root.addWidget(
            hero
        )



        # ==================================================
        # CONTROL AREA
        # ==================================================

        control_grid = QGridLayout()


        control_grid.setSpacing(
            18
        )



        control_grid.addWidget(

            self.create_card(

                "QUALITY & COMPRESSION",

                self.settings_panel

            ),

            0,

            0

        )


        control_grid.addWidget(

            self.create_card(

                "OUTPUT DESTINATION",

                self.output_panel

            ),

            0,

            1

        )



        root.addLayout(
            control_grid
        )



        # ==================================================
        # INFORMATION
        # ==================================================

        root.addWidget(

            self.create_card(

                "CONVERSION KNOWLEDGE",

                self.conversion_info

            )

        )



        # ==================================================
        # MONITOR AREA
        # ==================================================

        monitor = QHBoxLayout()


        monitor.setSpacing(
            18
        )


        monitor.addWidget(

            self.create_card(

                "RESULT SUMMARY",

                self.conversion_stats

            )

        )


        monitor.addWidget(

            self.create_card(

                "SYSTEM PERFORMANCE",

                self.performance_monitor

            )

        )


        root.addLayout(
            monitor
        )



    # ==================================================
    # CARD COMPONENT
    # ==================================================

    def create_card(
            self,
            title,
            widget
    ):


        card = QFrame()


        card.setObjectName(
            "glassCard"
        )


        layout = QVBoxLayout(card)


        layout.setContentsMargins(
            22,
            20,
            22,
            20
        )


        layout.setSpacing(
            14
        )



        label = QLabel(
            title
        )


        label.setObjectName(
            "cardTitle"
        )


        layout.addWidget(
            label
        )


        layout.addWidget(
            widget
        )


        return card



    # ==================================================
    # SIGNAL
    # ==================================================

    def connect_signals(self):


        self.settings_panel.settings_changed.connect(

            self.settings_changed.emit

        )



    # ==================================================
    # API
    # ==================================================

    def get_settings(self):

        return self.settings_panel.get_settings()



    def get_output_folder(self):

        return self.output_panel.get_output_folder()



    def set_profile(
            self,
            profile
    ):


        self.performance_monitor.set_profile(
            profile
        )



    def set_workers(
            self,
            workers
    ):


        self.performance_monitor.set_worker_info(
            workers
        )



    def update_statistics(
            self,
            data
    ):


        self.conversion_stats.update_stats(
            data
        )



    def reset(self):


        self.output_panel.reset()


        self.conversion_stats.update_stats({

            "total":0,

            "success":0,

            "failed":0,

            "duration":0,

            "speed":0,

            "input_mb":0,

            "output_mb":0,

            "saved_percent":0

        })