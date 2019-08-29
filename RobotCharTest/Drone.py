import pygame

class Drone(pygame.sprite.Sprite):
    def __init__(self, path, position):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.isActive = True
        pass

    def move(self, drone_speed):
        self.rect[0] = self.rect[0] - drone_speed
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pass