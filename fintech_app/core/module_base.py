from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget, QAction

class FinancialModule(ABC):
    @property
    @abstractmethod
    def module_name(self) -> str:
        pass

    @abstractmethod
    def create_view(self) -> QWidget:
        pass

    @abstractmethod
    def create_toolbar_action(self, parent) -> QAction:
        pass