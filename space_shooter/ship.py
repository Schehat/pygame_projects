import config
from laser import Laser


class Ship:
    COOLDOWN = 20

    def __init__(self, x, y, health=100, v=3):
        self.x = x
        self.y = y
        self.health = health
        self.v = v
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self):
        config.WINDOW.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw()

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
            config.sound_laser.play()

    def move_laser(self, player):
        self.cooldown()
        for laser in self.lasers:
            laser.move(laser.v // 2)
            if laser.off_screen():
                self.lasers.remove(laser)
            elif laser.collision(player, laser):
                player.health -= 10
                config.sound_hit.play()
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()
