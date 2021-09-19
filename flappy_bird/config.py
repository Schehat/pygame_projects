import os

import pygame

os.chdir(os.path.dirname(__file__))

pygame.init()
pygame.font.init()
font_score = pygame.font.SysFont("timesnewroman", 40)
font_gameover = pygame.font.SysFont("timesnewroman", 100)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
os.environ["SDL_VIDEO_CENTERED"] = "1"

WINDOW_SIZE = (600, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()
FPS = 30

BIRD_IMGS = [
    pygame.image.load(os.path.join("assets", "bird1.png")),
    pygame.image.load(os.path.join("assets", "bird2.png")),
    pygame.image.load(os.path.join("assets", "bird3.png")),
]
PIPE_IMG = pygame.image.load(os.path.join("assets", "pipe.png"))
BG_IMG = pygame.image.load(os.path.join("assets", "bg.png"))
BASE_IMG = pygame.image.load(os.path.join("assets", "base.png"))
