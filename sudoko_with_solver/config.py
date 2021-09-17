import os

import pygame

pygame.init()
pygame.font.init()

os.environ["SDL_VIDEO_CENTERED"] = "1"  # center screen
font_time = pygame.font.SysFont("timesnewroman", 40)
font_small_number = pygame.font.SysFont("timesnewroman", 20)
font_big_number = pygame.font.SysFont("timesnewroman", 40)

CLOCK = pygame.time.Clock()
FPS = 60
WINDOW_SIZE = (540, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
WHITE = (255, 255, 255)
WINDOW.fill(WHITE)
pygame.display.set_caption("Sudoku")

BLACK = (0, 0, 0)
GREY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (230, 230, 230)
MIDDLE_GREY = (128, 128, 128)
GAP = 60
ROWS, COL = 9, 9
seconds_reset = 0
