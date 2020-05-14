from .model_base import ModelBase
from random import randrange
from factories.cell_factory import CellFactory


class Population(ModelBase):
    def __init__(self, cell_factory: CellFactory, size):
        super().__init__()
        self.__evolve = True
        self.__size = size
        self.__cell_factory = cell_factory
        self.__cells = self.__init_cells()
        self.reset_population()

    def modify(self, *args, **kwargs):
        for obs in self._observers.values():
            obs.update()

        if self.__evolve:
            self.__next_generation()

        [[self.__cells[x][y].notify() for y in range(round(self.__size[1] / 10))]
         for x in range(round(self.__size[0] / 10))]

    def notify(self):
        pass

    def reset_population(self):
        [[self.__cells[x][y].modify(False) for y in range(round(self.__size[1] / 10))]
         for x in range(round(self.__size[0] / 10))]

        for x in range(100, 200):
            self.__cells[randrange(0, round(self.__size[0] / 10))][
                randrange(0, round(self.__size[1] / 10))].modify(True)

    def __next_generation(self):
        pass

    def toggle_evolution(self):
        self.__evolve = not self.__evolve

    def __init_cells(self):
        return [[self.__cell_factory.create(x, y) for y in range(round(self.__size[1] / 10))]
                for x in range(round(self.__size[0] / 10))]
