from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class MarketView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("<h2>实时市场数据</h2>"))