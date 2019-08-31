import pygame

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

    def move(self,delta):
        self.rect[1]+=delta
        pass
    




