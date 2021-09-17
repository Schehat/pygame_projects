import pygame

import config
from enemy import Enemy
from player import Player


def game_loop():
    run = True
    player = Player(int(config.WINDOW_SIZE[0] / 2 - config.PLAYER_SIZE[0] / 2), 500)
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
            game_pause()

        draw(player, enemies, enemy)





def game_intro():
    intro = True
    config.WINDOW.blit(config.BACKGROUND, (0, 0))
    text_output = config.font_screen.render("Space Shooter", True, config.WHITE)
    text_rect = text_output.get_rect()
    text_rect.center = (int(config.WINDOW_SIZE[0] / 2), 220)
    config.WINDOW.blit(text_output, text_rect)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonIntro(mouse, click)
        button.button_draw()
        button_info = ButtonInfo(mouse, click, config.RECT_INFO, "Information")
        button_info.button_draw()
        button.button_text(config.RECT_GREEN, "GO")
        button.button_text(config.RECT_RED, "CHICK OUT")

        config.pygame.display.config.update()
        pygame.event.get()
        config.clock.tick(15)


def game_info():
    intro = True
    config.WINDOW.blit(config.BACKGROUND, (0, 0))
    text_output = config.font_screen.render("Information", True, config.WHITE)
    text_rect = text_output.get_rect()
    text_rect.center = (int(config.WINDOW_SIZE[0] / 2), 100)
    config.WINDOW.blit(text_output, text_rect)

    ButtonInfo.info_text()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonIntro(mouse, click)
        button.button_draw()
        button.button_text(config.RECT_GREEN, "GO")
        button.button_text(config.RECT_RED, "CHICK OUT")

        config.pygame.display.config.update()
        pygame.event.get()
        config.clock.tick(15)


def game_pause():
    pygame.config.mixer.music.pause()

    global paused
    paused = True

    text_output = config.font_screen.render("Paused", True, config.WHITE)
    text_rect = text_output.get_rect()
    text_rect.center = (int(config.WINDOW_SIZE[0] / 2), 220)
    config.WINDOW.blit(text_output, text_rect)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonPause(mouse, click)
        button.button_draw()
        button.button_text(config.RECT_GREEN, "Continue")
        button.button_text(config..RECT_RED, "CHICK OUT")

        config.pygame.display.config.update()
        pygame.event.get()
        config.clock.tick(15)
