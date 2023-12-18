''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import score
import math
import spiller
import fiender
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

# Bakgrunnsteksturer
bg = pygame.image.load('images\dackground.png')
bg = pygame.transform.scale(bg, (650, 650))

# Definerer PI med bruk av Matte lib.
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

    #Kollisjoner med vegger for spiller
    if pygame.sprite.spritecollideany(pacman, walls_group):
        pacman.collideD(direction, speed)
        direction = -1

    # Draws all the sprites on the screen
    all_sprites.update()
    all_sprites.draw(screen)

    
    #Printer alle veggene ved bruk av wallSelect funksjonen.
    Walls.wallSelect(screen, walls_group)
  
    # Tegner opp alle sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        screen.blit(spiller.pbg, (pacman.rect.left, pacman.rect.top))  
        screen.blit(fiender.fbg, (fiende.rect.left, fiende.rect.top))  

    # Sjekker for pressed keys og beveger spilleren
    pressed_key = pygame.key.get_pressed()

    # Moveupdate funksjonen som endrer posisjonen til spiller
    pacman.moveUpdate(direction, speed)

    # Definerer bevegelsen til spilleren.
    if pressed_key[K_UP]:
        direction = 0
    elif pressed_key[K_DOWN]:
        direction = 1
    elif pressed_key[K_LEFT]:
        direction = 2
    elif pressed_key[K_RIGHT]:
        direction = 3
    
    # Oppdaterer fienders lokasjon og får den til å følge etter PacMan
    fiende.moveFiende(pacman.rect, walls_group)

    pygame.display.flip()

    # Setter frame rate til 30
    clock.tick(30)
    

