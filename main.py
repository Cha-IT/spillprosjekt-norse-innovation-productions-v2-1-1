''' Importerer forskjellige libraries inn i vårt spill '''
import pygame

import score
import os
import fiender

from pygame.locals import (
    K_ESCAPE,
    K_DOWN,
    K_UP,
    K_RIGHT,
    K_LEFT,
    KEYDOWN,
    QUIT
)

import math

''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

clock = pygame.time.Clock()


PI = math.pi

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

color= COLOR_BLUE
color = COLOR_BLUE

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

''' CLASSES '''
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

pacman = PacMan()
Score = score.Score()
fiende = fiender.Fiende()
speed = 10
running = True
direction = -1
points = 0

pygame.time.set_timer(100, 100)

''' HOVED LOOPEN '''
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    #fill background
    screen.fill(COLOR_BLACK)       


    #score
    score.score_instance(Score, screen, WINDOW_WIDTH)

    # Show and upadte player and enemies
    screen.blit(pacman.surf, pacman.rect)
    screen.blit(fiende.surf, fiende.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()

    #move in a direction with a speed
    pacman.moveUpdate(direction, speed)

    #traps player in hell
    pacman.borders()

    #set direction of movement
    if pressed_key[K_UP]:
        direction = 0
    elif pressed_key[K_DOWN]:
        direction = 1
    elif pressed_key[K_LEFT]:
        direction = 2
    elif pressed_key[K_RIGHT]:
        direction = 3

    pacman.moveUpdate(pressed_key, speed)
    
    # Update enemy positions
    fiende.moveFiende(speed)

    pygame.display.flip()

    # set frame rate to 30
    clock.tick(30)
    

