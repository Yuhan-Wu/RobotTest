import pygame

class Cowboy (pygame.sprite.Sprite):
    def __init__(self,path="",position=(90,300)):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path)
        self.rect=self.image.get_rect().convert_alpha()
        self.rect.topleft=position

    def sound(self):
        self.sound = 'CowboyDeathSound.wav'
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(loops = 1, start = 0)
        pass