import os

import pygame

os.chdir(os.path.dirname(__file__))

os.environ["SDL_VIDEO_CENTERED"] = "1"  # center screen
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# define fonts
font = pygame.font.SysFont("comicsans", 50)
font_screen = pygame.font.Font("freesansbold.ttf", 80)
font_button = pygame.font.Font("freesansbold.ttf", 20)

# declare constants
WINDOW_SIZE = (800, 600)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Space Shooter")
FPS = 60
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
HOVER_RED = (255, 0, 0)
HOVER_GREEN = (0, 255, 0)
HOVER_BLUE = (0, 0, 255)
RECT_GREEN = (500, 350, 150, 50)
RECT_RED = (150, 350, 150, 50)
RECT_INFO = (325, 450, 150, 50)

# load images
ENEMY_RED_SHIP = pygame.image.load(
    os.path.join("assets", "enemyRed3.png")
)  # or assets/enemy...
ENEMY_BLUE_SHIP = pygame.image.load(os.path.join("assets", "enemyBlue3.png"))
ENEMY_GREEN_SHIP = pygame.image.load(os.path.join("assets", "enemyGreen3.png"))

# player
PLAYER_RED_SHIP = pygame.image.load(
    os.path.join("assets", "playerShip2_red.png")
)
PLAYER_SIZE = (100, 67)

# laser
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png")
)

# background
BACKGROUND = pygame.image.load(os.path.join("assets", "background.png"))

# sound
sound_laser = pygame.mixer.Sound(os.path.join("assets", "laser.wav"))
sound_hit = pygame.mixer.Sound(os.path.join("assets", "hit.wav"))
sound_crash = pygame.mixer.Sound(os.path.join("assets", "crash.wav"))

paused = True
