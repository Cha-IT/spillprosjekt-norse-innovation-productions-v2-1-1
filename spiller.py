''' Importerer forskjellige libraries inn i vårt spill '''
import pygame

# Fargepalett
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (253, 255, 0)
COLOR_BLUE = (0, 0 ,255)

# Vindu Høyde og bredde
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 650

pbg = pygame.image.load('images\player.png')
pbg = pygame.transform.scale(pbg,(25,25))

# Spiller classen
class PacMan(pygame.sprite.Sprite):
#Definerer spilleren, imaget og fargene.
    def __init__(self):
        super(PacMan, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((COLOR_YELLOW))
        self.rect = self.image.get_rect()

#Oppretter bevegelse for spilleren. Starter på X & Y: 0, 0 
    def moveUpdate(self, d, speed):      
        x, y = self.rect.x, self.rect.y

        if d == 0:
            y -= speed
        elif d == 1:
            y += speed
        elif d == 2:
            x -= speed
        elif d == 3:
            x += speed

        # Sjekker om x og y posisjon er større eller mindre en vindu høyde og bredde, og om figuren berører en av disse hjørnene.
        # Om den gjør det stopper den opp og kan ikke gå videre.
        if 0 <= x <= WINDOW_WIDTH - self.rect.width and 0 <= y <= WINDOW_HEIGHT - self.rect.height:
            self.rect.x, self.rect.y = x, y

    # Kollisjoner med vegger for spilleren
    def collideD(self, d, speed):
        if d == 0:
            self.rect.move_ip(0, speed)
        if d == 1:
            self.rect.move_ip(0, -speed)
        if d == 2:
            self.rect.move_ip(speed, 0)
        if d == 3:
            self.rect.move_ip(-speed, 0)