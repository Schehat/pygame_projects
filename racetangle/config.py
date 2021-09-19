# centers the window
import os

import pygame

os.chdir(os.path.dirname(__file__))

# has to be written before pygame initializes to center the screen
os.environ["SDL_VIDEO_CENTERED"] = "1"
# initialise all modules of pygame
pygame.init()

# deceleration of constant variables
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
HOVER_RED = (255, 0, 0)
HOVER_GREEN = (0, 255, 0)
HOVER_BLUE = (0, 0, 255)
CAR_WIDTH = 70
CAR_HEIGHT = 120
BARREL_HEIGHT = 106
BARREL_WIDTH = 61
ROAD_HEIGHT = 600
OBSTACLES_NUMBER = 2
RECT_GREEN = (500, 350, 150, 50)
RECT_RED = (150, 350, 150, 50)
RECT_INFO = (325, 450, 150, 50)
paused = True

# defining the display - parameters as a tuple
game_display = pygame.display.set_mode(DISPLAY_SIZE)
# window title
pygame.display.set_caption(os.path.join("assets", "Roadtangle"))
# matters for frame per second
clock = pygame.time.Clock()

# load and display images
car_img = pygame.image.load(os.path.join("assets", "racing_car.png"))
car_img.set_colorkey(WHITE)
car_img.convert_alpha()
car_icon = pygame.image.load(os.path.join("assets", "racing_car_icon.png"))
barrel_img = pygame.image.load(os.path.join("assets", "barrel.png"))
barrel_img.set_colorkey(WHITE)
barrel_img.convert_alpha()
# converts the format and can process faster
road1_img = pygame.image.load(os.path.join("assets", "road1.png")).convert()
road2_img = pygame.image.load(os.path.join("assets", "road2.png")).convert()

# icon
pygame.display.set_icon(car_icon)

# sound and music
crash_sound = pygame.mixer.Sound(os.path.join("assets", "car_crash.wav"))
back_music = pygame.mixer.music.load(
    os.path.join("assets", "spy_music_by_Nicole_Marie_T.wav")
)
