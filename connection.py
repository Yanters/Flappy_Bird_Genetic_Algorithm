
class Connection:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def clone(self, from_node, to_node):
        clone = Connection(from_node, to_node, self.weight)
        return clone
