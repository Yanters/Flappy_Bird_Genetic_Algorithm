import components.bird as bird
import config

class Population:
    def __init__(self, size):
        self.birds = []
        self.size = size
        for _ in range(size):
            self.birds.append(bird.Bird(config.bird_x, config.bird_y,
                       config.bird_tick_max_count, config.win_height - config.ground_height, config.bird_jump_tick_delay, config.bird_jump_rotation, config.bird_jump_vel, config.bird_fall_vel, config.bird_fall_rotation, config.bird_fall_max_rotation))

    def update(self, window, pipes):
        for bird in self.birds:
            bird.update(window, pipes)

    def is_extinct(self):
        for bird in self.birds:
            if bird.alive:
                return False
        return True
    
    def temp_jump(self):
        for bird in self.birds:
            bird.jump()

    def random_jump(self):
        for bird in self.birds:
            bird.random_jump()

    def jump(self):
        for bird in self.birds:
            bird.jump()

    def get_best_score(self):
        best_score = 0
        for bird in self.birds:
            if bird.score > best_score:
                best_score = bird.score
        return best_score