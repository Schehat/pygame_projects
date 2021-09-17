import pygame

import config


def timer():
    seconds = (pygame.time.get_ticks()) // 1000 - config.seconds_reset
    minutes = pygame.time.get_ticks() // 60000
    if seconds == 60:
        config.seconds_reset += seconds
        seconds = 0

    time = f"Time: {minutes}:{seconds:02}"
    text_time = config.font_time.render(time, 1, config.BLACK)
    config.WINDOW.blit(
        text_time,
        (
            config.WINDOW_SIZE[0] - text_time.get_width() - 10,
            config.WINDOW_SIZE[1] - text_time.get_height() - 5,
        ),
    )
