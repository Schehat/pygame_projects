"""
    controls:
    - arrows: move
    - space: pause
"""

import random

import pygame

from cars import Cars
from config import (
    BARREL_HEIGHT,
    BARREL_WIDTH,
    BLACK,
    BLUE,
    CAR_HEIGHT,
    CAR_WIDTH,
    DISPLAY_HEIGHT,
    DISPLAY_WIDTH,
    FPS,
    GREEN,
    HOVER_BLUE,
    HOVER_GREEN,
    HOVER_RED,
    OBSTACLES_NUMBER,
    RECT_GREEN,
    RECT_INFO,
    RECT_RED,
    RED,
    WHITE,
    clock,
    crash_sound,
    game_display,
    road1_img,
    road2_img,
)
from obstacle import Obstacles
from road import Road


class Messages:
    def __init__(self, x_car, y_car):
        self.x_car = x_car
        self.y_car = y_car

    def crash_border(self):
        if (
            self.x_car > DISPLAY_WIDTH - CAR_WIDTH
            or self.x_car < 0
            or self.y_car < 0
            or self.y_car > DISPLAY_HEIGHT - CAR_HEIGHT
        ):
            crash("YOU CRASHED")

    def crash_ob(self, x_ob, y_ob):
        if self.y_car < y_ob + BARREL_HEIGHT and self.y_car + BARREL_HEIGHT > y_ob:
            if (
                x_ob < self.x_car < x_ob + BARREL_WIDTH
                or x_ob < self.x_car + CAR_WIDTH < x_ob + BARREL_WIDTH
            ):
                crash("YOU CRASHED")

    @staticmethod
    def score(points):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " + str(points), True, BLACK)
        game_display.blit(text, (0, 0))


class ButtonIntro:
    def __init__(self, mouse, click):
        self.mouse = mouse
        self.click = click

    def button_draw(self):
        if (
            RECT_RED[0] < self.mouse[0] < RECT_RED[0] + RECT_RED[2]
            and RECT_RED[1] < self.mouse[1] < RECT_RED[1] + RECT_RED[3]
        ):
            pygame.draw.rect(game_display, HOVER_RED, RECT_RED)
            if self.click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(game_display, RED, RECT_RED)
        if (
            RECT_GREEN[0] < self.mouse[0] < RECT_GREEN[0] + RECT_GREEN[2]
            and RECT_GREEN[1] < self.mouse[1] < RECT_GREEN[1] + RECT_GREEN[3]
        ):
            pygame.draw.rect(game_display, HOVER_GREEN, RECT_GREEN)
            if self.click[0] == 1:
                game_loop()

        else:
            pygame.draw.rect(game_display, GREEN, RECT_GREEN)

    @staticmethod
    def button_text(rect, text):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_output = font.render(text, True, BLACK)
        text_rect = text_output.get_rect()
        text_rect.center = (rect[0] + int((rect[2] / 2)), rect[1] + int((rect[3] / 2)))
        game_display.blit(text_output, text_rect)


class ButtonPause:
    def __init__(self, mouse, click):
        self.mouse = mouse
        self.click = click

    def button_draw(self):
        if (
            RECT_RED[0] < self.mouse[0] < RECT_RED[0] + RECT_RED[2]
            and RECT_RED[1] < self.mouse[1] < RECT_RED[1] + RECT_RED[3]
        ):
            pygame.draw.rect(game_display, HOVER_RED, RECT_RED)
            if self.click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(game_display, RED, RECT_RED)
        if (
            RECT_GREEN[0] < self.mouse[0] < RECT_GREEN[0] + RECT_GREEN[2]
            and RECT_GREEN[1] < self.mouse[1] < RECT_GREEN[1] + RECT_GREEN[3]
        ):
            pygame.draw.rect(game_display, HOVER_GREEN, RECT_GREEN)
            if self.click[0] == 1:
                pygame.mixer.music.unpause()
                return False
        else:
            pygame.draw.rect(game_display, GREEN, RECT_GREEN)

    @staticmethod
    def button_text(rect, text):
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_output = font.render(text, True, BLACK)
        text_rect = text_output.get_rect()
        text_rect.center = (rect[0] + int((rect[2] / 2)), rect[1] + int((rect[3] / 2)))
        game_display.blit(text_output, text_rect)


class ButtonInfo:
    def __init__(self, mouse, click, rect, text):
        self.mouse = mouse
        self.click = click
        self.rect = rect
        self.text = text

    def button_draw(self):
        if (
            RECT_INFO[0] < self.mouse[0] < RECT_INFO[0] + RECT_INFO[2]
            and RECT_INFO[1] < self.mouse[1] < RECT_INFO[1] + RECT_INFO[3]
        ):
            pygame.draw.rect(game_display, HOVER_BLUE, RECT_INFO)
            if self.click[0] == 1:
                game_info()
        else:
            pygame.draw.rect(game_display, BLUE, RECT_INFO)

        font = pygame.font.Font("freesansbold.ttf", 20)
        text_output = font.render(self.text, True, BLACK)
        text_rect = text_output.get_rect()
        text_rect.center = (
            self.rect[0] + int((self.rect[2] / 2)),
            self.rect[1] + int((self.rect[3] / 2)),
        )
        game_display.blit(text_output, text_rect)

    @staticmethod
    def info_text():
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_output_arrows = font.render(
            "Use The Arrows To Move Back and Forth or Sideway", True, BLACK, WHITE
        )
        text_rect_arrows = text_output_arrows.get_rect()
        text_rect_arrows.center = (int(DISPLAY_WIDTH / 2), 200)
        game_display.blit(text_output_arrows, text_rect_arrows)
        text_output_spacebar = font.render(
            "The Spacebar Allows To Pause The Game", True, BLACK, WHITE
        )
        text_rect_spacebar = text_output_spacebar.get_rect()
        text_rect_spacebar.center = (int(DISPLAY_WIDTH / 2), 220)
        game_display.blit(text_output_spacebar, text_rect_spacebar)
        text_output_obstacle = font.render(
            "Do Not Crash Against Obstacles", True, BLACK, WHITE
        )
        text_rect_obstacle = text_output_obstacle.get_rect()
        text_rect_obstacle.center = (int(DISPLAY_WIDTH / 2), 240)
        game_display.blit(text_output_obstacle, text_rect_obstacle)


