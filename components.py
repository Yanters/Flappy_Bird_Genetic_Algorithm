import random
import pygame


class BackGround:
    bg_img = pygame.image.load("images/bg.png").convert_alpha()

    # empty constructor
    def __init__(self):
        pass

    def draw(self, window):
        window.blit(self.bg_img, (0, 0))


class Ground:
    ground_img = pygame.image.load("images/ground.png").convert_alpha()

    def __init__(self, ground_speed):
        self.ground_speed = ground_speed
        self.ground_scroll = 0

    def draw(self, window, win_height, win_width):
        window.blit(self.ground_img, (self.ground_scroll,
                                      win_height - self.ground_img.get_height()))
        self.ground_scroll -= self.ground_speed
        if abs(self.ground_scroll) > self.ground_img.get_width() - win_width:
            self.ground_scroll = 0


class Pipe:
    bottom_pipe_img = pygame.image.load("images/pipe.png").convert_alpha()
    top_pipe_img = pygame.transform.flip(
        bottom_pipe_img, False, True).convert_alpha()

    def __init__(self, x, min_y, max_y, pipe_speed, pipe_gap_min, pipe_gap_max):
        self.x = x
        self.y = random.randint(min_y, max_y)
        self.pipe_speed = pipe_speed
        self.pipe_gap = random.randint(pipe_gap_min, pipe_gap_max)
        self.top_pipe_rect = self.top_pipe_img.get_rect()
        self.bottom_pipe_rect = self.bottom_pipe_img.get_rect()
        self.top_pipe_rect.bottomright = (self.x, self.y + self.pipe_gap / 2)
        self.bottom_pipe_rect.topright = (self.x, self.y - self.pipe_gap / 2)

    def draw(self, window):
        window.blit(self.top_pipe_img, self.top_pipe_rect)
        window.blit(self.bottom_pipe_img, self.bottom_pipe_rect)

    def update(self, win_width):
        self.x -= self.pipe_speed
        self.top_pipe_rect.bottomright = (self.x, self.y - self.pipe_gap / 2)
        self.bottom_pipe_rect.topright = (self.x, self.y + self.pipe_gap / 2)
        if self.x < -self.top_pipe_img.get_width():
            self.x = win_width + self.top_pipe_img.get_width()


class Bird:
    bird_images = [pygame.image.load("images/bird1.png").convert_alpha(), pygame.image.load(
        "images/bird2.png").convert_alpha(), pygame.image.load("images/bird3.png").convert_alpha()]

    def __init__(self, x, y, tick_max_count=7, ground_y=800, jump_tick_delay=5, jump_rotation=30, jump_vel=-10, fall_vel=0.5, fall_rotation=2, fall_max_rotation=-60):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.tick_max_count = tick_max_count
        self.bird_index = 0
        self.bird_img = self.bird_images[self.bird_index]
        self.bird_rect = self.bird_img.get_rect()
        self.bird_rect.center = (self.x, self.y)
        self.vel = 0
        self.rotation = 0
        self.ground_y = ground_y
        self.jump_tick_delay = jump_tick_delay
        self.jump_tick_count = 0
        self.jump_rotation = jump_rotation
        self.jump_vel = jump_vel
        self.fall_vel = fall_vel
        self.fall_rotation = fall_rotation
        self.fall_max_rotation = fall_max_rotation
        self.alive = True

    def draw(self, window):
        window.blit(self.bird_img, self.bird_rect)

    def update_image(self):
        self.tick_count += 1
        if self.tick_count % self.tick_max_count == 0:
            self.bird_index += 1
            if self.bird_index > 2:
                self.bird_index = 0

        self.bird_img = pygame.transform.rotate(
            self.bird_images[self.bird_index], self.rotation)

    def update_position(self):
        self.vel += self.fall_vel
        self.rotation -= self.fall_rotation
        if self.rotation < self.fall_max_rotation:
            self.rotation = self.fall_max_rotation

        self.y += self.vel
        if self.y > self.ground_y:
            self.y = self.ground_y
            self.vel = 0
            self.alive = False

        if self.y < 0:
            self.y = 0
            self.vel = 0
        self.bird_rect.center = (self.x, self.y)

    def update(self, window):
        if self.alive:
            self.update_image()
            self.update_position()
            self.jump_tick_count += 1
        self.draw(window)

    def jump(self):
        if self.jump_tick_count > self.jump_tick_delay and self.alive:
            self.vel = self.jump_vel
            self.rotation = self.jump_rotation
            self.jump_tick_count = 0
