from core.module_base import FinancialModule
from .view import DashboardView
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class DashboardController(FinancialModule):
    @property
    def module_name(self):
        return "dashboard"

    def create_view(self):
        self.view = DashboardView()
        return self.view

    def create_toolbar_action(self, parent):
        action = QAction(QIcon("resources/icons/dashboard.png"), "仪表盘", parent)
        action.triggered.connect(lambda: parent.content_stack.setCurrentWidget(self.view))
        return action