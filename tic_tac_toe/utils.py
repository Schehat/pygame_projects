import pygame

import config


def mouse():
    x, y = pygame.mouse.get_pos()
    row, col = None, None

    # evaluate correct col & row
    if (
        int(config.WINDOW_SIZE[0] / 3 + config.GAP / 2) > x > config.GAP
        and int(config.GAP / 2 * 3) < y < config.WINDOW_SIZE[1] - config.GAP
    ):
        col = 0
    elif (
        int(config.WINDOW_SIZE[0] / 3 * 2) > x > int(config.WINDOW_SIZE[0] / 3 * 1)
        and config.GAP < y < config.WINDOW_SIZE[1] - config.GAP
    ):
        col = 1
    elif (
        int(config.WINDOW_SIZE[0] - config.GAP) > x > int(config.WINDOW_SIZE[0] / 3 * 2)
        and config.GAP < y < config.WINDOW_SIZE[1] - config.GAP
    ):
        col = 2

    if (
        int(config.WINDOW_SIZE[1] / 3 * 1) > y > config.GAP
        and config.GAP < x < config.WINDOW_SIZE[0] - config.GAP
    ):
        row = 0
    elif (
        int(config.WINDOW_SIZE[1] / 3 * 2) > y > int(config.WINDOW_SIZE[1] / 3 * 1)
        and config.GAP < x < config.WINDOW_SIZE[0] - config.GAP
    ):
        row = 1
    elif (
        int(config.WINDOW_SIZE[1] - config.GAP) > y > int(config.WINDOW_SIZE[1] / 3 * 2)
        and config.GAP < x < config.WINDOW_SIZE[0] - config.GAP
    ):
        row = 2

    # evaluate correct xpos & ypos
    if col is not None and row is not None:
        if col == 0:
            xpos = config.GAP / 2 * 3
        elif col == 1:
            xpos = config.WINDOW_SIZE[0] / 3 + config.GAP / 2
        elif col == 2:
            xpos = config.WINDOW_SIZE[0] / 3 * 2 - config.GAP / 2
        else:
            xpos = None

        if row == 0:
            ypos = config.GAP / 2 * 3
        elif row == 1:
            ypos = config.WINDOW_SIZE[1] / 3 + config.GAP / 2
        elif row == 2:
            ypos = config.WINDOW_SIZE[1] / 3 * 2 - config.GAP / 2
        else:
            ypos = None

        if xpos is not None and ypos is not None:
            pygame.draw.rect(
                config.WINDOW,
                config.GREY,
                (
                    int(xpos),
                    int(ypos),
                    int(config.WINDOW_SIZE[0] / 3 - config.GAP),
                    int(config.WINDOW_SIZE[1] / 3 - config.GAP),
                ),
            )

        mouse_pressed(row, col, xpos, ypos)


def mouse_pressed(row, col, xpos, ypos):
    if row is not None and col is not None:
        pygame.event.get()
        if pygame.mouse.get_pressed()[0]:
            if config.current_player == "X" and config.grid_list[row][col] == "":
                config.grid_list[row][col] = config.current_player
                text = config.font_text.render(
                    str(config.current_player), 1, config.BLACK
                )
                # need to know which symbol to draw at which position
                # thus saving the information and blit later
                config.draw_text.append(
                    [
                        config.current_player,
                        int(xpos + 75 - text.get_width() / 2),
                        int(ypos + 75 - text.get_height() / 2),
                        row,
                        col,
                    ]
                )
                config.current_player = config.players[1]
            elif config.current_player == "O" and config.grid_list[row][col] == "":
                config.grid_list[row][col] = config.current_player
                text = config.font_text.render(
                    str(config.current_player), 1, config.BLACK
                )
                config.draw_text.append(
                    [
                        config.current_player,
                        int(xpos + 75 - text.get_width() / 2),
                        int(ypos + 75 - text.get_height() / 2),
                        row,
                        col,
                    ]
                )
                config.current_player = config.players[0]


def grid():
    # vertical line
    pygame.draw.line(
        config.WINDOW,
        config.BLACK,
        (int(config.WINDOW_SIZE[0] / 3 + config.GAP / 2), int(config.GAP / 2 * 3)),
        (
            int(config.WINDOW_SIZE[0] / 3 + config.GAP / 2),
            int(config.WINDOW_SIZE[1] - config.GAP / 2 * 3),
        ),
        4,
    )
    pygame.draw.line(
        config.WINDOW,
        config.BLACK,
        (int(config.WINDOW_SIZE[0] / 3 * 2 - config.GAP / 2), int(config.GAP / 2 * 3)),
        (
            int(config.WINDOW_SIZE[0] / 3 * 2 - config.GAP / 2),
            int(config.WINDOW_SIZE[1] - config.GAP / 2 * 3),
        ),
        4,
    )

    # horizontal line
    pygame.draw.line(
        config.WINDOW,
        config.BLACK,
        (
            int(config.GAP + config.GAP / 2),
            int(config.WINDOW_SIZE[1] / 3 + config.GAP / 2),
        ),
        (
            int(config.WINDOW_SIZE[1] - config.GAP / 2 * 3),
            int(config.WINDOW_SIZE[1] / 3 + config.GAP / 2),
        ),
        4,
    )
    pygame.draw.line(
        config.WINDOW,
        config.BLACK,
        (
            int(config.GAP + config.GAP / 2),
            int(config.WINDOW_SIZE[1] / 3 * 2 - config.GAP / 2),
        ),
        (
            int(config.WINDOW_SIZE[1] - config.GAP / 2 * 3),
            int(config.WINDOW_SIZE[1] / 3 * 2 - config.GAP / 2),
        ),
        4,
    )
