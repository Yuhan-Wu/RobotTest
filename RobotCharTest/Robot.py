from RobotCharTest.Body import Body
from RobotCharTest.Head import Head
import pygame
pygame.init()

class Robot(object):
    def __init__(self):
        self.total_health=1
        body=Body()
        self.bodyparts=[]
        self.bodyparts.append(body)

    def decrease_health(self,bodyPart):
        self.total_health=self.total_health-bodyPart.damage
        if self.total_health==0:
            print("Win")
        pass

    def draw(self,win):
        for bodypart in self.bodyparts:
            bodypart.draw(win)
    pass




