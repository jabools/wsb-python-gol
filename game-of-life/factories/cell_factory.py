from abc import ABC, abstractmethod
from models.cell import Cell


class CellFactory(ABC):
    @abstractmethod
    def create(self, x, y):
        return Cell(x, y)
