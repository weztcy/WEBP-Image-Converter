from app.core.system_monitor import SystemMonitor

from PySide6.QtWidgets import QApplication

import sys



app = QApplication(sys.argv)



monitor = SystemMonitor()



monitor.updated.connect(
    print
)


monitor.start()



sys.exit(
    app.exec()
)