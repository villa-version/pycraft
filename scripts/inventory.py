from settings import *


class Inventory:

    cells = [{'ground': 64}, {'cobblestone': 64}, {}, {}, {}, {}, {}, {}, {}, {}]

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
        for i in range(len(self.cells)):
            if len(self.cells[i]) != 0:
                img = d_blocks[list(self.cells[i].keys())[0]]['skin']
                self.screen.blit(pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE)), (self.x + BLOCK_SIZE*i, self.y))

