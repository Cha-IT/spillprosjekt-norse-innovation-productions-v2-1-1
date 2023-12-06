''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import score
import fiender
import walls

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

pacman = PacMan()
Score = score.Score()
fiende = fiender.Fiende()
wall = walls.Walls()
speed = 10
running = True
direction = -1
points = 0

#sprite groupes
all_sprites = pygame.sprite.Group()
Walls = pygame.sprite.Group()
#add to all sprites
all_sprites.add(wall)
all_sprites.add(pacman)
all_sprites.add(fiende)
#specific
Walls.add(wall)


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

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()

    #collide with walls
    if pygame.sprite.spritecollideany(pacman, Walls):
        pacman.collideD(direction, speed)
        direction = -1

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
    

