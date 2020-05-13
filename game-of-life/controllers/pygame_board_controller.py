from pygame import event, K_SPACE

from .controller_base import ControllerBase


class PygameBoardController(ControllerBase):
    def handle(self):
        for e in event.get():
            if e.type == K_SPACE:
                self.__toggle_evolution()

        self.model.modify()

    def __toggle_evolution(self):
        self.model.toggle_evolution()
