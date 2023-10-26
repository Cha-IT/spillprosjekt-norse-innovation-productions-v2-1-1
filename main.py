# Importerer forskjellige libraries inn i vårt spill
import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN
)
import random

# Initialiserer Pygame som Library og funksjon
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 850
WINDOWS_WIDTH = 850

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)

screen = pygame.display.set_mode([WINDOWS_WIDTH, WINDOW_HEIGHT])

class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        super(PacMan, self).__init__()

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__()


Life = 3

running = True

while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False