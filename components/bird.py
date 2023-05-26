import pygame
import config
import random
import brain

class Bird:
    bird_images = [pygame.image.load("./images/bird1.png").convert_alpha(), pygame.image.load(
        "./images/bird2.png").convert_alpha(), pygame.image.load("./images/bird3.png").convert_alpha()]
    

    def __init__(self, x, y, tick_max_count=7, ground_y=800, jump_tick_delay=5, jump_rotation=30, jump_vel=-10, fall_vel=0.5, fall_rotation=2, fall_max_rotation=-60):
        self.x = x
        self.y = y
        self.score = 0
        self.fitness = 0
        self.tick_count = 0
        self.tick_max_count = tick_max_count
        self.bird_index = 0
        self.bird_img = self.bird_images[self.bird_index]
        self.bird_hitbox = self.bird_img.get_rect()
        self.bird_hitbox.center = (self.x, self.y)
        self.vel = 0
        self.rotation = 0
        self.ground_y = ground_y # starting y position of the ground
        self.jump_tick_delay = jump_tick_delay
        self.jump_tick_count = 0
        self.jump_rotation = jump_rotation
        self.jump_vel = jump_vel
        self.fall_vel = fall_vel
        self.fall_rotation = fall_rotation
        self.fall_max_rotation = fall_max_rotation
        self.alive = True

        #AI
        self.vision = [0,0,0]
        self.brain = brain.Brain(3)

        # generate net 
        self.brain.generate_net()



    def draw(self, window):
        window.blit(self.bird_img, self.bird_hitbox)

    def update_image(self):
        if self.alive:
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
        self.bird_hitbox.center = (self.x, self.y)

    def check_collision(self, pipes):
        for pipe in pipes.get_pipes():
            if self.bird_hitbox.colliderect(pipe.top_pipe_rect) or self.bird_hitbox.colliderect(pipe.bottom_pipe_rect):
                self.alive = False

    def check_passed_pipes(self, pipes):
        for pipe in pipes.get_pipes():
            if self.bird_hitbox.left > pipe.top_pipe_rect.right and not pipe.pipe_passed:
                self.score += 1
                pipe.pipe_passed = True

    def update(self, window, pipes):
        if self.alive:
            self.check_collision(pipes)
            self.check_passed_pipes(pipes)
            self.jump_tick_count += 1
            self.look()
            self.think()
            self.fitness += 1
        self.update_position()
        self.update_image()
        self.draw(window)
        

    def jump(self):
        if self.jump_tick_count > self.jump_tick_delay and self.alive:
            self.vel = self.jump_vel
            self.rotation = self.jump_rotation
            self.jump_tick_count = 0

    def random_jump(self):
        # generate a random number between 0 and 1
        rand = random.random()
        # if the random number is less than 0.1, jump
        if rand < 0.1:
            self.jump()

    def closest_pipe(self):
        for pipe in config.pipes.get_pipes():
            if not pipe.pipe_passed:
                return pipe
        print("No pipes left")
        return config.pipes[-1]
                
    def look(self):
        if config.pipes and self.alive:

            # Line to top pipe
            self.vision[0] = max(0, self.bird_hitbox.center[1] - self.closest_pipe().top_pipe_rect.bottomleft[1]) / config.win_height

            # Line to mid pipe
            self.vision[1] = max(0, self.closest_pipe().top_pipe_rect.bottomleft[0] - self.bird_hitbox.center[0]) / config.win_width

            # Line to bottom pipe
            self.vision[2] = max(0, self.closest_pipe().bottom_pipe_rect.topleft[1] - self.bird_hitbox.center[1]) / config.win_height
            if config.show_lines:
                pygame.draw.line(config.window, config.font_color_blue, self.bird_hitbox.center,
                                    (self.bird_hitbox.center[0], self.closest_pipe().top_pipe_rect.bottomleft[1]))
                pygame.draw.line(config.window, config.font_color_orange, self.bird_hitbox.center,
                                    (self.closest_pipe().x , self.bird_hitbox.center[1]))
                pygame.draw.line(config.window, config.font_color_red, self.bird_hitbox.center,
                                    (self.bird_hitbox.center[0],  self.closest_pipe().bottom_pipe_rect.topleft[1]))
            
         
            
    def think(self):
        output = self.brain.feed_forward(self.vision)
        if output > 0.7:
            self.jump()

    def clone(self):
        clone = Bird(config.bird_x, config.bird_y, self.tick_max_count, self.ground_y, self.jump_tick_delay, self.jump_rotation, self.jump_vel, self.fall_vel, self.fall_rotation, self.fall_max_rotation)
        clone.brain = self.brain.clone()
        clone.brain.generate_net()
        return clone
            
