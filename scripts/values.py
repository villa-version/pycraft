from datetime import datetime
import pygame


cont_time = 0
button_down = None
pressed_keys = []
gravity = 0.1
BLOCK_SIZE = 30
curr_time = datetime.now().microsecond
last_time = curr_time

d_blocks = {
        'ground':      {'skin': pygame.image.load('image/block_skins/ground.png'),      'strength': 50},
        'cobblestone': {'skin': pygame.image.load('image/block_skins/cobblestone.jpg'), 'strength': 100},
        'wood':        {'skin': pygame.image.load('image/block_skins/wood.png'),        'strength': 100},
        'coal':        {'skin': pygame.image.load('image/block_skins/coal.png'),        'strength': 100},
        'diamond':     {'skin': pygame.image.load('image/block_skins/diamond.png'),     'strength': 100}
    }
d_mobs = {
    'player': {'skin': pygame.image.load('image/mobs_skin/steve.png'),
               'size': (BLOCK_SIZE, BLOCK_SIZE*2), 'hp': 10, 'speed': [0.5, 0]}
    }

