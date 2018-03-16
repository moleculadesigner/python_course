import numpy as np

class Node:
    """
    A simple implementation of graph theory objects
    """
    def __init__(self, neighbors=[], name=None, content=None):
        self.neighbors = set(neighbors)
        if content:
            self.content = content
        if name:
            self.name = name
        else:
            self.name = (id(self) % 100000)

    def __repr__(self):
        return "n.{}".format(self.name)

    def bind(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)

    @property
    def deg(self):
        return len(list(self.neighbors))


class Graph:
    """
    """

    def __init__(self, nodes=[], edges=[]):
        self.nodes = set(nodes)
        
        self.edges = list()
        for node in self.nodes:
            for nb in node.neighbors:
                self.bind(node, nb) 
        for e in map(tuple, edges):
            if len(e) != 2:
                raise ValueError("Incorrect format of edge")
            if e[0] == e[1]:
                raise ValueError("Loops are not implemented yet, sorry.")
            self.bind(*e)

    def bind(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            n1.bind(n2)
            e = frozenset((n1, n2))
            if e not in self.edges:
                self.edges.append(e)

    def __repr__(self):
        V = ", ".join(map(str, self.nodes))
        E = ", ".join(map(lambda e: "({}, {})".format(*e), self.edges))
        return str("""<V, E>: <{{{}}},
         {{{}}}
        >""".format(V, E))

    @property
    def matrix(self):
        dim = len(self.nodes)
        m = np.zeros((dim, dim))
        nds = list(self.nodes)
        for i, node in enumerate(nds):
            for j, nb in enumerate(nds[i:]):
                if frozenset((node, nb)) in self.edges:
                    m[i, i + j] = 1
        return m + m.T
            

a = Node()
b = Node([a])
c = Node([a])
d = Node([a, b, c])
G = Graph([a, b, c, d], [(d, c)])
print(G)
print(G.matrix)