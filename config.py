import pygame

# pygame setup
win_width = 864
win_height = 768 + 168
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy Bird Genetic Algorithm")

# ground setup
ground_scroll = 0
ground_speed = 3

# game variables
fps = 60

# bird variables
bird_x = win_width*2/9
bird_y = win_height / 2
bird_tick_max_count = 10
bird_jump_tick_delay = 10
bird_jump_rotation = 55
bird_jump_vel = -12
bird_fall_vel = 0.5
bird_fall_rotation = 2
bird_fall_max_rotation = -45
