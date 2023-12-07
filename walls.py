import pygame


class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls, self).__init__() 
        self.surf = pygame.Surface((0, 0))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (100,100))


    def wallSelect(self, screen):
        for i in wallList:
            
            self.surf = pygame.Surface((i['width'], i['hight']))
            self.surf.fill((255, 255, 255))
            self.rect = self.surf.get_rect(center = (i['x'], i['y']))

            screen.blit(self.surf, self.rect)

wallList = [{'width': 200, 'hight': 25, 'x': 200, 'y': 100},
            {'width': 100, 'hight': 25, 'x': 500, 'y': 100},
]
