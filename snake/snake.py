import random

import pygame

from config import BLACK, COL, GAP, RED, ROWS, WHITE, WINDOW, WINDOW_SIZE, font


class Snake:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.ran = random.randrange(4)
        if self.ran == 0:
            self.v_x = v
            self.v_y = 0
        elif self.ran == 1:
            self.v_x = -v
            self.v_y = 0
        elif self.ran == 2:
            self.v_y = v
            self.v_x = 0
        else:
            self.v_y = -v
            self.v_x = 0
        self.height = GAP
        self.width = GAP
        self.move_counter = 0
        self.tail = [[]]
        self.total = 0

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] and self.v_x != self.v:
            self.v_x = -self.v
            self.v_y = 0
        elif keys_pressed[pygame.K_d] and self.v_x != -self.v:
            self.v_x = self.v
            self.v_y = 0
        elif keys_pressed[pygame.K_w] and self.v_y != self.v:
            self.v_y = -self.v
            self.v_x = 0
        elif keys_pressed[pygame.K_s] and self.v_y != -self.v:
            self.v_y = self.v
            self.v_x = 0

        # tail

        if self.move_counter == 10:
            self.move_counter = 0

        self.tail[self.total] = self.x, self.y
        if self.total > 0 and self.move_counter == 0:
            for i in range(self.total):
                self.tail[i] = self.tail[i + 1]

        if self.move_counter == 0:
            self.x += self.v_x
            self.y += self.v_y

        self.move_counter += 1

    def draw(self):
        pygame.draw.rect(WINDOW, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(WINDOW, BLACK, (self.x, self.y, self.width, self.height), 1)
        if self.total > 0:
            for i in range(self.total):
                pygame.draw.rect(
                    WINDOW, WHITE, (self.tail[i][0], self.tail[i][1], GAP, GAP)
                )
                pygame.draw.rect(
                    WINDOW,
                    BLACK,
                    (self.tail[i][0], self.tail[i][1], GAP, GAP),
                    1,
                )

    def get_pos(self):
        s_col, s_row = int(self.x / GAP), int(self.y / GAP)
        return s_col, s_row

    def check(self, food):
        # collision
        col, row = self.get_pos()
        if (
            col == int(WINDOW_SIZE[0] / GAP)
            or col - 1 == -2
            or row == int(WINDOW_SIZE[1] / GAP)
            or row - 1 == -2
        ):
            # reposition snake for game over screen for being able to see
            if self.x > 0 and 0 < self.y < WINDOW_SIZE[1]:
                self.x = WINDOW_SIZE[0] - GAP
            elif self.x < 0 and 0 < self.y < WINDOW_SIZE[1]:
                self.x = 0
            elif self.y > 0 and 0 < self.x < WINDOW_SIZE[0]:
                self.y = WINDOW_SIZE[1] - GAP
            else:
                self.y = 0

            self.game_over(food)

        for i in range(self.total):
            if self.tail[i][0] == self.x and self.tail[i][1] == self.y:
                self.game_over(food)
                break

    def game_over(self, food):
        food.draw()
        self.draw()
        text = font.render("GAME OVER", 1, RED)
        WINDOW.blit(text, (int(WINDOW_SIZE[0] / 2 - text.get_width() / 2), 200))
        pygame.display.update()
        pygame.time.delay(2000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # relocate
        self.total = 0
        self.tail = [[]]
        self.x = random.randrange(6, COL - 5) * GAP
        self.y = random.randrange(6, ROWS - 5) * GAP
        food.spawn()
