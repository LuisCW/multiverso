class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for other_node in self.graph:
                self.graph[other_node] = [
                    neighbor for neighbor in self.graph[other_node] if neighbor != node
                ]

    def __str__(self):
        return str(self.graph)
