import math
import random

import pygame

import config


def make_numbers():
    config.do_parity = True
    config.do_error = True
    config.do_detection = True
    for i in range(0, config.ROWS * config.COLS):
        if i == 0:
            config.numbers.append([i, ""])
        elif not math.log2(i).is_integer():
            config.numbers.append([i, random.randint(0, 1)])
        else:
            config.numbers.append([i, ""])
    config.WINDOW.fill(config.BLACK)
    for i in config.numbers:
        text_number = config.font_text.render(str(i[1]), 1, config.WHITE)
        text_binary = config.font_binary.render(str(bin(i[0])[2:]), 1, config.WHITE)
        x, y, _, _ = config.rects[i[0]]
        config.WINDOW.blit(text_number, (x, y))
        config.WINDOW.blit(text_binary, (x, y + 27))
        pygame.display.update()


def do_parity_check():
    j = 0
    if config.do_parity and len(config.numbers) > 0:
        config.do_parity = False
        # to avoid errors will change parity after this
        config.numbers[0][1] = 0
        # fill the parity digits (2^n) correctly
        for x in range(config.n_power):
            j = 0
            for i in config.numbers:
                try:
                    if str(bin(i[0])[2:][-(x + 1)]) == str(1):
                        if i[1] == 1:
                            j += 1
                except IndexError:
                    pass
            if j % 2 == 0:
                config.numbers[2 ** x][1] = 0
            else:
                config.numbers[2 ** x][1] = 1

        # check if we have even 1 digits for the first parity figure
        for i in config.numbers:
            if str(i[1]) == str(1):
                j += 1
        if j % 2 == 0:
            config.numbers[0][1] = 0
        else:
            config.numbers[0][1] = 1

        for i in config.numbers:
            if i[0] == 0:
                text_number = config.font_text.render(
                    str(i[1]), 1, config.BLACK, config.YELLOW
                )
                x, y, _, _ = config.rects[i[0]]
                config.WINDOW.blit(text_number, (x, y))
                pygame.display.update()
            if i[1] != "":
                try:
                    if math.log2(i[0]).is_integer():
                        text_number = config.font_text.render(
                            str(i[1]), 1, config.BLACK, config.YELLOW
                        )
                        x, y, _, _ = config.rects[i[0]]
                        config.WINDOW.blit(text_number, (x, y))
                        pygame.display.update()
                except ValueError:
                    pass


def make_grid():
    for i in range(config.ROWS):
        for j in range(config.COLS):
            config.rects.append(
                [j * config.GAP + 55, i * config.GAP + 105, config.GAP, config.GAP]
            )


def draw_text():
    text_title = config.font_title.render("Binary Search", 1, config.YELLOW)
    config.WINDOW.blit(
        text_title,
        (
            int(config.WINDOW_SIZE[0] / 2 - text_title.get_width() / 2),
            int(text_title.get_height()),
        ),
    )
