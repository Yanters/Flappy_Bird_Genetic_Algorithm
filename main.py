import pygame
import config
import components

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0

# load images
bg = pygame.image.load("images/bg.png").convert()


# create objects
ground = components.Ground(config.ground_speed)
bg = components.BackGround()
bird = components.Bird(config.bird_x, config.bird_y,
                       config.bird_tick_max_count, config.win_height - ground.ground_img.get_height(), config.bird_jump_tick_delay, config.bird_jump_rotation, config.bird_jump_vel, config.bird_fall_vel, config.bird_fall_rotation, config.bird_fall_max_rotation)


def events_handler():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


while running:
    # handle events
    events_handler()

    # draw the background
    bg.draw(config.window)

    # draw the ground
    ground.draw(config.window, config.win_height, config.win_width)

    # draw the bird
    bird.update(config.window)

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
