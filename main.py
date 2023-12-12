''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import score
import fiender
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

color = COLOR_BLUE

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

''' CLASSES '''

#there are no gates here
class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls, self).__init__() 
        self.surf = pygame.Surface((0, 0))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (100,100))

#makes new wall based on the wallList
    def wallSelect(screen):
        for i in wallList:
            newWall = Walls()
            newWall.surf = pygame.Surface((i['width'], i['hight']))
            newWall.surf.fill((255, 255, 255))
            newWall.rect = newWall.surf.get_rect(center = (i['x'], i['y']))
            screen.blit(newWall.surf, newWall.rect)
            WallsG.add(newWall)

wallList = [{'width': 150, 'hight': 25, 'x': 250, 'y': 100},
            {'width': 25, 'hight': 150, 'x': 100, 'y': 250},
            {'width': 150, 'hight': 25, 'x': 400, 'y': 550},
            {'width': 25, 'hight': 150, 'x': 550, 'y': 400},
            {'width': 25, 'hight': 150, 'x': 325, 'y': 325},            
            {'width': 150, 'hight': 25, 'x': 325, 'y': 325},
]
#variables
Score = score.Score()
fiende = fiender.Fiende()
speed = 10
pacman = spiller.PacMan()
Score = score.Score()
fiende = fiender.Fiende()
speed = 6
running = True
direction = -1
points = 0

#sprite groupes
all_sprites = pygame.sprite.Group()
WallsG = pygame.sprite.Group()
#add to all sprites
all_sprites.add(pacman)
all_sprites.add(fiende)
#specific

''' HOVED LOOPEN '''
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    #fill background
    screen.fill(COLOR_BLACK)   

    #score
    score.score_instance(Score, screen, WINDOW_WIDTH)   

    #print walls
    Walls.wallSelect(screen)
    
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()

    #collide with walls
    if pygame.sprite.spritecollideany(pacman, WallsG):
        pacman.collideD(direction, speed)
        direction = -1

    #move in a direction with a speed
    pacman.moveUpdate(direction, speed)

    #restricts player from moving outside of the map - OLD Method look at spiller.py documentation
    #pacman.borders()

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
    
    # Update enemy positions & make the enemy follow the pacman sprite
    fiende.moveFiende(pacman.rect, speed)

    pygame.display.flip()

    # set frame rate to 30
    clock.tick(30)
    

