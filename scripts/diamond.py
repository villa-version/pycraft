from block import Block


class Diamond(Block):

    def __init__(self, x, y, w, h, way, speed, strength, name, screen):
        Block.__init__(self, x, y, w, h, way, speed, strength, name, screen)

    def update(self):
        Block.update(self)

