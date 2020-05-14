from .cell_factory import CellFactory
from views.pygame_cell import PygameCell
from pygame import display


class PygameCellFactory(CellFactory):
    def create(self, x, y):
        cell = super().create(x, y)
        cell_view = PygameCell('CellRect', cell, display.get_surface())
        cell.add_observer(cell_view)

        return cell
