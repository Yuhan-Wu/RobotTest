class AmmoManager(object):

    def __init__(self):
        self.ammo_capacity = 2
        self.ammo = self.ammo_capacity
        self.reloading_time = 1000
        self.reloading_timer = self.reloading_time
        self.reloading = False

    def try_shoot(self):
        if self.reloading:
            print("Reloading")
            return False
        else:
            self.ammo -= 1
            if self.ammo <= 0:
                self.reloading = True
            return True

    def get_ammo_index(self):
        return self.ammo - 1

    # Called in the main loop, reloading
    def update_reload(self, delta_time=50):
        if self.reloading:
            self.reloading_timer -= delta_time
            if self.reloading_timer <= 0:
                self.reloading_timer = self.reloading_time
                self.ammo = self.ammo_capacity
                self.reloading = False

