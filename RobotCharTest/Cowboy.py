import pygame

class Cowboy (pygame.sprite.Sprite):
    def __init__(self,path="tangram-eagle.png",position=(90,300)):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(path).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.topleft=position

    def draw(self,win):
        win.blit(self.image,self.rect)
        pass

    def lose_sound(self):
        sound = 'CowboyDeathSound.wav'
        self.__play_sound(sound)
        pass

    def shoot_sound(self):
        sound='CowboyLaserSound.wav'
        self.__play_sound(sound)
        pass

    def __play_sound(self,sound):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops=1, start=0)
        pass