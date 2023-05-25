import pygame
import pipes_collection

pygame.init()

# game variables
fps = 60
pipes = pipes_collection.Pipes()
population_size = 20

font = pygame.font.SysFont("comicsans", 50)
font_color_white = (255, 255, 255)
font_color_blue = (0, 0, 255)
font_color_red = (255, 0, 0)
font_color_orange = (255, 165, 0)

# ground variables
ground_scroll = 0
ground_speed = 3
ground_height = 168

# background variables
bg_height = 768
bg_width = 864

# pygame setup
win_width = bg_width
win_height = bg_height + ground_height
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy Bird Genetic Algorithm")

# bird variables
bird_x = win_width * 2 / 9
bird_y = win_height / 3
bird_tick_max_count = 10
bird_jump_tick_delay = 0
bird_jump_rotation = 55
bird_jump_vel = -8.5
bird_fall_vel = 0.5
bird_fall_rotation = 2
bird_fall_max_rotation = -45

# pipe variables
pipe_speed = 4
pipe_spawn_delay = 1500  # milliseconds
pipe_height = 560
pipe_width = 78
pipe_gap_min = 150
pipe_gap_max = 300
pipe_min_y = win_height - ground_height - pipe_height - pipe_gap_min/2
pipe_max_y = pipe_height + pipe_gap_min/2
