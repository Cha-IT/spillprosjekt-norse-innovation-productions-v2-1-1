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

WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

color = COLOR_BLUE

# Spiller classen
class PacMan(pygame.sprite.Sprite):
#create player hight width color and shape
    def __init__(self):
        super(PacMan, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((COLOR_YELLOW))
        self.rect = self.surf.get_rect()
        
#create movment for the player 
    def moveUpdate(self, d, speed):
        if d == -1:
            self.rect.move_ip(0, 0)
        if d == 0:
            self.rect.move_ip(0, -speed)
        if d == 1:
            self.rect.move_ip(0, speed)
        if d == 2:
            self.rect.move_ip(-speed, 0)
        if d == 3:
            self.rect.move_ip(speed, 0)

#borders around the world
    def borders(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

    #collide with non killing stuff
    def collideD(self, d, moveBack):
        if d == 0:
            self.rect.top += moveBack
        if d == 1:
            self.rect.bottom -= moveBack
        if d == 2:
            self.rect.left += moveBack
        if d == 3:
            self.rect.right -= moveBack