import pygame

from config import BLACK, GREEN, ORANGE, PURPLE, RED, TURQUOISE, WHITE, WINDOW


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_obstacle(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_opened(self):
        self.color = GREEN

    def make_obstacle(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self):
        pygame.draw.rect(
            WINDOW, self.color, (self.x, self.y, self.width, self.width)
        )

    def update(self, grid):
        self.neighbors = []

        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].is_obstacle()
        ):  # down
            self.neighbors.append(grid[self.row + 1][self.col])

        if (
            self.row > 0 and not grid[self.row - 1][self.col].is_obstacle()
        ):  # up
            self.neighbors.append(grid[self.row - 1][self.col])

        if (
            self.col > 0 and not grid[self.row][self.col - 1].is_obstacle()
        ):  # left
            self.neighbors.append(grid[self.row][self.col - 1])

        if (
            self.col < self.total_rows - 1
            and not grid[self.row][self.col + 1].is_obstacle()
        ):  # right
            self.neighbors.append(grid[self.row][self.col + 1])
