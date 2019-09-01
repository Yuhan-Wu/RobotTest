import pygame
import time

class Overheat(pygame.sprite.Sprite):
    def __init__(self, position):
        self.heatMeter = 0
        self.lastShot = 0
        self.cooldown_between_bullets = 1000
        self.isFull = False

        self.overheat_0 = pygame.image.load("overheat_0.png").convert_alpha()
        self.overheat_1 = pygame.image.load("overheat_1.png").convert_alpha()
        self.overheat_2 = pygame.image.load("overheat_2.png").convert_alpha()
        self.overheat_3 = pygame.image.load("overheat_3.png").convert_alpha()
        self.overheat_4 = pygame.image.load("overheat_4.png").convert_alpha()
        self.overheat_5 = pygame.image.load("overheat_5.png").convert_alpha()
        self.overheat_6 = pygame.image.load("overheat_6.png").convert_alpha()

        self.rect = self.overheat_0.get_rect()
        self.rect.topleft = position
        pass

    def check_heat(self, increase, shot_time):
        if self.isFull is False:
            if increase is True:
                self.increase_heat()
                self.lastShot = shot_time
            else:
                self.decrease_heat()
                self.lastShot = shot_time
        else:
            if self.heatMeter == 0:
                self.lastShot = 0
                self.isFull = False
            else:
                self.decrease_heat()
                self.lastShot = shot_time

        if self.heatMeter == 6:
            self.isFull = True
        pass

    def increase_heat(self):
        self.heatMeter += 1
        pass

    def decrease_heat(self):
        if self.heatMeter != 0:
            self.heatMeter -= 1
        pass

    def draw(self, screen):
        if self.heatMeter == 0:
            screen.blit(self.overheat_0, self.rect)
        elif self.heatMeter == 1:
            screen.blit(self.overheat_1, self.rect)
        elif self.heatMeter == 2:
            screen.blit(self.overheat_2, self.rect)
        elif self.heatMeter == 3:
            screen.blit(self.overheat_3, self.rect)
        elif self.heatMeter == 4:
            screen.blit(self.overheat_4, self.rect)
        elif self.heatMeter == 5:
            screen.blit(self.overheat_5, self.rect)
        elif self.heatMeter == 6:
            screen.blit(self.overheat_6, self.rect)
        pass