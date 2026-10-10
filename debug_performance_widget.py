from PySide6.QtWidgets import QApplication

from app.widgets.performance_panel import PerformancePanel

import sys



app = QApplication(sys.argv)



window = PerformancePanel()



window.start_monitor()



window.resize(
    900,
    600
)


window.show()



sys.exit(
    app.exec()
)