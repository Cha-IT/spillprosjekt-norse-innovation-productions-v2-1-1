''' Importerer forskjellige libraries inn i vårt spill '''
import pygame
import math


# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

class Fiende(pygame.sprite.Sprite):
    def __init__(self):
        super(Fiende, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((COLOR_RED))
        self.rect = self.image.get_rect()
        self.speed = 3


    def moveFiende(self, pac_man_rect):
        dx, dy = pac_man_rect.x - self.rect.x, pac_man_rect.y - self.rect.y

        if abs(dx) > abs(dy):
            # Move horizontally
            if dx > 0:
                self.rect.x += self.speed
            elif dx < 0:
                self.rect.x -= self.speed
        else:
            # Move vertically
            if dy > 0:
                self.rect.y += self.speed
            elif dy < 0:
                self.rect.y -= self.speed

        if self.rect.left <= 0 or self.rect.right >= pygame.display.get_surface().get_width():
            self.rect.x = max(0, min(self.rect.x, pygame.display.get_surface().get_width() - self.rect.width))

        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.rect.y = max(0, min(self.rect.y, pygame.display.get_surface().get_height() - self.rect.height))
        

            

