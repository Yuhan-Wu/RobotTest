import pygame
from RobotCharTest.BodyPart import Body_Part

class RobotGun(Body_Part):
	def __init__(self,path="square1.png",position=(300,300)):
		super(RobotGun,self).__init__(path=path,position=position)
		self.damage=0
		self.image = pygame.image.load(path).convert_alpha()
		self.original_image=self.image
		self.rect = self.image.get_rect()
		self.rect.topleft=position
		self.shoot_sound='RobotLaserSound.wav'
		self.angle=0

	def sound(self):
		pygame.mixer.music.load(self.shoot_sound)
		pygame.mixer.music.play(loops = 1, start = 0)

	def rotate(self, angle=0, stop_angle=0):
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		if abs(self.angle - stop_angle) < 5:
			return False
		self.angle += angle
		self.angle %= 360
		x, y = self.rect.center  # Save its current center.
		self.rect = self.image.get_rect()  # Replace old rect with new rect.
		self.rect.center = (x, y)  # Put the new rect's center at old center.
		return True