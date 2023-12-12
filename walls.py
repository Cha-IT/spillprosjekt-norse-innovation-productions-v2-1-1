import pygame


#there are no gates here
class Walls(pygame.sprite.Sprite):
    wallList = [{'width': 150, 'hight': 25, 'x': 250, 'y': 100},
            {'width': 25, 'hight': 150, 'x': 100, 'y': 250},
            {'width': 150, 'hight': 25, 'x': 400, 'y': 550},
            {'width': 25, 'hight': 150, 'x': 550, 'y': 400},
            {'width': 25, 'hight': 150, 'x': 325, 'y': 325},            
            {'width': 150, 'hight': 25, 'x': 325, 'y': 325},
    ]
    
    def __init__(self):
        super(Walls, self).__init__() 
        self.image = pygame.Surface((0, 0))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (100, 100))

#makes new wall based on the wallList
    @staticmethod
    def wallSelect(screen, walls_group):
        for i in Walls.wallList:
            newWall = Walls()
            newWall.image = pygame.Surface((i['width'], i['hight']))
            newWall.image.fill((255, 255, 255))
            newWall.rect = newWall.image.get_rect(center = (i['x'], i['y']))
            screen.blit(newWall.image, newWall.rect)
            walls_group.add(newWall)


