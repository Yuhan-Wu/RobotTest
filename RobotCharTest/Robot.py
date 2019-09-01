import pygame

class Robot(object):
    def __init__(self,bodyparts):
        self.total_health=2
        self.bodyparts=bodyparts
        self.smash_sound='RobotSmash.wav'

    def decrease_health(self,bodyPart):
        self.total_health=self.total_health-bodyPart.damage
        return self.total_health<=0
        pass

    def draw(self,win):
        for bodypart in self.bodyparts:
            bodypart.draw(win)

    def sound(self):
        pygame.mixer.music.load(self.smash_sound)
        pygame.mixer.music.play(loops = 1, start = 0)
        pass

    def action(self,level):
        level.robot_action()
        pass

    # used for level 2
    def __move(self):
        pass