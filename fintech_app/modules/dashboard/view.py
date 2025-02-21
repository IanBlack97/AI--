from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("<h1>欢迎使用金融分析平台</h1>"))