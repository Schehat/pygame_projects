import pygame

import config
import utils
from buttons import Buttons


def create_buttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    buttons = Buttons(mouse, click)
    return buttons


def draw(buttons):
    for i in config.rects:
        x, y, w, h = i
        pygame.draw.rect(config.WINDOW, config.WHITE, (x, y, w, h), 1)

    buttons.button_draw()
    buttons.button_text(config.RECT_BLUE, "1. Generate Numbers")
    buttons.button_text(config.RECT_YELLOW, "2. Parity Check")
    buttons.button_text(config.RECT_RED, "3. Generate Error")
    buttons.button_text(config.RECT_GREEN, "4. Error Detection")
    utils.draw_text()

    pygame.display.update()


def main():
    utils.make_grid()
    run = True
    while run:
        config.CLOCK.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        buttons = create_buttons()
        draw(buttons)


if __name__ == "__main__":
    main()
