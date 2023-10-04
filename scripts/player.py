from mob import Mob
from values import *


class Player(Mob):

    def __init__(self, x, y, w, h, skin, speed, strength, name, screen):
        Mob.__init__(self, x, y, w, h, skin, speed, strength, name, screen)

    def update(self):
        Mob.update(self)
        self.move()

    def move(self):
        global cont_time
        for key in pressed_keys:
            if key == 'a':
                self.x -= self.speed[0]
            if key == 'd':
                self.x += self.speed[0]
            if key == ' ':
                cont_time = 50000
                self.speed[1] = 0.6


