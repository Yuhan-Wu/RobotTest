import pygame
from pygame.locals import BLEND_ADD

class Body_Part(pygame.sprite.Sprite):
    def __init__(self,damage=0,path="square1.png",position=(300,300)):
        pygame.sprite.Sprite.__init__(self)
        self.original_image=pygame.image.load(path).convert_alpha()
        self.image=self.original_image
        self.rect=self.image.get_rect()
        self.rect.topleft=position
        self.damage=damage
        self.angle = 0
        pass

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass

    def set_center(self, center=(0,0)):
        x,y = self.rect.center
        self.rect.center = (x+center[0], y+center[1])

    def rotate(self, angle=0, stop_angle=0):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        if abs(self.angle-stop_angle) < 5:
            return False
        self.angle += angle
        self.angle %= 360
        print(self.angle)
        x, y = self.rect.center  # Save its current center.
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.
        return True

    # def __init__(self,path,position):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.bodypart=pygame.image.load(path)
    #     self.postition=position
        pass
    




