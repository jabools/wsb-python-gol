from .model_base import ModelBase
from random import randrange, choice
from factories.cell_factory import CellFactory


class Population(ModelBase):
    def __init__(self, cell_factory: CellFactory, size):
        super().__init__()
        self.__evolve = True
        self.__size = size
        self.__width = round(self.__size[0] / 10)
        self.__height = round(self.__size[1] / 10)
        self.__cell_factory = cell_factory
        self.__cells = self.__init_cells()
        self.reset_population()

    def modify(self, *args, **kwargs):
        for obs in self._observers.values():
            obs.update()

        if self.__evolve:
            self.__next_generation()

        [[self.__cells[x][y].notify() for y in range(self.__height)]
         for x in range(self.__width)]

    def notify(self):
        pass

    def reset_population(self):
        [[self.__cells[x][y].modify(choice([True, False, False, False])) for y in range(self.__height)]
         for x in range(self.__width)]

    def toggle_evolution(self):
        self.__evolve = not self.__evolve

    def __init_cells(self):
        return [[self.__cell_factory.create(x, y) for y in range(self.__height)]
                for x in range(self.__width)]

    def __next_generation(self):
        next_generation = self.__init_cells()

        for x in range(len(self.__cells)):
            column = self.__cells[x]

            for y in range(len(column)):
                count = sum(self.__neighbours(x, y))

                if count == 3:
                    next_generation[x][y].modify(True)
                elif count == 2:
                    next_generation[x][y].modify(column[y].alive)
                else:
                    next_generation[x][y].modify(False)

        self.__cells = next_generation

    def __neighbours(self, x, y):
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if nx == x and ny == y:
                    continue

                if nx >= self.__width:
                    nx = 0
                elif nx < 0:
                    nx = self.__width - 1
                if ny >= self.__height:
                    ny = 0
                elif ny < 0:
                    ny = self.__height - 1

                yield int(self.__cells[nx][ny].alive)
