import pygame
from RobotCharTest.Drone import Drone
from RobotCharTest.BossHealthBar import BossHealthBar

class BossDrone(Drone):
    def __init__(self,path,position):
        super(BossDrone,self).__init__(path,position)
        self.image = pygame.image.load('robot_head_v1.png')
        self.health = 3
        self.initial_position = position
        self.isActive=False
        self.health_bar=BossHealthBar((position[0] + 18, position[1] - 20))
        pass

    def damage(self, value):
        self.health += value
        if self.health == 2:
            self.image = pygame.image.load('robot_head_v1.png')
        if self.health == 1:
            self.image = pygame.image.load('robot_head_v1.png')
        if self.health <= 0:
            self.reset()
            return True
        return False

    def reset(self):
        self.rect.topleft = self.initial_position
        self.health_bar.rect.topleft = (self.rect.topleft[0] + 18, self.rect.topleft[1] - 20)
        self.health = 3

