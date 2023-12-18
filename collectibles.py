import pygame
import random



class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super(Collectible, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 192, 203))
        self.rect = self.image.get_rect(center = (35, 550))
    
    def rLocation(self):
        rNum = random.randint(0,3)

        if rNum == 0:
            self.rect = self.image.get_rect(center = (35, 100))
        elif rNum == 1:
            self.rect = self.image.get_rect(center = (615, 100))
        if rNum == 2:
            self.rect = self.image.get_rect(center = (615, 550))
        elif rNum == 3:
            self.rect = self.image.get_rect(center = (35, 550))

    def cSpawner(self, on, screen, cGroupe):
        if on == True:
            self.rLocation()
            cGroupe.add(self)
        screen.blit(self.image, self.rect)

    def cEat(self):
        self.kill()