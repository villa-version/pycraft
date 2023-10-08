import pygame

pygame.init()


class Mouse:

    x, y = 0, 0

    def update(self):
        self.x, self.y = pygame.mouse.get_pos()


class Controller:

    button_down = None
    pressed_keys = []
    mouse = Mouse()


controller = Controller()

