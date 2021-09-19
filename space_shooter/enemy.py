import random

import pygame

import config
from laser import Laser
from ship import Ship


class Enemy(Ship):
    COLOR_MAP = {
        "red": (config.ENEMY_RED_SHIP, config.RED_LASER),
        "blue": (config.ENEMY_BLUE_SHIP, config.BLUE_LASER),
        "green": (config.ENEMY_GREEN_SHIP, config.GREEN_LASER),
    }

    wave_length = 0

    def __init__(self, x, y, color, health=100, v=3):
        super().__init__(x, y, health, v)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self):
        self.y += self.v

    def check(self, player, enemy, enemies):
        # enemy off the screen
        if Laser.collision(enemy, player):
            player.health -= 10
            config.sound_crash.play()
            enemies.remove(enemy)

        if self.y + self.get_height() >= config.WINDOW_SIZE[1]:
            player.lives -= 1
            enemies.remove(enemy)

        # no enemies left => next level
        # if len(enemies) == 0:
        #     self.v += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 10, self.y + 50, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    @staticmethod
    def create_enemy(player, enemies):
        if len(enemies) == 0:
            player.level += 1
            Enemy.wave_length += 3
            while len(enemies) < Enemy.wave_length:
                enemy = Enemy(
                    random.randrange(50, config.WINDOW_SIZE[0] - 50),
                    random.randrange(-1500, -50),
                    random.choice(["red", "blue", "green"]),
                )
                enemies.append(enemy)
                if len(enemies) > 1:
                    # -2 for correct indexing not including last element
                    count = len(enemies) - 2
                    for i in range(0, count):
                        if (
                            enemies[i].x
                            <= enemy.x
                            <= enemies[i].x + enemies[i].get_width()
                            or enemies[i].x
                            <= enemy.x + enemy.get_width()
                            <= enemies[i].x + enemies[i].get_width()
                        ):
                            if (
                                enemies[i].y
                                <= enemy.y
                                <= enemies[i].y + enemies[i].get_height()
                                or enemies[i].y
                                <= enemy.y + enemy.get_height()
                                <= enemies[i].y + enemies[i].get_height()
                            ):
                                # idk why -1: count does nothing in this loop except
                                # to set the range which is set
                                count -= 1
                                enemies.pop(-1)
