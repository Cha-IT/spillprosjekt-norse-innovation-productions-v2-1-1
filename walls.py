import pygame


# Vegg Klassen i spillet. Definerer surfacen
class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls, self).__init__() 
        self.image = pygame.Surface((0, 0))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (100, 100))

#Funksjonen som lager vegger på spillbrettet ut fra instrukser i vegglisten (wallSelect)
    @staticmethod
    def wallSelect(screen, walls_group):
        for i in wallList:
            #ny vegg - newWall
            newWall = Walls()
            #Gir newWall farge, størrelse og lokasjon
            newWall.image = pygame.Surface((i['width'], i['hight']))
            newWall.image.fill((255, 255, 255))
            newWall.rect = newWall.image.get_rect(center = (i['x'], i['y']))
            #Gir newWall teksturer
            wbg = pygame.image.load('images\wall.png')
            wbg = pygame.transform.scale(wbg, (i['width'], i['hight']))
            #Viser newWall
            screen.blit(newWall.image, newWall.rect)
            #blit tekstur over vegg
            screen.blit(wbg, (i['x'] - (i['width']/2), i['y'] - (i['hight']/2)))
            #Legger til newWall til walls_group for å bruke den videre i andre funksjoner.
            walls_group.add(newWall)

wt = 20

wallList = [#Long walls outside center
            {'width': 370, 'hight': wt, 'x': 100+370/2, 'y': 100+wt/2},
            {'width': wt, 'hight': 120, 'x': 100+wt/2, 'y': 250},
            {'width': 130, 'hight': wt, 'x': 400, 'y': 550-wt/2},
            {'width': wt, 'hight': 120, 'x': 530+wt/2, 'y': 400},

            #center
            {'width': wt*2, 'hight': 120, 'x': 325, 'y': 325},            
            {'width': 120, 'hight': wt*2, 'x': 325, 'y': 325},
            
            #Top-left corner center
            {'width': 120, 'hight': wt, 'x': 275-60, 'y': 275-wt/2},
            {'width': wt, 'hight': 120, 'x': 255+wt/2, 'y': 275-60},

            #Top-right corner center
            {'width': 120, 'hight': wt, 'x': 395-60+100, 'y': 275-wt/2},
            {'width': wt, 'hight': 120, 'x': 325+wt/2+50, 'y': 275-60},

            #Bottom-left corner center
            {'width': wt, 'hight': 120, 'x': 255+wt/2, 'y': 275+100+60},
            {'width': 120, 'hight': wt, 'x': 275-60, 'y': 275+120-wt/2},

            #Bottom-right corner center
            {'width': 120, 'hight': wt, 'x': 395-60+100, 'y': 275+120-wt/2},
            {'width': wt, 'hight': 120, 'x': 325+wt/2+50, 'y': 275+100+60},

            #BR
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275+120+50},
            #BC
            {'width': wt*2, 'hight': wt*2, 'x': 395-70, 'y': 275+120+50},
            #BL
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275+120+50},
            #CR
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275+50},
            #CL
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275+50},
            #TR
            {'width': wt*2, 'hight': wt*2, 'x': 395+120-70, 'y': 275-120+50},
            #TC
            {'width': wt*2, 'hight': wt*2, 'x': 395-70, 'y': 275-120+50},
            #TL
            {'width': wt*2, 'hight': wt*2, 'x': 395-120-70, 'y': 275-120+50},
                   
]