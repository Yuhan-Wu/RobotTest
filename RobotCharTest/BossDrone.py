from RobotCharTest.Drone import Drone
from RobotCharTest.BossHealthBar import BossHealthBar

class BossDrone(Drone):
    def __init__(self,path,position):
        super(BossDrone,self).__init__(path,position)
        self.health = 3
        self.isActive=False
        self.health_bar=BossHealthBar((position[0] - 20, position[1] - 50))
        pass