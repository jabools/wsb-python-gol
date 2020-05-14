from .view_base import ViewBase
from models.cell import Cell
from pygame.draw import rect
from pygame.locals import Rect


class PygameCell(ViewBase):
    def __init__(self, name: str, model: Cell, surface):
        super().__init__(name, model, surface)
        self.__rect = Rect(model.x * 10 + 1, model.y * 10 + 1, 9, 9)

    def add_component(self, comp):
        pass

    def update(self, *args, **kwargs):
        if self.model.alive:
            color = (255, 0, 0)
        else:
            color = (255, 255, 255)

        rect(self.surface, color, self.__rect)
