import pygame

# Score klassen som teller poenger
class Score(object):
    def __init__(self):
        self.white = 255,255,255
        self.count = 0
        self.font = pygame.font.SysFont("comicsans",25, True , True)
        self.text = self.font.render('Score:' + str(self.count),1,self.white)

    def show_score(self, screen, width):
        screen.blit(self.text, (width/2-50, 0))

    def score_up(self, score):
        self.count += score
        self.text = self.font.render('Score:' + str(self.count),1,self.white)

def score_instance(score_instance, screen, width):
    score_instance.show_score(screen, width)