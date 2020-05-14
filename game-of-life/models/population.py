from .model_base import ModelBase
from random import randrange, choice
from factories.cell_factory import CellFactory


class Population(ModelBase):
    def __init__(self, cell_factory: CellFactory):
        super().__init__()
        self.__cells = [[]]
        self.__evolve = True
        self.__size = (0, 0)
        self.__cell_factory = cell_factory

    def modify(self, *args, **kwargs):
        for obs in self._observers.values():
            obs.update()

        if self.__evolve:
            self.__next_generation()

    def notify(self):
        pass

    def reset_population(self):
        self.__cells = [[self.__cell_factory.create(x, y) for y in range(round(self.__size[1] / 100))] for x in range(round(self.__size[0] / 100))]

        # generate random 15 to 30 cells
        for x in range(3, 5):
            print(len(self.__cells))
            self.__cells[randrange(0, round(self.__size[0] / 100) - 1)][randrange(0, round(self.__size[1] / 100) - 1)].modify(True)

    def __next_generation(self):
        self.reset_population()

    def toggle_evolution(self):
        self.__evolve = not self.__evolve

    def set_size(self, size):
        self.__size = size
