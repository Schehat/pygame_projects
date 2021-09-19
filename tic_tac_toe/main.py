import pygame

import config
import utils


def check():
    winner = False
    pstart = []
    pend = []

    # horizontal
    for i in range(0, 3):
        if config.grid_list[i][0] != "":
            if (
                config.grid_list[i][0] == config.grid_list[i][1]
                and config.grid_list[i][0] == config.grid_list[i][2]
            ):
                winner = config.grid_list[i][0]
                for j in config.draw_text:
                    if j[3] == i and j[4] == 0:
                        pstart.append([j[1], j[2] + 20])
                    if j[3] == i and j[4] == 2:
                        pend.append([j[1] + 25, j[2] + 20])

    # vertical
    for i in range(0, 3):
        if config.grid_list[0][i] != "":
            if (
                config.grid_list[0][i] == config.grid_list[1][i]
                and config.grid_list[0][i] == config.grid_list[2][i]
            ):
                winner = config.grid_list[0][i]
                for j in config.draw_text:
                    if j[3] == 0 and j[4] == i:
                        pstart.append([j[1] + 14, j[2]])
                    if j[3] == 2 and j[4] == i:
                        pend.append([j[1] + 14, j[2] + 37])

    # diagonal
    if config.grid_list[0][0] != "":
        if (
            config.grid_list[0][0] == config.grid_list[1][1]
            and config.grid_list[0][0] == config.grid_list[2][2]
        ):
            for j in config.draw_text:
                if j[3] == 0 and j[4] == 0:
                    pstart.append([j[1], j[2]])
                if j[3] == 2 and j[4] == 2:
                    pend.append([j[1] + 25, j[2] + 44])
            winner = config.grid_list[0][0]

    if config.grid_list[2][0] != "":
        if (
            config.grid_list[2][0] == config.grid_list[1][1]
            and config.grid_list[2][0] == config.grid_list[0][2]
        ):
            for j in config.draw_text:
                if j[3] == 2 and j[4] == 0:
                    pstart.append([j[1] - 5, j[2] + 40])
                if j[3] == 0 and j[4] == 2:
                    pend.append([j[1] + 30, j[2]])
            winner = config.grid_list[2][0]

    if winner is not False:
        text = config.font_text.render(f"Winner is {str(winner)}", 1, config.BLACK)
        config.WINDOW.blit(
            text, (int(config.WINDOW_SIZE[0] / 2 - text.get_width() / 2), 10)
        )
        pygame.draw.line(
            config.WINDOW,
            config.RED,
            (pstart[0][0], pstart[0][1]),
            (pend[0][0], pend[0][1]),
            4,
        )
        pygame.display.update()
        pygame.time.delay(3000)
        config.grid_list = [
            ["" for _ in range(config.COLS)] for _ in range(config.ROWS)
        ]
        config.current_player = config.players[0]
        config.draw_text = []
        main()

    # or draw: all elements in grid are taken
    if all(all(x) for x in config.grid_list):
        text = config.font_text.render(f"draw", 1, config.BLACK)
        config.WINDOW.blit(
            text, (int(config.WINDOW_SIZE[0] / 2 - text.get_width() / 2), 10)
        )
        pygame.display.update()
        pygame.time.delay(3000)
        config.grid_list = [
            ["" for _ in range(config.COLS)] for _ in range(config.ROWS)
        ]
        config.current_player = config.players[0]
        config.draw_text = []
        main()


def draw():
    config.WINDOW.fill(config.WHITE)
    utils.grid()
    utils.mouse()
    for i in config.draw_text:
        text = config.font_text.render(str(i[0]), 1, config.BLACK)
        config.WINDOW.blit(text, (i[1], i[2]))
    pygame.display.update()
    check()


def main():
    run = True

    while run:
        config.CLOCK.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()


if __name__ == "__main__":
    main()
