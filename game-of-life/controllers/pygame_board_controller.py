from pygame import event, K_SPACE, K_r, KEYDOWN

from .controller_base import ControllerBase


class PygameBoardController(ControllerBase):
    def handle(self):
        self.model.modify()
