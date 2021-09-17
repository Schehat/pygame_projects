from queue import PriorityQueue

import pygame

from config import GREY, RED, WHITE, WINDOW, WINDOW_SIZE, font
from node import Node


# horizontal and vertical distance of both nodes
def h(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    return abs(x2 - x1) + abs(y2 - y1)


def reconstruct_path(came_from, end, grid, rows):
    while end in came_from:
        end = came_from[end]
        end.make_path()
        draw(grid, rows)


def algorithm(grid, start, end, rows):
    count = 0  # needed to sort nodes with same f score
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}  # needed to make the shortest path
    g_score = {node: float("inf") for i in grid for node in i}
    g_score[start] = 0
    f_score = {node: float("inf") for i in grid for node in i}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, grid, rows)
            end.make_end()  # end node keeps his color same for start
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(
                    neighbor.get_pos(), end.get_pos()
                )

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_opened()

        draw(grid, rows)

        if current != start:
            current.make_closed()

    # no path
    if current != end:
        draw_text()


def draw_text():
    text = font.render("No Path Found", 1, RED)
    WINDOW.blit(text, (int(WINDOW_SIZE[0] / 2 - text.get_width() / 2), 100))
    pygame.display.update()
    pygame.time.delay(2000)


def make_grid(rows):
    grid = []
    gap = WINDOW_SIZE[0] // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


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


def get_clicked_position(rows, pos):
    gap = WINDOW_SIZE[0] / rows
    x, y = pos

    row = int(y / gap)
    col = int(x / gap)

    return row, col
