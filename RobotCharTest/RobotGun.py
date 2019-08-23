import pygame
pygame.init()

class RobotGun(Robot_Gun):
	def __init__(self):
		self.image = pygame.image.load('RobotGun').convert_alpha()
		self.rect = self.image.get_rect()

	def sound(self):
		self.sound = 'RobotLaserSound.wav'
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(loops = 1, start = 0)