import pygame

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

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
            newWall.image = pygame.Surface((i['width'], i['height']))
            newWall.image.fill((255, 255, 255))
            newWall.rect = newWall.image.get_rect(center = (i['x'], i['y']))
            #Gir newWall teksturer
            wbg = pygame.image.load('images\wall.png')
            wbg = pygame.transform.scale(wbg, (i['width'], i['height']))
            #Viser newWall
            screen.blit(newWall.image, newWall.rect)
            #blit tekstur over vegg
            screen.blit(wbg, (i['x'] - (i['width']/2), i['y'] - (i['height']/2)))
            #Legger til newWall til walls_group for å bruke den videre i andre funksjoner.
            walls_group.add(newWall)


wt = 20
path = 40

wallList = [

            #center path*0.5 eller /2
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2-50-path/2+25, 'y': WINDOW_HEIGHT/2-50-path/2+25},            
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2+path/2+25, 'y': WINDOW_HEIGHT/2-50-path/2+25},
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2-50-path/2+25, 'y': WINDOW_WIDTH/2+path/2+25},            
            {'width': 50, 'height': 50, 'x': WINDOW_WIDTH/2+path/2+25, 'y': WINDOW_WIDTH/2+path/2+25},

            #layer 1 path*1.5
            #l+r center exits    
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2-50-wt-path*1.5+wt/2, 'y': WINDOW_HEIGHT/2+path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2+50+path*1.5+wt/2, 'y': WINDOW_HEIGHT/2+path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2-50-wt-path*1.5+wt/2, 'y': WINDOW_HEIGHT/2-(70+path)-path/2+(70+path)/2},
            {'width': wt, 'height': 70+path, 'x': WINDOW_WIDTH/2+50+path*1.5+wt/2, 'y': WINDOW_HEIGHT/2-(70+path)-path/2+(70+path)/2},

            #top+bottom center exits
            {'width': 100+path, 'height': wt, 'x': WINDOW_WIDTH/2-50-path/2+(100+path)/2, 'y': WINDOW_HEIGHT/2+50+path/2+path+wt/2},
            {'width': 100+path, 'height': wt, 'x': WINDOW_WIDTH/2-50-path/2+(100+path)/2, 'y': WINDOW_HEIGHT/2-50-wt-path/2-path+wt/2},

            #Layer 2 Total path = path*2.5
            #(x < WINDOW_WIDTH/2) -50-wt*2 (bredden på veggene som kom før)
            #De fleste veggene er bare på layer 2 i 1 av aksene (path*1.5 på den osm ikke er lay2)
            
            #Top walls lay2
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+path*0.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},

            #Bottom walls lay2
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},
            {'width': 90+path*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+path*0.5+(90+path*2)/2, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},

            #L+R walls lay 2
            {'width': wt, 'height': 140+path*3, 'x': WINDOW_WIDTH/2-50-wt*2-path*2.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+(140+path*3)/2},
            {'width': wt, 'height': 140+path*3, 'x': WINDOW_WIDTH/2+50+wt+path*2.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+(140+path*3)/2},
            
            #Layer 3?
            #Top squares 
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt*3-path*2.5+wt},

            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+50/2},
            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2-50-wt-path*1.5+50/2},
            
            #Bottom squares
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},
            {'width': wt*2, 'height': wt*2, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2+50+wt+path*2.5+wt},

            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+wt, 'y': WINDOW_HEIGHT/2+wt+path*1.5+50/2},
            {'width': wt*2, 'height': 50, 'x': WINDOW_WIDTH/2-50-wt*4-path*3.5+wt, 'y': WINDOW_HEIGHT/2+wt+path*1.5+50/2},

            #Borders
            #Bot+Top
            {'width': 100+wt*8+path*9, 'height': wt, 'x': WINDOW_WIDTH/2-50-wt*4-path*4.5+(100+wt*8+path*9)/2, 'y': WINDOW_HEIGHT/2+50+wt*3+path*3.5+wt/2},
            {'width': 100+wt*8+path*9, 'height': wt, 'x': WINDOW_WIDTH/2-50-wt*4-path*4.5+(100+wt*8+path*9)/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+wt/2},

            #left
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2-50-wt*5-path*4.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+(50+wt*4+path*3)/2},
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2-50-wt*5-path*4.5+wt/2, 'y': WINDOW_HEIGHT/2+path*0.5+(50+wt*4+path*3)/2}, 
            #right
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2+50+wt*4+path*4.5+wt/2, 'y': WINDOW_HEIGHT/2-50-wt*4-path*3.5+(50+wt*4+path*3)/2},
            {'width': wt, 'height': 50+wt*4+path*3, 'x': WINDOW_WIDTH/2+50+wt*4+path*4.5+wt/2, 'y': WINDOW_HEIGHT/2+path*0.5+(50+wt*4+path*3)/2}, 

            #Portal exits?
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2-100-50-wt*4-path*4.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2-wt-path*0.5+wt/2},
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2-100-50-wt*4-path*4.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2+path*0.5+wt/2}, 
            
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2-wt-path*0.5+wt/2},
            {'width': 100+path+wt*2, 'height': wt, 'x': WINDOW_WIDTH/2+50+wt*2+path*3.5+(100+path+wt*2)/2, 'y': WINDOW_HEIGHT/2+path*0.5+wt/2},        
            
]