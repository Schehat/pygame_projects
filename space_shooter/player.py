import pygame

import config
from enemy import Enemy
from ship import Ship


class Player(Ship):
    def __init__(self, x, y, health=100, v=10):
        super().__init__(x, y, health, v)
        self.level = 0
        self.lives = 10
        self.ship_img = config.PLAYER_RED_SHIP
        self.laser_img = config.GREEN_LASER
        # pixel perfect collision mask = hitbox - edit: more or less...
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] and self.x - self.v >= 0:
            self.x -= self.v
        elif keys_pressed[pygame.K_a] and self.x >= 0:
            self.x -= 1
        if (
            keys_pressed[pygame.K_d]
            and self.x + self.v + self.get_width() <= config.WINDOW_SIZE[0]
        ):
            self.x += self.v
        elif (
            keys_pressed[pygame.K_d]
            and self.x + self.get_width() <= config.WINDOW_SIZE[0]
        ):
            self.x += 1
        if keys_pressed[pygame.K_w] and self.y - self.v >= 0:
            self.y -= self.v
        elif keys_pressed[pygame.K_w] and self.y >= 0:
            self.y -= 1
        if (
            keys_pressed[pygame.K_s]
            and self.y + self.v + self.get_height() + 25
            <= config.WINDOW_SIZE[1]
        ):
            self.y += self.v
        elif (
            keys_pressed[pygame.K_s]
            and self.y + self.get_height() + 25 <= config.WINDOW_SIZE[1]
        ):
            self.y += 1

        if keys_pressed[pygame.K_SPACE]:
            self.shoot()

    def check(self, enemies):
        # game over screen
        if self.lives <= 0 or self.health <= 0:
            game_over_text = config.font.render("Game Over", 1, config.WHITE)
            config.WINDOW.blit(
                game_over_text,
                (
                    int(
                        config.WINDOW_SIZE[0] / 2
                        - game_over_text.get_width() / 2
                    ),
                    int(
                        config.WINDOW_SIZE[1] / 2
                        - game_over_text.get_height() / 2
                    ),
                ),
            )
            self.draw()
            pygame.display.update()
            pygame.time.delay(1000)
            # to exit the game
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.level = 0
            self.lives = 10
            self.health = 100
            enemies.clear()
            Enemy.wave_length = 0
            self.x, self.y = (
                int(config.WINDOW_SIZE[0] / 2 - config.PLAYER_SIZE[0] / 2),
                500,
            )

    def move_laser(self, enemies):
        self.cooldown()
        for laser in self.lasers:
            laser.move(-laser.v)
            if laser.off_screen():
                self.lasers.remove(laser)
            else:
                for enemy in enemies:
                    if laser.collision(enemy, laser):
                        config.sound_hit.play()
                        enemies.remove(enemy)
                        self.lasers.remove(laser)

    def health_bar(self):
        pygame.draw.rect(
            config.WINDOW,
            (255, 0, 0),
            (self.x, self.y + self.get_height() + 10, self.get_width(), 10),
        )
        pygame.draw.rect(
            config.WINDOW,
            (0, 255, 0),
            (
                self.x,
                self.y + self.get_height() + 10,
                int(self.get_width() * (self.health / self.max_health)),
                10,
            ),
        )
