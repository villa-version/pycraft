import pygame


class Display:
    def __init__(self, ss):
        self.width, self.height = ss
        self.screen = pygame.display.set_mode((self.width, self.height))


