import os

import pygame

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()

font_text = pygame.font.SysFont("timesnewroman", 40)

WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREY = (252, 252, 252)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

ROWS, COLS = 3, 3
grid_list = [["" for _ in range(COLS)] for _ in range(ROWS)]

GAP = 50

players = ["X", "O"]
current_player = players[0]
draw_text = []
