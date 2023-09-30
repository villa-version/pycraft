import pygame


BLOCK_SIZE = 30
BUTTON_DOWN = False


class Display:
    def __init__(self, ss):
        self.width, self.height = ss
        self.screen = pygame.display.set_mode((self.width, self.height))


class Block:

    detected = False

    def __init__(self, x, y, w, h, skin_way, speed, strength, name, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = pygame.transform.scale(pygame.image.load(skin_way), (self.w, self.h))
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

    def draw(self):
        self.screen.blit(self.skin, (self.x, self.y))

    def detect(self):
        mx, my = pygame.mouse.get_pos()
        if self.x < mx < self.x + self.w and self.y < my < self.y + self.h:
            self.detected = True
        else:
            self.detected = False

    def breaking(self):
        if BUTTON_DOWN and self.detected:
            self.strength -= 0.5
        else:
            self.strength = self.given_strength

    def remove(self):
        if self.strength == 0:
            return True


class Cobblestone(Block):

    def __init__(self, x, y, w, h, way, speed, strength, name, screen):
        Block.__init__(self, x, y, w, h, way, speed, strength, name, screen)

    def update(self):
        Block.update(self)


class Ground(Block):

    def __init__(self, x, y, w, h, way, speed, strength, name, screen):
        Block.__init__(self, x, y, w, h, way, speed, strength, name, screen)

    def update(self):
        Block.update(self)


class Inventory:

    cells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, x, y, w, h, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.w, self.h))


class App:

    blocks = []
    d_blocks = {
        'ground': {'skin': 'image/block_skins/ground.png', 'strength': 50},
        'cobblestone': {'skin': 'image/block_skins/cobblestone.jpg', 'strength': 100}
    }

    def __init__(self, screen_size):
        self.display = Display(screen_size)
        self.inventory = Inventory(self.display.width//2-BLOCK_SIZE*4.5, self.display.height-BLOCK_SIZE, BLOCK_SIZE*9, BLOCK_SIZE, self.display.screen)
        self.spawn_world()

    def spawn_world(self):
        for y in range(self.display.height//(2*BLOCK_SIZE)):
            for x in range(self.display.width//BLOCK_SIZE):
                if y < 3:
                    self.spawn_block(BLOCK_SIZE * x, self.display.height // 2 + BLOCK_SIZE * y, 'ground')
                else:
                    self.spawn_block(BLOCK_SIZE * x, self.display.height // 2 + BLOCK_SIZE * y, 'cobblestone')

    def spawn_block(self, x, y, name):
        self.blocks.append(Ground(x, y, BLOCK_SIZE, BLOCK_SIZE, self.d_blocks[name]['skin'], (0, 0),
                                  self.d_blocks[name]['strength'], name, self.display.screen))

    def update(self):
        self.draw()

    def draw(self):
        for block in self.blocks[:]:
            block.update()
            if block.remove():
                self.blocks.remove(block)
        self.inventory.draw()


def main():
    global BUTTON_DOWN
    app = App((BLOCK_SIZE*25, BLOCK_SIZE*20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                BUTTON_DOWN = True
            if event.type == pygame.MOUSEBUTTONUP:
                BUTTON_DOWN = False

        app.display.screen.fill((19, 197, 237))
        app.update()
        pygame.display.update()


if __name__ == '__main__':
    main()
