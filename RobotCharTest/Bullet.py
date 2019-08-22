import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,path="square1.png",position=(100,300)):
        self.image=pygame.image.load(path).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=position
        pass

    def update_position(self,value):
        self.rect[0]=self.rect[0]+value
        pass

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass