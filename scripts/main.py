import pygame
from datetime import datetime
from values import *
from display import *
from player import *
from inventory import *
from block import *
from cobblestone import *
from ground import *
from wood import *
from coal import *
from diamond import *
from mob import *


def calculate_delta_time():
    global last_time, cont_time
    if abs(curr_time - last_time) >= 0.5:
        last_time = curr_time
        cont_time += last_time


class App:
    blocks = []

    def __init__(self, screen_size):
        self.display = Display(screen_size)
        self.player = Player(self.display.width // 2, self.display.height // 2 - BLOCK_SIZE * 3,
                             d_mobs['player']['size'][0], d_mobs['player']['size'][1],
                             d_mobs['player']['skin'], d_mobs['player']['hp'], d_mobs['player']['speed'],
                             'player', self.display.screen)
        self.inventory = Inventory(self.display.width // 2 - BLOCK_SIZE * 4.5, 0, BLOCK_SIZE * 9, BLOCK_SIZE,
                                   self.display.screen)
        self.spawn_world()

    def spawn_world(self):
        for y in range(1):  # self.display.height//(2*BLOCK_SIZE)
            for x in range(self.display.width // BLOCK_SIZE):
                if x < 3:
                    self.spawn_ground_block(BLOCK_SIZE * x, self.display.height // 2 + BLOCK_SIZE * y)
                else:
                    self.spawn_diamond_block(BLOCK_SIZE * x, self.display.height // 2 + BLOCK_SIZE * y)

    def spawn_ground_block(self, x, y):
        self.blocks.append(Ground(x, y, BLOCK_SIZE, BLOCK_SIZE, d_blocks['ground']['skin'], [0, 0], d_blocks['ground']['strength'], 'ground', self.display.screen))

    def spawn_wood_block(self, x, y):
        self.blocks.append(Wood(x, y, BLOCK_SIZE, BLOCK_SIZE, d_blocks['wood']['skin'], [0, 0], d_blocks['wood']['strength'], 'wood', self.display.screen))

    def spawn_cobblestone_block(self, x, y):
        self.blocks.append(Cobblestone(x, y, BLOCK_SIZE, BLOCK_SIZE, d_blocks['cobblestone']['skin'], [0, 0], d_blocks['cobblestone']['strength'], 'cobblestone', self.display.screen))

    def spawn_coal_block(self, x, y):
        self.blocks.append(Coal(x, y, BLOCK_SIZE, BLOCK_SIZE, d_blocks['coal']['skin'], [0, 0], d_blocks['coal']['strength'], 'coal', self.display.screen))

    def spawn_diamond_block(self, x, y):
        self.blocks.append(Diamond(x, y, BLOCK_SIZE, BLOCK_SIZE, d_blocks['diamond']['skin'], [0, 0], d_blocks['diamond']['strength'], 'diamond', self.display.screen))

    @staticmethod
    def update_time():
        global curr_time
        curr_time = datetime.now().microsecond

    def spawn_mob(self, x, y, name):
        pass

    def update(self):
        self.draw()
        self.update_time()

    def draw(self):
        for block in self.blocks[:]:
            block.get_mob(self.player)
            block.update()
            if block.remove():
                self.blocks.remove(block)
        self.inventory.draw()
        self.player.update()


def main():
    global button_down
    app = App((BLOCK_SIZE * 25, BLOCK_SIZE * 20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                button_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pressed_keys.append('a')
                if event.key == pygame.K_d:
                    pressed_keys.append('d')
                if event.key == pygame.K_SPACE:
                    pressed_keys.append(' ')
            if event.type == pygame.KEYUP:
                pressed_keys.clear()

        calculate_delta_time()
        app.display.screen.fill((19, 197, 237))
        app.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
