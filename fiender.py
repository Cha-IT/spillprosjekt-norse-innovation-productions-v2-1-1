''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import math
import spiller
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

class Fiende(pygame.sprite.Sprite):
    def __init__(self):
        super(Fiende, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((COLOR_RED))
        self.rect = self.surf.get_rect()
        self.xspeed = 3
        self.yspeed = 2

    def moveFiende(self, pac_man_rect, speed):
        # distancex and distancey is being calculated between pacman and the enemy
        dx, dy = pac_man_rect.x - self.rect.x, pac_man_rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        # Makes the player follow the pacman figure and calculates distance throughout the whole game.
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.xspeed
            self.rect.y += dy * self.yspeed
        
        # Restricts the enemy from going out of the map
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.xspeed = -self.xspeed

        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.yspeed = -self.yspeed

            

