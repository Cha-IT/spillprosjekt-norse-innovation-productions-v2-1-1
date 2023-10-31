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

''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOWS_WIDTH = 650
# cock um... i mean clock
clock = pygame.time.Clock()

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)

screen = pygame.display.set_mode([WINDOWS_WIDTH, WINDOW_HEIGHT])

''' CLASSES '''

# Spiller classen
class PacMan(pygame.sprite.Sprite):
#create player hight width color and shape
    def __init__(self):
        super(PacMan, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
#create movment for the player 
    def moveUpdate(self, Key_pressed, speed):
        if Key_pressed[K_UP]:
            self.rect.move_ip(0, -speed)
        if Key_pressed[K_DOWN]:
            self.rect.move_ip(0, speed)
        if Key_pressed[K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if Key_pressed[K_RIGHT]:
            self.rect.move_ip(speed, 0)

# Fiende classen
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__()

pacman = PacMan()

Life = 3
speed = 5
running = True

path=[((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((470,300),(30,300)),((500,300),(250,30)),((0,200),(200,30))]

''' HOVED LOOPEN '''
while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False

    screen.fill(COLOR_RED)
    for x in path:
        pygame.draw.rect(screen,(255,255,255),x)
    
    # create player
    screen.blit(pacman.surf, pacman.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()
    pacman.moveUpdate(pressed_key, speed)

    pygame.display.flip()
    # set frame rate to 30
    clock.tick(30)