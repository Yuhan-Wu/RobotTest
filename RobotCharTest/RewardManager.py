import pygame

class RewardManager(object):
    def __init__(self, reward_cost=5, last_time=5, position=(0,0)):
        self.reward_cost = reward_cost
        self.score_counter = 0
        self.position = position
        self.buffing = False
        self.multiplier = 2
        self.timer = 0
        self.last_time = last_time
        # UI
        self.font = pygame.font.SysFont("Arial", 72)
        self.content = "Damage Multiply: X" + str(self.multiplier)
        self.text = self.font.render(self.content, True, (255, 0, 0))

    def add(self):
        if self.buffing:
            return
        self.score_counter += 1
        if self.score_counter >= self.reward_cost:
            self.score_counter = 0
            self.buffing = True

    def get_damage(self, value):
        if self.buffing:
            return value * self.multiplier
        else:
            return value

    def update(self, delta_time):
        if not self.buffing:
            return
        self.timer += delta_time
        if self.timer >= self.last_time:
            self.timer = 0
            self.buffing = False

    def draw(self, screen):
        if not self.buffing:
            return
        screen.blit(self.text, (self.position[0] - self.text.get_width() / 2, self.position[1]))