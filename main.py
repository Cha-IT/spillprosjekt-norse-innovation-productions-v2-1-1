''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import score
import math
from spiller import PacMan
from fiender import Fiende
from walls import Walls

from pygame.locals import (
    K_ESCAPE,
    K_DOWN,
    K_UP,
    K_RIGHT,
    K_LEFT,
    KEYDOWN,
    QUIT
)


''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

clock = pygame.time.Clock()

bg = pygame.image.load('images\dackground.png')
bg = pygame.transform.scale(bg, (650, 650))


PI = math.pi

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

color = COLOR_BLUE

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


#variables
speed = 6
running = True
direction = -1
points = 0

#sprite groupes
all_sprites = pygame.sprite.Group()
walls_group = pygame.sprite.Group()

# Call wallSelect using Walls.wallist
Walls.wallSelect(screen, walls_group)

#Creates instances of Score, PacMan and Fiende
Score = score.Score()
fiende = Fiende()
pacman = PacMan()

#add to all sprites
all_sprites.add(pacman)
all_sprites.add(fiende)

''' HOVED LOOPEN '''
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    #fill background
    screen.fill(COLOR_BLACK)   
    screen.blit(bg, (0,0))
    #score
    score.score_instance(Score, screen, WINDOW_WIDTH)

    #Prints the walls
    Walls.wallSelect(screen, walls_group)  # Pass walls_group as an argument

    # Draws all the sprites on the screen
    all_sprites.update()
    all_sprites.draw(screen)

    # draw all sprites
    #for entity in all_sprites:
    #    screen.blit(entity.surf, entity.rect)
    
    #print walls
    walls.Walls.wallSelect(screen, WallsG)
  
    #collide with walls
    if pygame.sprite.spritecollideany(pacman, walls_group):
        pacman.collideD(direction, speed)
        direction = -1
  
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    screen.blit(spiller.pbg, (pacman.rect.left, pacman.rect.top))  

    # update player positions
    pressed_key = pygame.key.get_pressed()

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
    fiende.moveFiende(pacman.rect)

    pygame.display.flip()

    # set frame rate to 30
    clock.tick(30)
    

