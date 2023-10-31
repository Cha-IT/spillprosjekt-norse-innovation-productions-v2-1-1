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
import random
import os
import math

'''Import av adre filer'''
import brettet

''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650
# cock um... i mean clock
clock = pygame.time.Clock()


PI = math.pi

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)
color = COLOR_BLUE

level = brettet.boards

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

''' CLASSES '''

# Spiller classen
class PacMan(pygame.sprite.Sprite):
#create player hight width color and shape
    def __init__(self):
        super(PacMan, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
#create movment for the player 
    def moveUpdate(self, Key_pressed, speed):
        if Key_pressed[K_UP]:
            self.rect.move_ip(0, -speed)
        if Key_pressed[K_DOWN]:
            self.rect.move_ip(0, speed)
        if Key_pressed[K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if Key_pressed[K_RIGHT]:
            self.rect.move_ip(speed, 0)

# Fiende classen
class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__()


def draw_board():
    num1 = ((WINDOW_HEIGHT - 50) // 32)
    num2 = (WINDOW_WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            if level[i][j] == 2: #and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
pacman = PacMan()

Life = 3
speed = 5
running = True

''' HOVED LOOPEN '''
while running:

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
            
    screen.fill(COLOR_BLACK)       
    draw_board()
    
    
    # create player
    screen.blit(pacman.surf, pacman.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()
    pacman.moveUpdate(pressed_key, speed)

    pygame.display.flip()
    # set frame rate to 30
    clock.tick(30)