import pygame

from RobotCharTest.HealthBar import HealthBar

class Drone(pygame.sprite.Sprite):
    def __init__(self, path, position):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.isActive = True
        self.health_bar = HealthBar(position)
        pass

    def move(self, drone_speed):
        self.rect[0] = self.rect[0] - drone_speed
        self.health_bar.update_position((-drone_speed, 0))
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.health_bar.draw(screen, 3)
        pass