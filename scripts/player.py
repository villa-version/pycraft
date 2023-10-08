import pygame
from settings import settings
from controller import controller
from timer import timer
from inventory import Inventory


BLOCK_SIZE = settings.BLOCK_SIZE


class Player:

    def __init__(self, x, y, w, h, skin, hp, speed, name, display):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = pygame.transform.scale(skin, (self.w, self.h))
        self.hp = hp
        self.speed = speed
        self.name = name
        self.display = display

        self.inventory = Inventory(self.display.width // 2 - BLOCK_SIZE * 4.5, 0,
                                   BLOCK_SIZE * 9, BLOCK_SIZE, self.display.screen)

    def update(self):
        self.draw()
        self.move()
        # self.inventory.update()

    def draw(self):
        self.display.screen.blit(self.skin, (self.x, self.y))

    def move(self):
        self.move_control()
        self.walk()

    def walk(self):
        self.x += self.speed.x

    def move_control(self):
        if self.speed.x:
            self.speed.x = 0
        for key in controller.pressed_keys:
            if key == 'a':
                self.speed.x = -0.25
            elif key == 'd':
                self.speed.x = 0.25
            if key == ' ':
                timer.update_start_time()
                self.speed.y = 0.6

