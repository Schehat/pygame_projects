"""
    controls:
    - w, a, s, d: move
"""
import random

import pygame

from config import CLOCK, COL, FPS, GAP, GREY, ROWS, WHITE, WINDOW, WINDOW_SIZE
from food import Food
from snake import Snake


def eat(snake, food):
    if snake.get_pos() == food.get_pos():
        food.spawn()
        snake.total += 1
        snake.tail.append([snake.x, snake.y])


def make_grid():
    grid = list()
    for i in range(ROWS):
        for j in range(COL):
            grid.append(pygame.draw.rect(WINDOW, GREY, (i * GAP, j * GAP, GAP, GAP)))

    for i in range(ROWS):
        pygame.draw.line(
            WINDOW, WHITE, (0, i * GAP), (WINDOW_SIZE[0], i * GAP)
        )  # horizontal
        for j in range(COL):
            pygame.draw.line(
                WINDOW, WHITE, (j * GAP, 0), (j * GAP, WINDOW_SIZE[1])
            )  # vertical


def draw(snake, food):
    WINDOW.fill(GREY)
    make_grid()
    eat(snake, food)
    snake.check(food)
    snake.move()
    food.draw()
    snake.draw()
    pygame.display.update()


def main():
    run = True
    x_snake = random.randrange(6, COL - 5) * GAP
    y_snake = random.randrange(6, ROWS - 5) * GAP
    snake = Snake(x_snake, y_snake, GAP)
    food = Food()
    food.spawn()
    make_grid()

    while run:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw(snake, food)
        pygame.display.update()


if __name__ == "__main__":
    main()
