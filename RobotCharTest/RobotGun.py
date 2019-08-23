import pygame
from RobotCharTest.BodyPart import Body_Part

class RobotGun(Body_Part):
	def __init__(self,path="square1.png",position=(300,300)):
		super(RobotGun,self).__init__(path=path,position=position)
		self.damage=0
		self.image = pygame.image.load(path).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft=position
		self.shoot_sound='RobotLaserSound.wav'

	def sound(self):
		pygame.mixer.music.load(self.shoot_sound)
		pygame.mixer.music.play(loops = 1, start = 0)