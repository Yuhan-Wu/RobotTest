import pygame

class ScoreBoard(object):
    def __init__(self, position=(0,0)):
        self.position = position
        self.font = pygame.font.SysFont("Arial", 72)
        self.score = 0
        self.content = "Score: " + str(self.score)
        self.text = self.font.render(self.content, True, (0, 128, 0))
        self.rect = self.text.get_rect()

    def add_score(self, value):
        self.score += value
        self.content = "Score: " + str(self.score)
        self.text = self.font.render(self.content, True, (0, 128, 0))
        self.rect = self.text.get_rect()

    def draw(self, screen):
        screen.blit(self.text, self.rect)
