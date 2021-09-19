import math
import operator
import random
from functools import reduce

import pygame

import config
import utils


class Buttons:
    def __init__(self, mouse, click):
        self.mouse = mouse
        self.click = click

    def button_draw(self):
        if (
            config.RECT_BLUE[0]
            < self.mouse[0]
            < config.RECT_BLUE[0] + config.RECT_BLUE[2]
            and config.RECT_BLUE[1]
            < self.mouse[1]
            < config.RECT_BLUE[1] + config.RECT_BLUE[3]
        ):
            pygame.draw.rect(config.WINDOW, config.HOVER_BLUE, config.RECT_BLUE)
            if self.click[0] == 1:
                # avoid spamming clicks
                seconds = pygame.time.get_ticks() // 1000
                if seconds > config.seconds_reset + 0.001:
                    config.seconds_reset = seconds
                    if len(config.numbers) == 0:
                        utils.make_numbers()
                    elif len(config.numbers) > 0:
                        config.numbers = []
        else:
            pygame.draw.rect(config.WINDOW, config.BLUE, config.RECT_BLUE)

        if (
            config.RECT_YELLOW[0]
            < self.mouse[0]
            < config.RECT_YELLOW[0] + config.RECT_YELLOW[2]
            and config.RECT_YELLOW[1]
            < self.mouse[1]
            < config.RECT_YELLOW[1] + config.RECT_YELLOW[3]
        ):
            pygame.draw.rect(config.WINDOW, config.HOVER_YELLOW, config.RECT_YELLOW)
            if self.click[0] == 1:
                seconds = pygame.time.get_ticks() // 1000
                if seconds > config.seconds_reset + 0.2:
                    config.seconds_reset = seconds
                    utils.do_parity_check()
        else:
            pygame.draw.rect(config.WINDOW, config.YELLOW, config.RECT_YELLOW)

        if (
            config.RECT_RED[0] < self.mouse[0] < config.RECT_RED[0] + config.RECT_RED[2]
            and config.RECT_RED[1]
            < self.mouse[1]
            < config.RECT_RED[1] + config.RECT_RED[3]
        ):
            pygame.draw.rect(config.WINDOW, config.HOVER_RED, config.RECT_RED)
            if self.click[0] == 1:
                seconds = pygame.time.get_ticks() // 1000
                if seconds > config.seconds_reset + 0.2:
                    config.seconds_reset = seconds
                    ran = random.randint(3, 63)  # no need to take 0, 1, 2
                    while math.log2(ran).is_integer():
                        ran = random.randint(3, 63)
                    if (
                        config.do_error
                        and not config.do_parity
                        and len(config.numbers) > 0
                    ):
                        config.do_error = False
                        if config.numbers[ran][1] == 1:
                            config.numbers[ran][1] = 0
                            text_number = config.font_text.render(
                                str(config.numbers[ran][1]), 1, config.WHITE, config.RED
                            )
                            x, y, _, _ = config.rects[ran]
                            config.WINDOW.blit(text_number, (x, y))
                        else:
                            config.numbers[ran][1] = 1
                            text_number = config.font_text.render(
                                str(config.numbers[ran][1]), 1, config.WHITE, config.RED
                            )
                            x, y, _, _ = config.rects[ran]
                            config.WINDOW.blit(text_number, (x, y))
                            pygame.display.update()
        else:
            pygame.draw.rect(config.WINDOW, config.RED, config.RECT_RED)

        if (
            config.RECT_GREEN[0]
            < self.mouse[0]
            < config.RECT_GREEN[0] + config.RECT_GREEN[2]
            and config.RECT_GREEN[1]
            < self.mouse[1]
            < config.RECT_GREEN[1] + config.RECT_GREEN[3]
        ):
            pygame.draw.rect(config.WINDOW, config.HOVER_GREEN, config.RECT_GREEN)
            if self.click[0] == 1:
                seconds = pygame.time.get_ticks() // 1000
                if seconds > config.seconds_reset + 0.2:
                    config.seconds_reset = seconds
                    count = 0
                    if (
                        config.do_detection
                        and not config.do_parity
                        and not config.do_error
                    ):
                        config.do_detection = False
                        for i in config.numbers:
                            if i[1] == 1:
                                config.ones.append(i[0])
                                count += 1
                                text_number = config.font_binary.render(
                                    str(bin(i[0])[2:]), 1, config.WHITE
                                )
                                config.WINDOW.blit(
                                    text_number,
                                    (config.WINDOW_SIZE[0] - 120, 90 + 12 * count),
                                )
                                pygame.display.update()

                        text_number = config.font_binary.render(
                            "----------------", 1, config.RED
                        )
                        config.WINDOW.blit(
                            text_number,
                            (config.WINDOW_SIZE[0] - 130, 90 + 12 * (count + 1)),
                        )
                        text_number = config.font_binary.render(
                            f"XOR: {str(bin(reduce(operator.xor, [i for i in config.ones]))[2:])}",
                            1,
                            config.RED,
                        )
                        config.WINDOW.blit(
                            text_number,
                            (config.WINDOW_SIZE[0] - 130, 90 + 12 * (count + 2)),
                        )
                        config.ones = []
        else:
            pygame.draw.rect(config.WINDOW, config.GREEN, config.RECT_GREEN)

    @staticmethod
    def button_text(rect, text):
        text_output = config.font_button.render(text, True, config.BLACK)
        text_rect = text_output.get_rect()
        text_rect.center = (rect[0] + int((rect[2] / 2)), rect[1] + int((rect[3] / 2)))
        config.WINDOW.blit(text_output, text_rect)
