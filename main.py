import pygame
import config
import components

# pygame setup
clock = pygame.time.Clock()
running = True
dt = 0
pipe_spawn_timer = -config.pipe_spawn_delay

# create objects
ground = components.Ground(config.ground_speed)
bg = components.BackGround()
bird = components.Bird(config.bird_x, config.bird_y,
                       config.bird_tick_max_count, config.win_height - ground.ground_img.get_height(), config.bird_jump_tick_delay, config.bird_jump_rotation, config.bird_jump_vel, config.bird_fall_vel, config.bird_fall_rotation, config.bird_fall_max_rotation)
pipes = []


def events_handler():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    config.window.blit(img, (x, y))


while running:
    # handle events
    events_handler()

    # draw the background
    bg.draw(config.window)

    # spawn pipes
    time = pygame.time.get_ticks()
    if time - pipe_spawn_timer > config.pipe_spawn_delay:
        pipe_spawn_timer = time
        pipes.append(components.Pipe(config.win_width + config.pipe_width, config.pipe_min_y, config.pipe_max_y,
                                     config.pipe_speed, config.pipe_gap_min, config.pipe_gap_max))

    # remove pipes that are out of screen
    for pipe in pipes:
        if pipe.x < 0 - pipe.top_pipe_img.get_width()/2:
            pipes.remove(pipe)

    # draw the pipes
    for pipe in pipes:
        pipe.draw(config.window)
        pipe.update()

    # draw the ground
    ground.draw(config.window, config.win_height, config.win_width)

    # draw the bird
    bird.update(config.window, pipes)

    # draw the score
    draw_text(str(bird.score), config.font,
              config.font_color, config.win_width/2 - 10, 10)

    # bird movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.jump()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(config.fps) / 1000

pygame.quit()
