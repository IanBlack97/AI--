from core.module_base import FinancialModule
from .view import MarketView
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class MarketController(FinancialModule):
    @property
    def module_name(self):
        return "market"

    def create_view(self):
        self.view = MarketView()
        return self.view

    def create_toolbar_action(self, parent):
        action = QAction(QIcon("resources/icons/market.png"), "市场数据", parent)
        action.triggered.connect(lambda: parent.content_stack.setCurrentWidget(self.view))
        return action