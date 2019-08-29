import pygame
class AudioManager(object):
    @staticmethod
    def play(path="RobotSmash.wav", loops=1):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops, start = 0)
        pass