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

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

color= COLOR_BLUE
color = COLOR_BLUE


class Fiende(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Fiende, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((COLOR_RED))
        self.rect = self.surf.get_rect()
        self.speed = 1
        self.x = x
        self.y = y

    def moveFiende(self, speed):
        self.rect.move_ip(self.speed, 0)
       
            

