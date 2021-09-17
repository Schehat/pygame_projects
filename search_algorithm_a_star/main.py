"""
    controls:
    - left mouse: set blocks
    - right mouse: remove blocks
    - space: start algorithm
    - c: clear grid
"""

import pygame

import utils
from config import FPS, GREY, WHITE, WINDOW, WINDOW_SIZE, clock


def draw(grid, rows):
    WINDOW.fill(WHITE)

    for i in grid:
        for j in i:
            j.draw()

    gap = int(WINDOW_SIZE[0] / rows)
    for i in range(rows):
        pygame.draw.line(
            WINDOW, GREY, (0, i * gap), (WINDOW_SIZE[0], i * gap)
        )  # horizontal
        for j in range(rows):
            pygame.draw.line(
                WINDOW,
                GREY,
                (j * gap, 0),
                (j * gap, WINDOW_SIZE[0]),
            )  # vertical

    pygame.display.update()


def main():
    rows = 50
    grid = utils.make_grid(rows)
    start = None
    end = None

    run = True
    algorithm_start = False
    while run:
        clock.tick(FPS)
        draw(grid, rows)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if pygame.mouse.get_pressed()[0]:  # left
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_position(rows, pos)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    node.make_start()

                elif not end and node != start:
                    end = node
                    node.make_end()

                elif node != start and node != end:
                    node.make_obstacle()

            elif pygame.mouse.get_pressed()[2]:  # right
                pos = pygame.mouse.get_pos()
                row, col = utils.get_clicked_position(rows, pos)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if pygame.key.get_pressed()[pygame.K_SPACE] and start and end:
                for i in grid:
                    for j in i:
                        j.update(grid)

                utils.algorithm(grid, start, end, rows)

            if pygame.key.get_pressed()[pygame.K_c] and not algorithm_start:
                start = None
                end = None
                grid = utils.make_grid(rows)


if __name__ == "__main__":
    main()
