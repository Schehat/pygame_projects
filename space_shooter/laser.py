import pygame

import config


class Laser:
    def __init__(self, x, y, img, v=10):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.v = v

    def draw(self):
        config.WINDOW.blit(self.img, (self.x, self.y - 30))

    def move(self, v):
        self.y += v

    def off_screen(self):
        return self.y >= config.WINDOW_SIZE[1] or self.y <= 0

    @staticmethod
    def collision(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None
