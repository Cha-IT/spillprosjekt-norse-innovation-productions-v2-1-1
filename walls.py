import pygame


#there are no gates here
class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls, self).__init__() 
        self.surf = pygame.Surface((0, 0))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (100,100))

#makes new wall based on the wallList
    def wallSelect(screen, WallsG):
        for i in wallList:
            #add newWall
            newWall = Walls()
            #give newWall size, color and position
            newWall.surf = pygame.Surface((i['width'], i['hight']))
            newWall.surf.fill((255, 255, 255))
            newWall.rect = newWall.surf.get_rect(center = (i['x'], i['y']))
            #give newWall texture
            wbg = pygame.image.load('images\wall.png')
            wbg = pygame.transform.scale(wbg, (i['width'], i['hight']))
            #blit newWall
            screen.blit(newWall.surf, newWall.rect)
            #blit texture over wall
            screen.blit(wbg, (i['x'] - (i['width']/2), i['y'] - (i['hight']/2)))
            #add wall to group for colision
            WallsG.add(newWall)

wallList = [{'width': 150, 'hight': 25, 'x': 250, 'y': 100},
            {'width': 25, 'hight': 150, 'x': 100, 'y': 250},
            {'width': 150, 'hight': 25, 'x': 400, 'y': 550},
            {'width': 25, 'hight': 150, 'x': 550, 'y': 400},
            {'width': 25, 'hight': 150, 'x': 325, 'y': 325},         
            {'width': 150, 'hight': 25, 'x': 325, 'y': 325},
]
