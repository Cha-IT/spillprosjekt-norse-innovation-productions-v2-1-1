import pygame


#there are no gates here
class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls, self).__init__() 
        self.image = pygame.Surface((0, 0))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (100, 100))

#makes new wall based on the wallList
    @staticmethod
    def wallSelect(screen, walls_group):
        for i in wallList:
            #add newWall
            newWall = Walls()
            #give newWall size, color and position
            newWall.image = pygame.Surface((i['width'], i['hight']))
            newWall.image.fill((255, 255, 255))
            newWall.rect = newWall.image.get_rect(center = (i['x'], i['y']))
            #give newWall texture
            wbg = pygame.image.load('images\wall.png')
            wbg = pygame.transform.scale(wbg, (i['width'], i['hight']))
            #blit newWall
            screen.blit(newWall.image, newWall.rect)
            #blit texture over wall
            screen.blit(wbg, (i['x'] - (i['width']/2), i['y'] - (i['hight']/2)))
            #add wall to group for colision
            walls_group.add(newWall)

wt = 20

wallList = [{'width': 370, 'hight': wt, 'x': 100+370/2, 'y': 100+wt/2},
            {'width': wt, 'hight': 120, 'x': 100+wt/2, 'y': 250},
            {'width': 130, 'hight': wt, 'x': 400, 'y': 550-wt/2},
            {'width': wt, 'hight': 120, 'x': 530+wt/2, 'y': 400},
            {'width': wt*2, 'hight': 120, 'x': 325, 'y': 325},
            {'width': 120, 'hight': wt*2, 'x': 325, 'y': 325},
            {'width': 120, 'hight': wt, 'x': 275-60, 'y': 275-wt/2},
            {'width': wt, 'hight': 120, 'x': 255+wt/2, 'y': 275-60},
            {'width': 120, 'hight': wt, 'x': 275-60, 'y': 275-wt/2},
            {'width': 120, 'hight': wt, 'x': 395-60+100, 'y': 275-wt/2},
            {'width': wt, 'hight': 120, 'x': 325+wt/2+50, 'y': 275-60},
            {'width': wt, 'hight': 120, 'x': 255+wt/2, 'y': 275+100+60},
            {'width': 120, 'hight': wt, 'x': 275-60, 'y': 275+120-wt/2},
            {'width': 120, 'hight': wt, 'x': 395-60+100, 'y': 275+120-wt/2},
            {'width': wt, 'hight': 120, 'x': 325+wt/2+50, 'y': 275+100+60},
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275+120+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395-70, 'y': 275+120+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275-120+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395-70, 'y': 275-120+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275-120+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275+50},
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275+120+50},

]