from .view_base import ViewBase
from pygame.draw import line


class PygameBoard(ViewBase):
    def add_component(self, comp):
        super().add_component(comp)

    def update(self, *args, **kwargs):
        self.surface.fill((255, 255, 255))
        width = self.surface.get_width()
        height = self.surface.get_height()
        for x in range(round(width / 10)):
            line(self.surface, (100, 100, 100), (x * 10, 0), (x * 10, height))
        for y in range(round(height / 10)):
            line(self.surface, (100, 100, 100), (0, y * 10), (width, y * 10))
