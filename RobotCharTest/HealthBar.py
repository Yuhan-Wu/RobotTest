import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, position=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.health_full = pygame.image.load("healthybar_full_v1.png").convert_alpha()
        self.health_half = pygame.image.load("healthybar_half_v1.png").convert_alpha()
        self.health_empty = pygame.image.load("healthybar_empty_v1.png").convert_alpha()
        self.rect=self.health_full.get_rect()
        self.rect.topleft=position
        pass

    def update_position(self, velocity=(0,0)):
        self.rect[0]=self.rect[0]+velocity[0]
        self.rect[1]=self.rect[1]+velocity[1]
        pass

    def draw(self,win, health):
        if health >= 2:
            win.blit(self.health_full, self.rect)
        elif health == 1:
            win.blit(self.health_half, self.rect)
        else:
            win.blit(self.health_empty, self.rect)
        pass