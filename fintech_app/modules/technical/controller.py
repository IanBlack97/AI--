from core.module_base import FinancialModule
from .view import TechnicalView
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class TechnicalController(FinancialModule):
    @property
    def module_name(self):
        return "technical"

    def create_view(self):
        return TechnicalView()

    def create_toolbar_action(self, parent):
        action = QAction(QIcon("resources/icons/analysis.png"), "技术分析", parent)
        action.triggered.connect(lambda: parent.content_stack.setCurrentIndex(len(parent.modules)))
        return action