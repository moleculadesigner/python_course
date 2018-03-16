import numpy as np

class Node:
    """
    A simple implementation of graph theory objects
    """
    def __init__(self, neighbors=None, name='node', content=None):
        if neighbors:
            self.neighbors = set(neighbors)
        else:
            self.neighbors = set()
        self.content = content
        self.name = name
        self.edges = set()
        for n in self.neighbors:
            n.neighbors.add(self)
            self.edges.add((self, n))
            n.edges.add((n, self))

    def __repr__(self):
        return "n.{}".format(self.name)

    def bind(self, node):
        self.neighbors.add(node)
        self.edges.add((self, node))
        node.neighbors.add(self)
        node.edges.add((node, self))

    @property
    def deg(self):
        return len(list(self.edges))


class Graph:
    """
    """

    def __init__(self, nodes=None, edges=None):
        if nodes:
            self.nodes = set(nodes)
        else:
            self.nodes = set()
        
        self.edges = set()
        for node in self.nodes:
            self.edges |= node.edges

        if edges:
            new_e = set(edges) - self.edges
            for n1, n2 in new_e:
                n1.bind(n2)

    def __repr__(self):
        return "{}{}{}".format('{', ", ".join(map(str, self.nodes)), '}')
            

a = Node(name='A')
b = Node([a], 'B')
c = Node([a], 'C')
print(Graph([a, b, c]))