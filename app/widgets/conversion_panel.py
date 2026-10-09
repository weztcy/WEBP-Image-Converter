from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)


from PySide6.QtCore import Signal



from app.widgets.settings_panel import (
    SettingsPanel
)


from app.widgets.conversion_info import (
    ConversionInfo
)


from app.widgets.output_panel import (
    OutputPanel
)


from app.widgets.conversion_stats import (
    ConversionStats
)


from app.widgets.performance_monitor import (
    PerformanceMonitor
)





class ConversionPanel(QWidget):


    settings_changed = Signal(dict)



    def __init__(self):

        super().__init__()


        self.init_components()

        self.init_ui()

        self.connect_signals()





    # ==================================
    # COMPONENTS
    # ==================================


    def init_components(self):


        self.settings_panel = SettingsPanel()



        self.conversion_info = ConversionInfo()



        self.output_panel = OutputPanel()



        # NEW

        self.conversion_stats = ConversionStats()



        self.performance_monitor = PerformanceMonitor()





    # ==================================
    # UI
    # ==================================


    def init_ui(self):


        layout = QVBoxLayout()



        layout.addWidget(

            self.settings_panel

        )



        layout.addWidget(

            self.conversion_info

        )



        layout.addWidget(

            self.output_panel

        )



        # STATISTICS

        layout.addWidget(

            self.conversion_stats

        )



        # PERFORMANCE

        layout.addWidget(

            self.performance_monitor

        )



        self.setLayout(

            layout

        )





    # ==================================
    # SIGNALS
    # ==================================


    def connect_signals(self):


        self.settings_panel.settings_changed.connect(

            self.settings_changed.emit

        )





    # ==================================
    # SETTINGS API
    # ==================================


    def get_settings(self):


        return (

            self.settings_panel.get_settings()

        )





    # ==================================
    # OUTPUT API
    # ==================================


    def get_output_folder(self):


        return (

            self.output_panel.get_output_folder()

        )





    # ==================================
    # PERFORMANCE API
    # ==================================


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





    # ==================================
    # STATISTICS API
    # ==================================


    def update_statistics(
            self,
            data
    ):


        self.conversion_stats.update_stats(

            data

        )





    # ==================================
    # RESET
    # ==================================


    def reset(self):


        self.output_panel.reset()



        self.conversion_stats.update_stats({

            "total": 0,

            "success": 0,

            "failed": 0,

            "duration": 0,

            "speed": 0,

            "input_mb": 0,

            "output_mb": 0,

            "saved_percent": 0

        })