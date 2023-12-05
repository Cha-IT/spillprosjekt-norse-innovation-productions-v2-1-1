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

import math

''' Initialiserer Pygame som Library og funksjon '''
pygame.init()

current_folder = os.path.dirname(os.path.abspath(__file__))
assets_folder = os.path.join(current_folder, "assets")

# Load image from the assets folder
image_file = "pacman.png"
image_path = os.path.join(assets_folder, image_file)
image = pygame.image.load(image_path)

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


pacman = PacMan()
speed = 10
running = True

''' HOVED LOOPEN '''
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(COLOR_BLACK)       

    # create player
    screen.blit(pacman.surf, pacman.rect)

    # update player position
    pressed_key = pygame.key.get_pressed()
    pacman.moveUpdate(pressed_key, speed)

    pygame.display.flip()
    # set frame rate to 30
    
    clock.tick(30)