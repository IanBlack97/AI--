from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class PortfolioView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("<h2>投资组合分析</h2>"))