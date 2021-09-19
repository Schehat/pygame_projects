"""
    controls:
    - left mouse: select cell
    - digit keys: select a digit
    - space: enter digit
    - right click: reset entered digit e.g. digit is wrong
    - s: solve sudoku
"""

# method to avoid spamming key presses without making a delay would be nice
import pygame

import config
from get_timer import timer
from grid import Grid


def draw(board):
    config.WINDOW.fill(config.WHITE)
    board.control()
    timer()
    board.draw_board()
    board.solve()
    pygame.display.update()


def main():
    run = True
    board = Grid(config.ROWS, config.COL, config.WINDOW_SIZE[0], config.WINDOW_SIZE[1])

    while run:
        config.CLOCK.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        draw(board)


if __name__ == "__main__":
    main()
