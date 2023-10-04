import pygame
from values import *


class Mob:

    is_land = None

    def __init__(self, x, y, w, h, skin, hp, speed, name, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = pygame.transform.scale(skin, (self.w, self.h))
        self.hp = hp
        self.speed = speed
        self.name = name
        self.screen = screen

    def update(self):
        self.draw()
        self.fall()

    def fall(self):
        if not self.is_land:
            self.y -= self.speed[1]
            self.speed[1] = -gravity*cont_time/100000000

    def draw(self):
        self.screen.blit(self.skin, (self.x, self.y))
