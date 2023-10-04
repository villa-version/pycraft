import pygame
from values import *


class Block:

    detected = False
    mob = None

    def __init__(self, x, y, w, h, skin, speed, strength, name, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = pygame.transform.scale(skin, (self.w, self.h))
        self.speed = speed
        self.strength = strength
        self.given_strength = strength
        self.name = name
        self.screen = screen

    def update(self):
        self.draw()
        self.detect()
        self.breaking()
        self.remove()
        self.collision()

    def draw(self):
        self.screen.blit(self.skin, (self.x, self.y))

    def detect(self):
        mx, my = pygame.mouse.get_pos()
        if self.x < mx < self.x + self.w and self.y < my < self.y + self.h:
            self.detected = True
        else:
            self.detected = False

    def breaking(self):
        if button_down and self.detected:
            self.strength -= 0.5
        else:
            self.strength = self.given_strength

    def remove(self):
        if self.strength == 0:
            return True

    def get_mob(self, mob):
        self.mob = mob

    def check_stay_in_place_y(self):
        if self.y <= self.mob.y <= self.y + self.h:
            return True
        elif self.y <= self.mob.y + self.mob.h <= self.y + self.h:
            return True

    def check_stay_in_place_x(self):
        if self.x <= self.mob.x <= self.x + self.w:
            return True
        elif self.x <= self.mob.x + self.mob.w <= self.x + self.w:
            return True

    def collision(self):
        global cont_time
        dx, dy = self.x - self.mob.x, self.y - self.mob.y
        d_up_side = abs(self.mob.speed[1]) >= self.y - self.mob.y - self.mob.h
        d_down_side = abs(self.mob.speed[1]) >= self.mob.y - self.y - self.h

        if self.check_stay_in_place_x():
            if d_up_side:
                self.mob.speed[1], cont_time = 0, 0
                self.mob.is_land = True
                self.mob.y = self.y - self.mob.h - 1
            else:
                self.mob.is_land = False
            if d_down_side:
                self.mob.speed[1], cont_time = 0, 0
                self.mob.y = self.y + self.h + 1
            else:
                self.mob.is_land = False

