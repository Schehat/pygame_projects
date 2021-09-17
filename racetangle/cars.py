import pygame

from config import car_img, game_display


class Cars:
    def __init__(
        self, x, y, x_l_change, x_r_change, x_vel, y_u_change, y_d_change, y_vel
    ):
        self.x = x
        self.y = y
        self.x_l_change = x_l_change
        self.x_r_change = x_r_change
        self.x_vel = x_vel
        self.y_u_change = y_u_change
        self.y_d_change = y_d_change
        self.y_vel = y_vel

    def draw(self):
        game_display.blit(car_img, (self.x, self.y))

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            self.x_l_change = -self.x_vel
        else:
            self.x_l_change = 0
        if keys_pressed[pygame.K_RIGHT]:
            self.x_r_change = self.x_vel
        else:
            self.x_r_change = 0

        if keys_pressed[pygame.K_UP]:
            self.y_u_change = -self.y_vel
        else:
            self.y_u_change = 0
        if keys_pressed[pygame.K_DOWN]:
            self.y_d_change = self.y_vel
        else:
            self.y_d_change = 0

    def update(self):
        self.x += self.x_l_change + self.x_r_change
        self.y += self.y_u_change + self.y_d_change
