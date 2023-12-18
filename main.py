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
            newWall.surf = pygame.Surface((i['width'], i['height']))
            newWall.surf.fill((0, 0, 255))
            newWall.rect = newWall.surf.get_rect(center = (i['x'], i['y']))
            screen.blit(newWall.surf, newWall.rect)
            WallsG.add(newWall)

wt = 20
path = 40

wallList = [

            #center path*0.5 eller /2
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2-50-path/2+25, 'y': WINDOW_HEIGHT/2-50-path/2+25},            
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2+path/2+25, 'y': WINDOW_HEIGHT/2-50-path/2+25},
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2-50-path/2+25, 'y': WINDOW_WIDTH/2+path/2+25},            
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2+path/2+25, 'y': WINDOW_WIDTH/2+path/2+25},

            #layer 1 path*1.5
            #l+r center exits    
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2-50-wt-path*1.5+wt/2, 'y': WINDOW_HEIGHT/2+path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2+50+path*1.5+wt/2, 'y': WINDOW_HEIGHT/2+path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2-50-wt-path*1.5+wt/2, 'y': WINDOW_HEIGHT/2-(70+path)-path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2+50+path*1.5+wt/2, 'y': WINDOW_HEIGHT/2-(70+path)-path/2+(70+path)/2},

            #top+bottom center exits
            {'width': 100+path, 'height': wt, 'x': WINDOW_WIDTH/2-50-path/2+(100+path)/2, 'y': WINDOW_HEIGHT/2+50+path/2+path+wt/2},
            {'width': 100+path, 'height': wt, 'x': WINDOW_WIDTH/2-50-path/2+(100+path)/2, 'y': WINDOW_HEIGHT/2-50-wt-path/2-path+wt/2},

            #Layer 2 Total path = path*2.5
            #(x < WINDOW_WIDTH/2) -50-wt*2 (bredden på veggene som kom før)
            #De fleste veggene er bare på layer 2 i 1 av aksene (path*1.5 på den osm ikke er lay2)
            
            #Top walls lay2
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+path*0.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},

            #Bottom walls lay2
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+path*0.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},

            #L+R walls lay 2
            {'width': wt, 'height': 140+path*3, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+(140+path*3)/2},
            {'width': wt, 'height': 140+path*3, 'x': WINDOW_WIDTH/2+50+wt+path*2.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+(140+path*3)/2},
            
            #Layer 3?
            #Top squares 
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},

            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+50/2},
            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+50/2},
            
            #Bottom squares
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},

            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2+wt+path*1.5+50/2},
            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2+wt+path*1.5+50/2},

            #Borders
            #Bot+Top
            {'width': 100+wt*8+path*9, 'height': wt, 'x': WINDOW_WIDTH/2-50-wt*4-path*4.5+(100+wt*8+path*9)/2, 'y': WINDOW_HEIGHT/2+50+wt*3+path*3.5+wt/2},
            {'width': 100+wt*8+path*9, 'height': wt, 'x': WINDOW_WIDTH/2-50-wt*4-path*4.5+(100+wt*8+path*9)/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+wt/2},

            #left
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2-50-wt*5-path*4.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+(50+wt*4+path*3)/2},
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2-50-wt*5-path*4.5+wt/2, 'y': WINDOW_HEIGHT/2+path*0.5+(50+wt*4+path*3)/2}, 
            #right
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2+50+wt*4+path*4.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+(50+wt*4+path*3)/2},
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2+50+wt*4+path*4.5+wt/2, 'y': WINDOW_HEIGHT/2+path*0.5+(50+wt*4+path*3)/2}, 

            #Portal exits?
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2-100-50-wt*4-path*4.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2-wt-path*0.5+wt/2},
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2-100-50-wt*4-path*4.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2+path*0.5+wt/2}, 
            
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2-wt-path*0.5+wt/2},
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2+path*0.5+wt/2},        
            
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

        #collide with walls
    if pygame.sprite.spritecollideany(pacman, WallsG):
        pacman.collideD(direction, speed)
        direction = -1
    
    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()



    #move in a direction with a speed
    pacman.moveUpdate(direction, speed)

    #restricts player from moving outside of the map
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
    
    # Update enemy positions & make the enemy follow the pacman sprite
    fiende.moveFiende(pacman.rect, speed)

    pygame.display.flip()

    # set frame rate to 30
    clock.tick(30)
    

