from RobotCharTest.Body import Body
from RobotCharTest.Head import Head
import pygame
pygame.init()

class Robot(object):
    def __init__(self,bodyparts):
        self.total_health=2
        self.bodyparts=bodyparts

    def decrease_health(self,bodyPart):
        self.total_health=self.total_health-bodyPart.damage
        return self.total_health<0
        pass

    def draw(self,win):
        for bodypart in self.bodyparts:
            bodypart.draw(win)
    pass




