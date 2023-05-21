import pygame
import config
import population
import components.background as background
import components.ground as ground

# pygame setup
clock = pygame.time.Clock()
running = True
dt = 0
pipe_spawn_timer = -config.pipe_spawn_delay

# create objects
ground = ground.Ground(config.ground_speed)
bg = background.BackGround()
birdPopulation = population.Population(config.population_size)

def events_handler():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    config.window.blit(img, (x, y))


def reset():
    global birdPopulation, pipe_spawn_timer
    birdPopulation = population.Population(config.population_size)
    config.pipes.clear_pipes()
    pipe_spawn_timer = -config.pipe_spawn_delay


while running:
    # handle events
    events_handler()

    # draw the background
    bg.draw(config.window)

    # spawn pipes
    time = pygame.time.get_ticks()
    if time - pipe_spawn_timer > config.pipe_spawn_delay:
        pipe_spawn_timer = time
        config.pipes.add_pipe(config.win_width, config.pipe_width, config.pipe_min_y, config.pipe_max_y,
                              config.pipe_speed, config.pipe_gap_min, config.pipe_gap_max)

    # remove pipes that are out of screen
    config.pipes.remove_pipes_passed()

    # draw the pipes
    config.pipes.draw(config.window)

    # draw the ground
    ground.draw(config.window, config.win_height, config.win_width)

    # draw the population
    birdPopulation.update(config.window, config.pipes)

    # draw the score
    draw_text(str(birdPopulation.get_best_score()), config.font,
              config.font_color_white, config.win_width/2 - 10, 10)

    # bird movement
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    birdPopulation.random_jump()

    # check if population is dead
    if birdPopulation.is_extinct():
        draw_text("Press SPACE to restart", config.font,
                  config.font_color_blue, config.win_width/2 - 250, config.win_height/2 - 50)
        # wait for space to be pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            reset()
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(config.fps) / 1000

pygame.quit()
