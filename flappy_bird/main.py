"""
    controls:
    - space: jump
"""

import pygame

from base import Base
from bird import Bird
from config import (
    BASE_IMG,
    BG_IMG,
    BLACK,
    CLOCK,
    FPS,
    RED,
    WINDOW,
    WINDOW_SIZE,
    font_gameover,
    font_score,
)
from pipe import Pipe


def draw_window(bird, pipes, base, score):
    WINDOW.blit(BG_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw()
    base.draw()
    text_score = font_score.render(f"Score: {score}", 1, BLACK)
    WINDOW.blit(text_score, (10, 10))
    bird.draw()
    pygame.display.update()


def gameover():
    text_gameover = font_gameover.render("Game Over", 1, RED)
    WINDOW.blit(
        text_gameover,
        (
            int(WINDOW_SIZE[0] / 2 - text_gameover.get_width() / 2),
            int(WINDOW_SIZE[1] / 2 - text_gameover.get_height() / 2),
        ),
    )
    pygame.display.update()
    pygame.time.delay(2000)
    main()


def main():
    run = True
    bird = Bird(100, 150)
    pipes = [Pipe(WINDOW_SIZE[0])]
    base = Base(WINDOW_SIZE[0] - BASE_IMG.get_height())
    score = 0

    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        add_pipe = False
        rem = []
        for pipe in pipes:
            if pipe.collide(bird):
                gameover()

            if not pipe.passed and pipe.x - 50 < bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(WINDOW_SIZE[0]))

        for r in rem:
            pipes.remove(r)

        if bird.y > WINDOW_SIZE[1] - BASE_IMG.get_height():
            gameover()

        base.move()
        bird.jump()
        bird.move()
        draw_window(bird, pipes, base, score)


if __name__ == "__main__":
    main()
