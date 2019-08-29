import pygame

from RobotCharTest.HealthBar import HealthBar

class Drone(pygame.sprite.Sprite):
    def __init__(self, path, position):
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.initial_position = position
        self.rect.topleft = position
        self.velocity = (0, 0)
        self.isActive = True
        self.health = 2
        self.health_bar = HealthBar((position[0] - 20, position[1] - 50))
        pass

    def update_position(self, speed):
        self.rect[0] = self.rect[0] + self.velocity[0] * speed
        self.rect[1] = self.rect[1] + self.velocity[1] * speed
        self.health_bar.update_position((self.velocity[0] * speed, self.velocity[1] * speed))
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.health_bar.draw(screen, self.health)
        pass

    def damage(self, value):
        self.health += value
        if self.health <= 0:
            self.reset()
            return True
        return False

    def reset(self):
        self.rect.topleft = self.initial_position
        self.health_bar.rect.topleft = (self.rect.topleft[0] - 20, self.rect.topleft[1] - 50)
        self.health = 2
        #self.velocity = (0, 0)