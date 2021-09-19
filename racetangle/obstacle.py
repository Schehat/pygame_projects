import random

from config import (
    BARREL_HEIGHT,
    BARREL_WIDTH,
    DISPLAY_HEIGHT,
    DISPLAY_WIDTH,
    OBSTACLES_NUMBER,
    barrel_img,
    game_display,
)


class Obstacles:
    def __init__(self, ob_x, ob_y, ob_speed):
        self.ob_x = ob_x
        self.ob_y = ob_y
        self.ob_speed = ob_speed

    def draw(self):
        game_display.blit(barrel_img, (self.ob_x, self.ob_y))

    def move(self):
        self.ob_y += self.ob_speed
        return self.ob_y

    def set_random(self):
        if self.ob_y > DISPLAY_HEIGHT:
            obstacles = list()
            for _ in range(OBSTACLES_NUMBER):
                obstacles.append(
                    Obstacles(
                        random.randrange(0, DISPLAY_WIDTH),
                        random.randrange(-1000, -600),
                        random.randrange(5, 10),
                    )
                )
            self.ob_y = 0 - BARREL_HEIGHT
            self.ob_x = random.randrange(0, DISPLAY_WIDTH - BARREL_WIDTH)
