import numpy as np
from collections import namedtuple, defaultdict
from functools import reduce
import copy as cp

Arrow = namedtuple('Arrow', ['start', 'end', 'w'])
Edge = namedtuple('Edge', ['nodes', 'w'])
ARROW = Arrow(None, None, None)
EDGE = Edge(frozenset((None,)), None)


class Node:
    """
    A basic type for graph node representation.
    """
    def __init__(self, children=[],
            name=None, content=None):
        if name:
            self.name = name
        else:
            self.name = id(self) % 10000
        self.edges = []
        for node in set(children):
            self.grow(node)
        if content:
            self.content = content

    def __repr__(self):
        return "v.{}".format(self.name)

    @property
    def children(self):
        return set([
            (n.pop() if len(n) == 1 else self) for\
            n in map(lambda x: set(x.nodes) - set((self,)), self.edges)
        ])

    @property
    def deg(self):
        return len(self.children)
    
    def grow(self, node, weight=None):
        if node in self.children:
            return None
        e = Edge(frozenset((self, node)), None)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)

    def drop(self, node):
        for edge in self.edges:
            if set((self, node)) == edge.nodes:
                self.edges.remove(edge)
                if node is not self:
                    node.edges.remove(edge)


class UNode(Node):
    """
    A node in unoriented graph
    """
    def __init__(self, name=None, children=[],
            multi=False, content=None):
        Node.__init__(self, name=name, content=content)
        self.multi = multi
        self.edges = []
        for node, w in children:
            self.grow(node, w)

    def __repr__(self):
        return "u.{}".format(self.name)

    @property
    def children(self):
        ch = []
        for e in self.edges:
            if set((self,)) == e.nodes:
                ch.append((self, e.w))
            else:
                n = set(e.nodes) - set((self,))
                ch.append((
                    n.pop(),
                    e.w
                ))
        return ch

    @property
    def deg(self):
        return reduce(lambda x, y: x + y[1],
                      self.children, 0)

    def grow(self, node, weight=1):
        if not self.multi and node in map(lambda x: x[0], self.children):
            return None
        e = Edge(set((self, node)), weight)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)




def merge(edges, method=(lambda x, y: x + y)):
    if not edges:
        return []
    else:
        edges = cp.deepcopy(edges)
    t = type(edges[0])
    out = []
    if t is type(EDGE):
        for i, e in enumerate(edges):
            weight = e.w
            if e is EDGE:
                continue
            for j, ee in enumerate(edges[i+1:]):
                if e.nodes == ee.nodes:
                    weight = method(weight, ee.w)
                    edges[i + j + 1] = EDGE
            out.append(Edge(e.nodes, weight))
        del(edges)
        return out


if __name__ == '__main__':
    a = UNode('a')
    b = UNode('b')
    print(b.children)

    c = UNode('c', [(a, 5), (b, 1), (a, 4)])
    print(b.children)
    b.grow(c, 3)
    print(b.children)
    print(c.children)
    """
    aa = Node()
    ab = Node()
    ac = Node([aa, ab, aa, aa])
    print(ac)
    print(ac.edges)
    print(ac.children)
    """