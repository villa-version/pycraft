from block import Block
import pygame
from settings import settings
from speed import Speed


w, h = settings.BLOCK_SIZE, settings.BLOCK_SIZE
speed = Speed(0, 0)
skin = pygame.image.load('image/block_skins/ground.png')
strength = 0.5
name = 'ground'
constant_friction = 0.6


class Ground(Block):

    def __init__(self, x, y, screen, player):
        Block.__init__(self, x, y, w, h, speed, skin, name, strength, screen, player, constant_friction)

    def update(self):
        Block.update(self)

