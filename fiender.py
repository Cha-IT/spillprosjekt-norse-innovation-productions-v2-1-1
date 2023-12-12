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
        self.xspeed = 4
        self.yspeed = 6

    def moveFiende(self, pac_man_rect, speed):
        # distancex and distancey is being calculated between pacman and the enemy
        dx, dy = pac_man_rect.x - self.rect.x, pac_man_rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        # Makes the player follow the pacman figure and calculates distance throughout the whole game.
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.xspeed
            self.rect.y += dy * self.yspeed

        # Checks through the absolute value of dx and dy and if dx is a higher number 
        # it adjusts the movement to follow 90-degree angles to have a similiar movement as the player
        if abs(dx) > abs(dy):
            # Snaps the player in increments of 25 degress in y-direction
            self.rect.y = round(self.rect.y / 25) * 25

            # Handles collisions with the map / window width and height
            self.rect.clamp_ip(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        else:
            # Snaps the player in increments of 25 degress in x-direction
            self.rect.x = round(self.rect.x / 25) * 25

            # Handle collisions with THE MAP / WINDOW WIDTH AND HEIGHT
            self.rect.clamp_ip(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        

            

