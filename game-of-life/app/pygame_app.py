from .app_base import AppBase
from pygame import init, display, draw, time, event, QUIT, quit, K_SPACE
from views.pygame_board import PygameBoard
from models.population import Population


class PygameApp(AppBase):
    def __init__(self, controller):
        super().__init__(controller)
        self.__screen_color = (255, 255, 255)
        self.__screen_size = (640, 480)
        self.__pyg_clock = time.Clock()
        self.__surface = None

    def run_app(self):
        self.__init_window()

    def __init_window(self):
        init()

        self.__surface = display.set_mode(self.__screen_size)

        model = Population()
        model.set_size(self.__screen_size)
        self.__board_view = PygameBoard('Population', model, self.__surface)
        model.add_observer(self.__board_view)

        self.controller.model = model
        self.controller.view = self.__board_view

        model.reset_population()
        print("Resetting population")

        while True:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    exit()

            self.__surface.fill(self.__screen_color)

            self.controller.handle()

            self.__pyg_clock.tick(40)
            display.flip()
