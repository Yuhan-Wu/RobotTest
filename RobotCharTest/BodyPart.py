import pygame
from pygame.locals import BLEND_ADD

class Body_Part(pygame.sprite.Sprite):
    def __init__(self,path="square1.png",position=(300,300)):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=position
        self.damage=0
        pass

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass

    # def __init__(self,path,position):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.bodypart=pygame.image.load(path)
    #     self.postition=position
        pass
    




