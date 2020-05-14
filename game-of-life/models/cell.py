from .model_base import ModelBase


class Cell(ModelBase):
    def __init__(self, x, y):
        super().__init__()
        self.__alive = False
        self.__x = x
        self.__y = y

    def modify(self, *args, **kwargs):
        self.__alive = bool(args[0])
        self.notify()

    def notify(self):
        for obs in self._observers.values():
            obs.update(self.__alive)

    @property
    def alive(self):
        return self.__alive

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
