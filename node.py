import math

class Node:
    def __init__(self, id_number):
        self.id = id_number
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections = []

    def activate(self):
        if self.layer == 1:
            # Sigmoid activation function
            self.output_value = 1/(1+math.exp(-self.input_value))

        # Loop through connections and add input value to connected nodes
        for i in range(0, len(self.connections)):
            self.connections[i].to_node.input_value += self.connections[i].weight * self.output_value

    def clone(self):
        clone = Node(self.id)
        clone.layer = self.layer
        clone.input_value = self.input_value
        clone.output_value = self.output_value
        return clone








