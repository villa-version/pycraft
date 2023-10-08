import pygame
from settings import settings
from controller import controller
from timer import timer


class Block:

    detected = False

    def __init__(self, x, y, w, h, speed, skin, name, strength, screen, player, con_friction):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = pygame.transform.scale(skin, (self.w, self.h))
        self.speed = speed
        self.name = name
        self.strength = strength
        self.given_strength = self.strength
        self.screen = screen
        self.player = player
        self.constant_friction = con_friction

    def update(self):
        self.rub()
        self.draw()
        self.detect()
        self.break_process()
        self.collision()

    def break_process(self):
        if controller.button_down and self.detected:
            self.breaking()
        else:
            self.restoration()

    def rub(self):
        if self.player.speed.x > 0:
            self.player.speed.x -= self.constant_friction
        else:
            self.player.speed.x += self.constant_friction

    def draw(self):
        self.screen.blit(self.skin, (self.x, self.y))

    def detect(self):
        if self.x < controller.mouse.x < self.x + self.w and self.y < controller.mouse.y < self.y + self.h:
            self.detected = True
        else:
            self.detected = False

    def breaking(self):
        self.given_strength -= 0.0005

    def restoration(self):
        self.given_strength = self.strength

    def check_stay_in_place_y(self):
        if self.player.y < self.y < self.player.y + self.player.h:
            return True

    def check_stay_in_place_x(self):
        if self.x < self.player.x <= self.x + self.w:
            return True
        elif self.x < self.player.x + self.player.w <= self.x + self.w:
            return True

    def collision(self):
        d_up_side = self.y + abs(self.player.speed.y) + 1 > self.player.y + self.player.h + abs(self.player.speed.y) >= self.y
        d_right_side = self.x + self.w + abs(self.player.speed.x) - 1 < self.player.x - abs(self.player.speed.x) <= self.x + self.w
        d_left_side = self.x + abs(self.player.speed.x) + 1 > self.player.x + self.player.w + abs(self.player.speed.x) >= self.x
        d_down_side = self.y + self.h - abs(self.player.speed.y) - 1 < self.player.y - abs(self.player.speed.y) <= self.y + self.h

        if self.check_stay_in_place_x():
            if d_up_side and self.player.speed.y < 0:
                timer.update_start_time()
                self.player.speed.y = 0
                self.player.y = self.y - self.player.h
            elif d_down_side and self.player.speed.y > 0:
                timer.update_start_time()
                self.player.speed.y = 0
                self.player.y = self.y + self.h
        if self.check_stay_in_place_y():
            if d_right_side and self.player.speed.x < 0:
                self.player.speed.x = 0
                self.player.x = self.x + self.w
            elif d_left_side and self.player.speed.x > 0:
                self.player.speed.x = 0
                self.player.x = self.x - self.player.w

