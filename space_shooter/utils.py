import pygame

import config


def check_quit_button(rect, mouse, click):
    if check_button(rect, mouse):
        pygame.draw.rect(config.WINDOW, config.HOVER_RED, config.RECT_RED)
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(config.WINDOW, config.RED, config.RECT_RED)


def check_button(rect, mouse):
    return (
        rect[0] < mouse[0] < rect[0] + rect[2]
        and rect[1] < mouse[1] < rect[1] + rect[3]
    )


def draw_button_text(rect, text):
    text_output = config.font_button.render(text, True, config.WHITE)
    text_rect = text_output.get_rect()
    text_rect.center = (rect[0] + int((rect[2] / 2)), rect[1] + int((rect[3] / 2)))
    config.WINDOW.blit(text_output, text_rect)


def draw_info_text(text):
    text_output_arrows = config.font_button.render(text, True, config.WHITE)
    text_rect_arrows = text_output_arrows.get_rect()
    text_rect_arrows.center = (int(config.WINDOW_SIZE[0] / 2), 200)
    config.WINDOW.blit(text_output_arrows, text_rect_arrows)
