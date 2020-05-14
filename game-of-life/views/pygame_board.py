from .view_base import ViewBase
from pygame.draw import line


class PygameBoard(ViewBase):
    def add_component(self, comp):
        super().add_component(comp)

    def update(self, *args, **kwargs):
        width = self.surface.get_width()
        height = self.surface.get_height()
        for x in range(round(width / 100)):
            line(self.surface, (100, 100, 100), (x * 100, 0), (x * 100, height))
        for y in range(round(height / 100)):
            line(self.surface, (100, 100, 100), (0, y * 100), (width, y * 100))