# defining functions
def game_intro():
    intro = True
    game_display.blit(road1_img, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 80)
    text_output = font.render("Roadtangle", True, BLACK)
    text_rect = text_output.get_rect()
    text_rect.center = (int(DISPLAY_WIDTH / 2), 220)
    game_display.blit(text_output, text_rect)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonIntro(mouse, click)
        button.button_draw()
        button_info = ButtonInfo(mouse, click, RECT_INFO, "Information")
        button_info.button_draw()
        button.button_text(RECT_GREEN, "GO")
        button.button_text(RECT_RED, "CHICK OUT")

        pygame.display.update()
        pygame.event.get()
        # to not take all my ram
        clock.tick(15)


def game_info():
    intro = True
    game_display.blit(road1_img, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 80)
    text_output = font.render("Information", True, BLACK)
    text_rect = text_output.get_rect()
    text_rect.center = (int(DISPLAY_WIDTH / 2), 100)
    game_display.blit(text_output, text_rect)

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
        button.button_text(RECT_GREEN, "GO")
        button.button_text(RECT_RED, "CHICK OUT")

        pygame.display.update()
        pygame.event.get()
        clock.tick(15)


def game_loop():

    # -1 means in infinity (1: normal and 1.5: faster etc.)
    pygame.mixer.music.play(-1)

    game_exit = False
    points = 0
    obstacles = list()
    # creating instances of objects
    car = Cars(int(DISPLAY_WIDTH * 0.45), int(DISPLAY_HEIGHT * 0.8), 0, 0, 5, 0, 0, 5)
    for i in range(OBSTACLES_NUMBER):
        obstacles.append(
            Obstacles(
                random.randrange(0, DISPLAY_WIDTH),
                random.randrange(-1000, -600),
                random.randrange(5, 10),
            )
        )

    road1 = Road(0, 0)
    road2 = Road(0, 600)

    while not game_exit:

        message = Messages(car.x, car.y)

        # checks all events (inputs) and creates a list per frame per second
        for event in pygame.event.get():
            # closes the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # location update
        car.move()
        car.update()
        for i in range(OBSTACLES_NUMBER):
            obstacles[i].move()

        # drawing
        game_display.fill(WHITE)
        road1.draw(road1_img)
        road1.move()
        road2.draw(road2_img)
        road2.move()
        car.draw()
        message.score(points)
        for i in range(OBSTACLES_NUMBER):
            obstacles[i].draw()

        # checking
        for i in range(OBSTACLES_NUMBER):
            if DISPLAY_HEIGHT < obstacles[i].ob_y:
                points += 50
                if points >= 1000:
                    obstacles[i].ob_speed += 1
        message.crash_border()
        for i in range(OBSTACLES_NUMBER):
            message.crash_ob(obstacles[i].ob_x, obstacles[i].ob_y)
        for i in range(OBSTACLES_NUMBER):
            obstacles[i].set_random()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:
            game_pause()

        # the drawing with no parameter updates everything & with parameter only this => less calculation
        pygame.display.update()

        # determine frames per second
        clock.tick(FPS)


def game_pause():
    pygame.mixer.music.pause()

    paused = True

    font = pygame.font.Font("freesansbold.ttf", 80)
    text_output = font.render("Paused", True, BLACK)
    text_rect = text_output.get_rect()
    text_rect.center = (int(DISPLAY_WIDTH / 2), 220)
    game_display.blit(text_output, text_rect)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonPause(mouse, click)
        # updated paused weather continue was
        paused = button.button_draw()
        if paused is None:
            paused = True
        button.button_text(RECT_GREEN, "Continue")
        button.button_text(RECT_RED, "CHICK OUT")

        pygame.display.update()
        pygame.event.get()
        clock.tick(15)


def crash(text):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    intro = True
    font = pygame.font.Font("freesansbold.ttf", 80)
    text_output = font.render(text, True, BLACK)
    text_rect = text_output.get_rect()
    text_rect.center = (int(DISPLAY_WIDTH / 2), 220)
    game_display.blit(text_output, text_rect)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button = ButtonIntro(mouse, click)
        button.button_draw()
        button.button_text(RECT_GREEN, "PLAY AGAIN!")
        button.button_text(RECT_RED, "CHICK OUT")

        pygame.display.update()
        pygame.event.get()
        clock.tick(15)


# call the game
game_intro()
game_loop()
# stop pygame
pygame.quit()
# system quit
quit()
