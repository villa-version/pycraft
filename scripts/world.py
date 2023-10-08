import pygame
from settings import settings
from cobblestone import *
from ground import *
from wood import *
from coal import *
from diamond import *
from numpy import empty as matrix


BLOCK_SIZE = settings.BLOCK_SIZE


class World:

    blocks = matrix((settings.MAX_BLOCKS_X, settings.MAX_BLOCKS_Y))
    print(blocks)

    def __init__(self, display, player):
        self.display = display
        self.player = player

        self.spawn_blocks()

    def spawn_blocks(self):
        for y in range(1):  # self.display.height//(2*BLOCK_SIZE)
            for x in range(self.display.width // BLOCK_SIZE):
                if y < 3:
                    self.spawn_ground_block(x, self.display.height // (2*BLOCK_SIZE) + y)
                else:
                    self.spawn_diamond_block(x, self.display.height // (2*BLOCK_SIZE) + y)

    def update(self):
        for block in self.blocks:
            block.update()
        self.remove_blocks()

    def remove_blocks(self):
        for block in self.blocks[:]:
            if block.given_strength <= 0:
                self.blocks.remove(block)

    def spawn_ground_block(self, x, y):
        self.blocks.append(Ground(BLOCK_SIZE * x, BLOCK_SIZE * y, self.display.screen, self.player))

    def spawn_wood_block(self, x, y):
        self.blocks.append(Wood(BLOCK_SIZE * x, BLOCK_SIZE * y, self.display.screen, self.player))

    def spawn_cobblestone_block(self, x, y):
        self.blocks.append(Cobblestone(BLOCK_SIZE * x, BLOCK_SIZE * y, self.display.screen, self.player))

    def spawn_coal_block(self, x, y):
        self.blocks.append(Coal(BLOCK_SIZE * x, BLOCK_SIZE * y, self.display.screen, self.player))

    def spawn_diamond_block(self, x, y):
        self.blocks.append(Diamond(BLOCK_SIZE * x, BLOCK_SIZE * y, self.display.screen, self.player))
