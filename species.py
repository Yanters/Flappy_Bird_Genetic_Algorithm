import random

class Species:
    def __init__(self, bird):
        self.birds = [bird]
        self.threshold = 1.4
        self.average_fitness = bird.score
        self.species_connections = bird.brain.get_connections()

    def compare_brain(self, brain):
        connections = brain.get_connections()
        return self.compare_connections(connections) > self.threshold
    
    def compare_connections(self, connections):
        weight_difference = 0
        for i in range(0, len(connections)):
            for j in range(0, len(connections)):
                if self.species_connections[i].from_node.id == connections[j].from_node.id and self.species_connections[i].to_node.id == connections[j].to_node.id:
                    weight_difference += abs(self.species_connections[i].weight - connections[j].weight)      
        return weight_difference

    def add_to_species(self, bird):
        self.birds.append(bird)

    def sort_players_by_fitness(self):
        self.birds.sort(key=lambda x: x.score, reverse=True)
        
    def calculate_average_fitness(self):
        total_fitness = 0
        for bird in self.birds:
            total_fitness += bird.score
            
        self.average_fitness = total_fitness / len(self.birds)

    def child(self):
        # pick a random bird from the species without first bird
        if len(self.birds) > 1:
            child = random.choice(self.birds[1:]).clone()
        else:
            child = self.birds[0].clone()
        child.brain.mutate()
        return child