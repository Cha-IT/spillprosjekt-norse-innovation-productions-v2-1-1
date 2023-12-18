import pygame
import random
import score

class Collectible(pygame.sprite.Sprite):
    def __init__(self):
        super(Collectible, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 192, 203))
        self.rect = self.image.get_rect(center = (35, 550))
        #Hell
        self.Score = 100

    def cSpawner(self, screen, cGroupe, pacman, score):
        #only prints out fruit if no fruit is out
        if not len(cGroupe.sprites()) > 0:
            #set position
            i = collectibleLocationList[random.randint(0,3)]
            self.rect = self.image.get_rect(center = (i['x'], i['y']))
            #set colour and points
            e = collectibleScoreList[random.randint(0,2)]
            self.Score = e['score']
            self.image.fill(e['RGB'])
            #add to group
            cGroupe.add(self) 
        screen.blit(self.image, self.rect)

        #kills fruit and gives points
        if pygame.sprite.spritecollideany(pacman, cGroupe):
            self.kill()
            score.score_up(self.Score)

collectibleLocationList = [
    {'x':35, 'y':100},
    {'x':35, 'y':550},
    {'x':615, 'y':100},
    {'x':615, 'y':550},
]
collectibleScoreList = [
    {'score':100, 'RGB':(255, 192, 203)},
    {'score':50, 'RGB':(255, 0, 0)},
    {'score':125, 'RGB':(100, 0, 255)},
]