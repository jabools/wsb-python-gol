from .app_base import AppBase
from pygame import init, display, draw, time, event, QUIT, quit, K_SPACE
from views.pygame_board import PygameBoard
from models.population import Population
from factories.pygame_cell_factory import PygameCellFactory
from pygame import event, K_SPACE, K_r, KEYDOWN


class PygameApp(AppBase):
    def __init__(self, controller):
        super().__init__(controller)
        self.__screen_size = (500, 500)
        self.__pyg_clock = time.Clock()
        self.__surface = None

    def run_app(self):
        self.__init_window()

    def __init_window(self):
        init()

        self.__surface = display.set_mode(self.__screen_size)

        model = Population(PygameCellFactory(), self.__screen_size)
        self.__board_view = PygameBoard('Population', model, self.__surface)
        model.add_observer(self.__board_view)

        self.controller.model = model
        self.controller.view = self.__board_view

        while True:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    exit()

                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        model.toggle_evolution()
                    if e.key == K_r:
                        model.reset_population()

            self.controller.handle()

            self.__pyg_clock.tick(40)
            display.flip()
