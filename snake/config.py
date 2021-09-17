import os

import pygame

pygame.init()
pygame.font.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"
font = pygame.font.SysFont("timesnewroman", 80)

CLOCK = pygame.time.Clock()
FPS = 60
WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
GREY = (50, 50, 50)
WINDOW.fill(GREY)
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GAP = 20
ROWS, COL = int(WINDOW_SIZE[0] / GAP), int(WINDOW_SIZE[1] / GAP)
