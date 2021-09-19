import random

import pygame

from config import COL, GAP, RED, ROWS, WINDOW


class Food:
    def __init__(self):
        self.x = None
        self.y = None

    def spawn(self):
        self.x = random.randrange(COL) * GAP
        self.y = random.randrange(ROWS) * GAP

    def draw(self):
        pygame.draw.rect(WINDOW, RED, (self.x, self.y, GAP, GAP))

    def get_pos(self):
        f_col, f_row = int(self.x / GAP), int(self.y / GAP)
        return f_col, f_row
