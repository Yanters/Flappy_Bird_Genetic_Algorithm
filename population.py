import components.bird as bird
import config
import species

class Population:
    def __init__(self, size):
        self.birds = []
        self.size = size
        self.species = []
        self.generations = 0
        self.best_score = 0
        for _ in range(size):
            self.birds.append(bird.Bird(config.bird_x, config.bird_y,
                       config.bird_tick_max_count, config.win_height - config.ground_height, config.bird_jump_tick_delay, config.bird_jump_rotation, config.bird_jump_vel, config.bird_fall_vel, config.bird_fall_rotation, config.bird_fall_max_rotation))

    def update(self, window, pipes):
        for bird in self.birds:
            bird.update(window, pipes)
        self.check_best_score()

    def is_extinct(self):
        for bird in self.birds:
            if bird.alive:
                return False
        return True
    
    def check_best_score(self):
        for bird in self.birds:
            if bird.score > self.best_score:
                self.best_score = bird.score

    def get_best_score(self):
        best_score = 0
        for bird in self.birds:
            if bird.score > best_score:
                best_score = bird.score
        return best_score
    
    def create_new_generation(self):
        self.species = []
        self.generations += 1

        # Split the population into species
        self.create_species()
        
        # Calculate the average fitness of each species
        self.sort_species_by_fitness()

        # Create a new generation of birds
        self.create_new_generation_birds()


    def create_new_generation_birds(self):
        bird_count = config.population_size
        next_gen = []
        # Add the best bird from each species to the next generation
        for s in self.species:
            if bird_count > 0:
                next_gen.append(s.birds[0].clone())
                bird_count -= 1

        # Generate number of birds to mutate from each species
        birds_for_species = bird_count // len(self.species)

        # Add the rest of the birds to the next generation
        for s in self.species:
            for _ in range(birds_for_species):
                next_gen.append(s.child())
                bird_count -= 1

        # Fill the rest of the next generation with random birds from the best species
        for _ in range(bird_count):
            next_gen.append(self.species[0].child())

        self.birds = next_gen


    def create_species(self):
        for bird in self.birds:
            # if species is empty, create a new species
            if not self.species:
                self.species.append(species.Species(bird))
            else:
                # if the bird is not compatible with any species, create a new species
                if not self.is_compatible(bird):
                    self.species.append(species.Species(bird))
              

    def is_compatible(self, bird):
        for species in self.species:
            if species.compare_brain(bird.brain):
                # add bird to species
                species.add_to_species(bird)
                return True
        return False
    
    def sort_species_by_fitness(self):
        for s in self.species:
            s.calculate_average_fitness()
            s.sort_players_by_fitness()
        self.species.sort(key=lambda x: x.average_fitness, reverse=True)

    def count_alive(self):
        alive = 0
        for bird in self.birds:
            if bird.alive:
                alive += 1
        return alive
    
    def kill_all(self):
        for bird in self.birds:
            bird.alive = False