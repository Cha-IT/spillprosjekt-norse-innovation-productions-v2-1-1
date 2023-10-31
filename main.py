''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
from pygame.locals import (
    K_ESCAPE,
    K_DOWN,
    K_UP,
    K_RIGHT,
    K_LEFT,
    KEYDOWN,
    QUIT
)
import random
import os

'''Import av adre filer'''
import brettet

''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOWS_WIDTH = 650

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)

level = boards

screen = pygame.display.set_mode([WINDOWS_WIDTH, WINDOW_HEIGHT])

''' CLASSES '''

# Spiller classen
class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        super(PacMan, self).__init__()

# Fiende classen
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__()


Life = 3

running = True

path=[((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((470,300),(30,300)),((500,300),(250,30)),((0,200),(200,30))]

''' HOVED LOOPEN '''
while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

    screen.fill(COLOR_RED)
    Draw_board()

    for x in path:
        pygame.draw.rect(screen,(255,255,255),x)

    pygame.display.flip()