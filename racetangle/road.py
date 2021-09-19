from config import DISPLAY_HEIGHT, game_display


class Road:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, img):
        game_display.blit(img, (self.x, self.y))

    def move(self):
        self.y += 7
        if self.y > DISPLAY_HEIGHT:
            self.y = -588
        # scrolling picture in bad
