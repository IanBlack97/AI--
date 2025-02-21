from core.module_base import FinancialModule
from .view import PortfolioView
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class PortfolioController(FinancialModule):
    @property
    def module_name(self):
        return "portfolio"

    def create_view(self):
        self.view = PortfolioView()
        return self.view

    def create_toolbar_action(self, parent):
        action = QAction(QIcon("resources/icons/portfolio.png"), "投资组合", parent)
        action.triggered.connect(lambda: parent.content_stack.setCurrentWidget(self.view))
        return action