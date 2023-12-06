import pygame

class Walls(pygame.sprite.Sprite):
#create player hight width color and shape
    def __init__(self):
        super(Walls, self).__init__()
        self.surf = pygame.Surface((25, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (300, 300)
        )
    