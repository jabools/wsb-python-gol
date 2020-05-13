from controllers.pygame_board_controller import PygameBoardController
from app.pygame_app import PygameApp


def main():
    controller = PygameBoardController()
    app = PygameApp(controller)
    app.run_app()


if '__main__' == __name__:
    main()
