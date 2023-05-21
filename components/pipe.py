import pygame
import random

class Pipe:
    def __init__(self, x, min_y, max_y, pipe_speed, pipe_gap_min, pipe_gap_max):
        self.bottom_pipe_img = pygame.image.load("images/pipe.png").convert_alpha()
        self.top_pipe_img = pygame.transform.flip(self.bottom_pipe_img, False, True).convert_alpha()
        self.x = x
        self.y = random.randint(min_y, max_y)
        self.pipe_speed = pipe_speed
        self.pipe_passed = False
        self.pipe_gap = random.randint(pipe_gap_min, pipe_gap_max)
        self.top_pipe_rect = self.top_pipe_img.get_rect()
        self.bottom_pipe_rect = self.bottom_pipe_img.get_rect()
        self.top_pipe_rect.bottomright = (self.x, self.y + self.pipe_gap / 2)
        self.bottom_pipe_rect.topright = (self.x, self.y - self.pipe_gap / 2)

    def draw(self, window):
        window.blit(self.top_pipe_img, self.top_pipe_rect)
        window.blit(self.bottom_pipe_img, self.bottom_pipe_rect)

    def update(self):
        self.x -= self.pipe_speed
        self.top_pipe_rect.bottomright = (self.x, self.y - self.pipe_gap / 2)
        self.bottom_pipe_rect.topright = (self.x, self.y + self.pipe_gap / 2)
