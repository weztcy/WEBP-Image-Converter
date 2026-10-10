from PySide6.QtWidgets import QApplication

from app.widgets.resource_chart import ResourceChart

from app.core.system_monitor import SystemMonitor

import sys



app = QApplication(sys.argv)



window = ResourceChart(
    "CPU Usage"
)


monitor = SystemMonitor()



monitor.updated.connect(
    lambda data:
    window.update_value(
        data["cpu"]
    )
)



monitor.start()



window.resize(
    500,
    300
)


window.show()



sys.exit(
    app.exec()
)