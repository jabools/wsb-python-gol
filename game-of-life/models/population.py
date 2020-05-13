from .model_base import ModelBase
from .cell import Cell
from random import randrange, choice
from views.pygame_cell import PygameCell
from pygame import display


class Population(ModelBase):
    def __init__(self):
        super().__init__()
        self.__cells = [[]]
        self.__evolve = True
        self.__size = (0, 0)

    def modify(self, *args, **kwargs):
        for obs in self._observers.values():
            obs.update()

        if self.__evolve:
            self.__next_generation()

        [[y.modify(choice([False, True])) for y in x] for x in self.__cells]

    def notify(self):
        pass

    def reset_population(self):
        self.__cells = [[self.__create_cell(x, y) for y in range(self.__size[1])] for x in range(self.__size[0])]

        # generate random 15 to 30 cells
        for x in range(15, 30):
            self.__cells[randrange(0, self.__size[0])][randrange(0, self.__size[1])].modify(True)

    def __next_generation(self):
        pass

    def toggle_evolution(self):
        self.__evolve = not self.__evolve

    def set_size(self, size):
        self.__size = size

    def __create_cell(self, x, y):
        cell = Cell(x, y)
        cell_view = PygameCell('CellRect', cell, display.get_surface())
        cell.add_observer(cell_view)

        return cell
