import os

import pygame

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("timesnewroman", 50)
os.environ["SDL_VIDEO_CENTERED"] = "1"
clock = pygame.time.Clock()
FPS = 60

WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("A* Star Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
