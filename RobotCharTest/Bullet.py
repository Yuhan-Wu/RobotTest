import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self,path="square1.png",position=(100,300)):
        self.image=pygame.image.load(path).convert_alpha()
        self.rect=self.image.get_rect()
        self.initial_position=position
        self.velocity=(0, 0)
        self.initial_angle=0
        self.rect.topleft=position
        self.visibility = False
        pass

    def update_position(self, speed):
        self.rect[0]=self.rect[0]+self.velocity[0]*speed
        self.rect[1]=self.rect[1]+self.velocity[1]*speed
        pass

    def shoot(self, angle):
        self.initial_angle = angle
        self.reset()
        self.rect.topleft = self.initial_position
        self.velocity = (math.cos(math.radians(angle)), -math.sin(math.radians(angle)))
        self.visibility = True
        pass

    def reset(self):
        self.rect.topleft = 2000, 2000
        self.velocity = (0,0)
        self.sound()

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass

    def sound(self):
        # self.sound = 'CowboyLaserSound.wav'
        pygame.mixer.music.load('CowboyLaserSound.wav')
        pygame.mixer.music.play(loops = 1, start = 0)