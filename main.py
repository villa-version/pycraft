import pygame


class Display:
    def __init__(self, ss):
        self.width, self.height = ss
        self.screen = pygame.display.set_mode((self.width, self.height))


class App:

    def __init__(self, screen_size):
        self.display = Display(screen_size)

    def update(self):
        pass

    def draw(self):
        pass


def main():

    app = App((1000, 650))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        app.display.screen.fill((255, 255, 255))
        app.update()
        pygame.display.update()


if __name__ == '__main__':
    main()

