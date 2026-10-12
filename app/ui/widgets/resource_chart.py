from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame
)

import pyqtgraph as pg


from app.styles.colors import COLORS


from app.styles.theme import THEME

class ResourceChart(QWidget):


    def __init__(
            self,
            title,
            unit="%"
    ):

        super().__init__()


        self.values = []


        self.max_points = 60


        self.init_ui(
            title
        )



    # ==================================
    # UI
    # ==================================

    def init_ui(
            self,
            title
    ):


        self.setStyleSheet(
            THEME["resource_chart"]
        )



        root = QVBoxLayout(
            self
        )


        root.setContentsMargins(
            0,
            0,
            0,
            0
        )


        card = QFrame()


        card.setObjectName(
            "chartCard"
        )


        layout = QVBoxLayout(
            card
        )


        layout.setContentsMargins(
            16,
            14,
            16,
            14
        )


        layout.setSpacing(
            8
        )



        header = QWidget()


        header_layout = QVBoxLayout(
            header
        )


        header_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )



        self.title_label = QLabel(
            title
        )


        self.title_label.setObjectName(
            "title"
        )


        self.value_label = QLabel(
            "0%"
        )


        self.value_label.setObjectName(
            "value"
        )



        header_layout.addWidget(
            self.title_label
        )


        header_layout.addWidget(
            self.value_label
        )



        layout.addWidget(
            header
        )



        # ==========================
        # GRAPH
        # ==========================


        self.chart = pg.PlotWidget()


        self.chart.setBackground(
            COLORS["panel_inner"]
        )


        self.chart.showAxis(
            "left",
            False
        )


        self.chart.showAxis(
            "bottom",
            False
        )


        self.chart.setYRange(
            0,
            100
        )


        self.chart.setMouseEnabled(
            False,
            False
        )


        self.chart.hideButtons()



        self.line = self.chart.plot(
            [],
            pen=pg.mkPen(
                COLORS["accent"],
                width=2
            )
        )



        layout.addWidget(
            self.chart
        )



        root.addWidget(
            card
        )



    # ==================================
    # UPDATE
    # ==================================

    def update_value(
            self,
            value
    ):


        value = float(value)


        self.value_label.setText(
            f"{value:.0f}%"
        )


        self.values.append(
            value
        )


        if len(self.values) > self.max_points:

            self.values.pop(0)



        self.line.setData(
            self.values
        )