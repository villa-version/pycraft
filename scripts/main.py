import pygame
from speed import Speed
from settings import settings
from display import Display
from player import Player
from controller import controller
from timer import timer
from world import World


BLOCK_SIZE = settings.BLOCK_SIZE


class App:

    world = None
    detected_block = None

    def __init__(self, screen_size):
        self.display = Display(screen_size)
        self.player = Player(self.display.width // 2, self.display.height // 2 - BLOCK_SIZE * 10,
                             settings.BLOCK_SIZE, settings.BLOCK_SIZE * 2, pygame.image.load('image/mobs_skin/steve.png'),
                             10, Speed(0.25, 0), 'player', self.display)
        self.create_world()

    def create_world(self):
        self.world = World(self.display, self.player)
        for i in range(1, 6):
            x = self.display.width // (2*BLOCK_SIZE) - i
            y = self.display.height // (2*BLOCK_SIZE) - i
            self.world.spawn_wood_block(x, y)

    def update(self):
        self.attraction()
        self.rub()
        self.world.update()
        self.check_detected_block()
        self.player.update()
        self.add_block()
        timer.update_timer()

    def check_detected_block(self):
        for block in self.world.blocks:
            if block.detected:
                self.detected_block = block
                break

    def add_block(self):
        if self.detected_block is not None:
            x1, y1 = self.detected_block.x - 1, self.detected_block.y
            x2, y1 = self.detected_block.x + 1, self.detected_block.y
            y2 = self.detected_block.y - 1
            y3 = self.detected_block.y + 1

            self.detected_block = None

    def attraction(self):
        self.player.y -= self.player.speed.y
        self.player.speed.y = -settings.GRAVITY * timer.timer

    def rub(self):
        pass


def main():
    app = App(screen_size=(BLOCK_SIZE * settings.MAX_BLOCKS_X, BLOCK_SIZE * settings.MAX_BLOCKS_Y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                controller.button_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                controller.button_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    controller.pressed_keys.append('a')
                if event.key == pygame.K_d:
                    controller.pressed_keys.append('d')
                if event.key == pygame.K_SPACE:
                    controller.pressed_keys.append(' ')
            if event.type == pygame.KEYUP:
                controller.pressed_keys.clear()

        app.display.screen.fill((19, 197, 237))
        app.update()
        pygame.display.update()
        controller.mouse.update()


if __name__ == '__main__':
    main()
