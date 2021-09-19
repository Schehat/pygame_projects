"""
    controls:
    - w, a, s, d: move
    - space: shoot
    - p: pause
"""


import random

import pygame

import config
import utils
from enemy import Enemy
from player import Player


class Button:
    def __init__(self, mouse, click):
        self.mouse = mouse
        self.click = click

    def button_draw(self):
        utils.check_quit_button(config.RECT_RED, self.mouse, self.click)

        check_go_button(self.mouse, self.click)


class ButtonInfo:
    def __init__(self, mouse, click, rect, text):
        self.mouse = mouse
        self.click = click
        self.rect = rect
        self.text = text

    def button_draw(self):
        utils.check_quit_button(config.RECT_RED, self.mouse, self.click)

        if utils.check_button(config.RECT_INFO, self.mouse):
            pygame.draw.rect(config.WINDOW, config.HOVER_BLUE, config.RECT_INFO)
            if self.click[0] == 1:
                set_screen(
                    "Information",
                    100,
                    intro_screen=False,
                    info_screen=True,
                    info_text="Try not to get hit from the skeleton",
                )
        else:
            pygame.draw.rect(config.WINDOW, config.BLUE, config.RECT_INFO)

        text_output = config.font_button.render(self.text, True, config.WHITE)
        text_rect = text_output.get_rect()
        text_rect.center = (
            self.rect[0] + int((self.rect[2] / 2)),
            self.rect[1] + int((self.rect[3] / 2)),
        )
        config.WINDOW.blit(text_output, text_rect)


def check_go_button(mouse, click):
    if utils.check_button(config.RECT_GREEN, mouse):
        pygame.draw.rect(config.WINDOW, config.HOVER_GREEN, config.RECT_GREEN)
        if click[0] == 1:
            if config.paused:
                config.paused = False  # stop from pausing the game
            else:
                game_loop()
    else:
        pygame.draw.rect(config.WINDOW, config.GREEN, config.RECT_GREEN)


def draw(player, enemies, enemy):
    config.WINDOW.blit(config.BACKGROUND, (0, 0))

    # draw text
    level_text = config.font.render(f"Level: {player.level}", 1, config.WHITE)
    lives_text = config.font.render(f"Lives: {player.lives}", 1, config.WHITE)
    config.WINDOW.blit(level_text, (10, 10))
    config.WINDOW.blit(
        lives_text, (config.WINDOW_SIZE[0] - 10 - lives_text.get_width(), 10)
    )

    enemy.create_enemy(player, enemies)

    for enemy in enemies:
        enemy.move()
        enemy.move_laser(player)
        if random.randrange(0, 2 * 60) == 1:
            enemy.shoot()
    player.move()
    player.move_laser(enemies)

    for enemy in enemies:
        enemy.draw()
        enemy.check(player, enemy, enemies)
    player.check(enemies)
    player.draw()
    player.health_bar()

    pygame.display.update()


def game_loop():
    run = True
    player = Player(
        int(config.WINDOW_SIZE[0] / 2 - config.PLAYER_SIZE[0] / 2), 500
    )
    enemies = []
    # creating an enemy to call the methods
    enemy = Enemy(0, 0, "red")

    while run:
        config.clock.tick(config.FPS)

        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if keys_pressed[pygame.K_p]:
            set_screen("Paused", 220, intro_screen=False, pause_screen=True)

        draw(player, enemies, enemy)


def set_screen(
    font_screen,
    text_pos,
    intro_screen=True,
    info_screen=False,
    pause_screen=False,
    info_text=None,
):
    if pause_screen:
        pygame.mixer.music.pause()
        config.paused = True
        intro = False
    else:
        intro = True
        config.paused = False
        config.WINDOW.blit(config.BACKGROUND, (0, 0))

    text_output = config.font_screen.render(font_screen, True, config.WHITE)
    text_rect = text_output.get_rect()
    text_rect.center = (int(config.WINDOW_SIZE[0] / 2), text_pos)
    config.WINDOW.blit(text_output, text_rect)

    if info_screen:
        utils.draw_info_text(info_text)

    while intro or config.paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = Button(mouse, click)

        if pause_screen:
            button.button_draw()
        else:
            button.button_draw()

        if intro_screen:
            button_info = ButtonInfo(
                mouse, click, config.RECT_INFO, "Information"
            )
            button_info.button_draw()

        if pause_screen:
            utils.draw_button_text(config.RECT_GREEN, "Continue")
        else:
            utils.draw_button_text(config.RECT_GREEN, "GO")

        utils.draw_button_text(config.RECT_RED, "CHICK OUT")

        pygame.display.update()
        pygame.event.get()
        config.clock.tick(15)


set_screen("Space Shooter", 220, intro_screen=True)
game_loop()
