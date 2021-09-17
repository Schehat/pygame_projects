import math
import os

import pygame

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()

font_title = pygame.font.SysFont("timesnewroman", 40)
font_button = pygame.font.SysFont("timesnewroman", 18)
font_text = pygame.font.SysFont("timesnewroman", 20)
font_binary = pygame.font.SysFont("timesnewroman", 12)

CLOCK = pygame.time.Clock()
FPS = 60
WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hamming Code Error Detection")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 96, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
HOVER_BLUE = (0, 41, 200)
HOVER_YELLOW = (200, 200, 0)
HOVER_RED = (200, 0, 0)
HOVER_GREEN = (0, 200, 0)
RECT_BLUE = (50, 450, 160, 60)
RECT_YELLOW = (230, 450, 160, 60)
RECT_RED = (50, 530, 160, 60)
RECT_GREEN = (230, 530, 160, 60)

ROWS, COLS = 8, 8
GAP = 40
n_power = int(math.log2(ROWS * COLS))

rects = []
numbers = []
ones = []

ran = None
seconds_reset = 0

# check to avoid multiple checks and to assure correct order of actions
do_parity = True
do_error = True
do_detection = False
