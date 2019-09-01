import pygame
from RobotCharTest.HealthBar import HealthBar

class BossHealthBar(HealthBar):
    def __init__(self, position=(0,0)):
        super(BossHealthBar,self).__init__(position)
        self.health_full = pygame.image.load("healthbar_full_v2.png").convert_alpha()
        self.health_two_third = pygame.image.load("healthbar_two_third_v2.png").convert_alpha()
        self.health_one_third = pygame.image.load("healthbar_one_third_v2.png").convert_alpha()
        self.health_empty = pygame.image.load("healthybar_empty_v1.png").convert_alpha()
        pass

    def draw(self,win, health):
        if health >= 3:
            win.blit(self.health_full, self.rect)
        elif health==2:
            win.blit(self.health_two_third,self.rect)
        elif health == 1:
            win.blit(self.health_one_third, self.rect)
        else:
            win.blit(self.health_empty, self.rect)
        pass