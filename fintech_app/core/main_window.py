import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QStackedWidget, QToolBar,
                             QHBoxLayout, QVBoxLayout)  # 添加布局类导入
from PyQt5.QtCore import Qt
from .module_base import FinancialModule
from utils.module_loader import ModuleLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("金融分析平台")
        self.setGeometry(200, 200, 1200, 800)
        self.modules = {}
        self.init_ui()
        self.load_modules()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)  # 现在这个类已正确导入

        # 侧边导航
        self.sidebar = QToolBar("导航栏", self)
        self.sidebar.setOrientation(Qt.Vertical)
        self.addToolBar(Qt.LeftToolBarArea, self.sidebar)

        # 主内容区
        self.content_stack = QStackedWidget()
        main_layout.addWidget(self.content_stack)

    def load_modules(self):
        loader = ModuleLoader("modules", FinancialModule)
        for module_name in loader.discover_modules():
            module = loader.load_module(module_name)
            if module:
                self.register_module(module)

    def register_module(self, module):
        self.modules[module.module_name] = module
        self.content_stack.addWidget(module.create_view())
        self.sidebar.addAction(module.create_toolbar_action(self))