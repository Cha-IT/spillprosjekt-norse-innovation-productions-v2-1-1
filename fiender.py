''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
from time import sleep, time
import math
import random

# Teksturer for fienden
fbg = pygame.image.load('images\enemy.png')
fbg = pygame.transform.scale(fbg,(25,25))

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)


#Fiende klassen
class Fiende(pygame.sprite.Sprite):
    def __init__(self):
        super(Fiende, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((COLOR_RED))
        self.rect = self.image.get_rect(center = (325, 225))
        self.speed = 3
        

    # moveFiende som tar for seg bevegelsen til fienden og hvordan den skal følge etter pacman og evt kollisjoner.
    def update(self, pac_man_rect, walls_group):
        
        # Beregner distanse mellom pacman og fienden selv.
        dx, dy = pac_man_rect.x - self.rect.x, pac_man_rect.y - self.rect.y

        new_rect = self.rect.copy()

        direction = ''
        # Tvinger fienden til å bevege seg med 90 graders vinkel slik at den beveger seg likt som vår hovedfigur.
        # Her sjekker den om distanse x er større enn distanse y. Om den er det beveger den seg på x aksen
        # Om ikke beveger den seg på y aksen.


        if abs(dx) > abs(dy):
            # Move horizontally
            if dx > 0:
                new_rect.x += self.speed

            elif dx < 0:
                new_rect.x -= self.speed

        else:
            # Move vertically
            if dy > 0:
                new_rect.y += self.speed

            elif dy < 0:
                new_rect.y -= self.speed



        self.rect = new_rect

        if pygame.sprite.spritecollideany(self, walls_group):
            if dx > 0 or dx < 0:
                new_rect.y -= self.speed
  
            if dy > 0 or dy < 0:
                new_rect.x -= self.speed                   



        # Adjust the position to stay within screen boundaries
        # Setter en grense for fiendene slik at den ikke kan bevege seg ut av spill vinduet.
        self.rect.x = max(0, min(self.rect.x, pygame.display.get_surface().get_width() - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, pygame.display.get_surface().get_height() - self.rect.height))

