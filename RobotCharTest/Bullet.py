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

    def move(self, screen, angle, velocity):
        # CALCULATING THE PATH OF THE BULLET
        # print(angle)
        slope = 0
        intercept = 0
        angle = angle % 360
        # RIGHT ANGLES
        if angle == 0:
            self.rect[0] = self.rect[0] + velocity
        elif angle == 180:
            self.rect[0] = self.rect[0] - velocity
        elif angle == 90:
            self.rect[1] = self.rect[1] - velocity
        elif angle == 270:
            self.rect[1] = self.rect[1] + velocity
        # QUADRANT ANGLES
        else:
            slope = -(math.tan(math.radians(angle)))
            intercept = 400 - (300 * slope)
            if (angle > 0 and angle < 90) or (angle > 270 and angle < 360):
                self.rect[0] = self.rect[0] + velocity
            elif (angle > 180 and angle < 270) or (angle > 90 and angle < 180):
                self.rect[0] = self.rect[0] - velocity
            self.rect[1] = (slope * self.rect[0]) + intercept

        # CALCULATING THE PATH OF THE BULLET
        # self.rect[0] = self.rect[0] + velocity
        # self.rect[1] = -self.rect[0] * slope
        # self.rect = self.rect.move(x_movement, y_movement)

        # CHECKING FOR SCREEN TOUCH
        if self.rect[0] > 0 and self.rect[0] < screen.get_size()[0] - self.image.get_size()[0] and self.rect[1] > 0 and \
                self.rect[1] < screen.get_size()[1] - self.image.get_size()[1]:
            print(str(self.rect[0]) + "::" + str(self.rect[1]))
            screen.blit(self.image, self.rect)
            return True
            pass

        return False
        # BLIT THE IMAGE
        # print(str(self.rect[0]) + "::" + str(self.rect[1]))
        # screen.blit(self.image, self.rect)
        # pass

    def sound(self):
        # self.sound = 'CowboyLaserSound.wav'
        pygame.mixer.music.load('CowboyLaserSound.wav')
        pygame.mixer.music.play(loops = 1, start = 0)