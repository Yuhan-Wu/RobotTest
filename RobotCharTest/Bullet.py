import pygame
import math
from RobotCharTest.AudioManager import AudioManager

class Bullet(pygame.sprite.Sprite):
    def __init__(self, path="square1.png", position=(100, 300)):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.initial_position = position
        self.velocity = (0, 0)
        self.initial_angle = 0
        self.rect.topleft = (-100, -100)
        self.visibility = False
        pass

    def set_position(self,new_position):
        self.rect[0]=new_position[0]
        self.rect[1]=new_position[1]
        pass

    def update_position(self, speed):
        self.rect[0]=self.rect[0]+self.velocity[0]*speed
        self.rect[1]=self.rect[1]+self.velocity[1]*speed
        pass

    def shoot(self, angle):
        self.initial_angle = angle
        self.reset()
        AudioManager.play("CowboyLaserSound.wav", 1)
        self.rect.topleft = self.initial_position
        self.velocity = (math.cos(math.radians(angle)), -math.sin(math.radians(angle)))
        self.visibility = True
        pass

    def reset(self):
        self.rect.topleft = 2000, 2000
        self.velocity = (0,0)
        self.visibility = False

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass