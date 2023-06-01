import random
import node
import connection


class Brain:
    def __init__(self, inputs, clone=False):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.net = []
        self.layers = 2

        if not clone:
            # Create input nodes
            for i in range(0, self.inputs):
                self.nodes.append(node.Node(i))
                self.nodes[i].layer = 0
            # Create bias node
            self.nodes.append(node.Node(3))
            self.nodes[3].layer = 0
            # Set bias node output value
            self.nodes[3].output_value = 1
            # Create output node
            self.nodes.append(node.Node(4))
            self.nodes[4].layer = 1

            # Create connections
            for i in range(0, 4):
                self.connections.append(connection.Connection(self.nodes[i],
                                                              self.nodes[4],
                                                              random.uniform(-1, 1)))

    def connect_nodes(self):
        # Reset node connections
        for i in range(0, len(self.nodes)):
            self.nodes[i].connections = []

        # Connect nodes
        for i in range(0, len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])

    def generate_net(self):
        self.connect_nodes()
        self.net = []
        for j in range(0, self.layers):
            for i in range(0, len(self.nodes)):
                if self.nodes[i].layer == j:
                    self.net.append(self.nodes[i])

    def feed_forward(self, vision):
        # Set input values
        for i in range(0, self.inputs):
            self.nodes[i].output_value = vision[i]

        # Set bias node output value
        self.nodes[3].output_value = 1

        for i in range(0, len(self.net)):
            self.net[i].activate()

        # Get output value from output node
        output_value = self.nodes[4].output_value

        # clear output node
        # self.nodes[4].input_value = 0

        # clear nodes
        for i in range(0, len(self.nodes)):
            self.nodes[i].input_value = 0

        return output_value

    def getNode(self, id):
        for n in self.nodes:
            if n.id == id:
                return n
            
    def get_connections(self):
        return self.connections
    
    def clone(self):
        clone = Brain(self.inputs, True)
        for i in range(0, len(self.nodes)):
            clone.nodes.append(self.nodes[i].clone())
        for c in self.connections:
            clone.connections.append(c.clone(clone.getNode(c.from_node.id), clone.getNode(c.to_node.id)))
        
        return clone
    
    def mutate(self):
        chance = random.uniform(0, 1) 

        if (chance > 0.2):
            for i in range(0, len(self.connections)):
                if random.uniform(0, 1) > 0.5:
                    self.connections[i].weight = self.connections[i].weight + random.uniform(-0.5, 0.5)
                    if self.connections[i].weight > 1:
                        self.connections[i].weight = 1
                    elif self.connections[i].weight < -1:
                        self.connections[i].weight = -1
            