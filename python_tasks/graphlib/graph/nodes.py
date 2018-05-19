"""
nodes.py module
Implements some graph node classes:

Node (basic node type, unoriented, unweighted, non-multi)
|- ONode (oriented, weighted)
|- UNode (unoriented, weighted)
"""

from collections import namedtuple
from functools import reduce

# Edge types
# Oriented
Arrow = namedtuple('Arrow', ['start', 'end', 'w'])
ARROW = Arrow(None, None, None)
# Unoriented
Edge = namedtuple('Edge', ['nodes', 'w'])
EDGE = Edge(frozenset((None,)), None)


def extract_nodes(edge):
    """
    Return list of nodes connected by `edge`.

    Implemented for maintaining Arrow | Edge
    polymorphism.
    """
    if type(edge) is type(EDGE):
        if len(edge.nodes) == 1:
            node = list(edge.nodes).pop()
            return [node, node]
        elif len(edge.nodes) == 2:
            return list(edge.nodes)
        else:
            raise ValueError(f"Invalid edge: {edge}.")
    if type(edge) is type(ARROW):
        return [edge.start, edge.end]


class Node:
    """
    A basic type for graph node representation.
    """
    def __init__(self, name=None, children=[], content={}):
        if name is not None:
            self.name = name
        else: # Default name is derived from oject ID
            self.name = str(id(self) % 100000)
        self.edges = []
        for node in set(children):
            self.grow(node)
        self._content = content

    # Handling Node content dictionary
    def _get_content(self):
        return self._content
    def _set_content(self, upd_dict:dict):
        if self._content is None:
            self._content = dict()
        upd_dict = dict(upd_dict)
        for k in upd_dict:
            self._content[k] = upd_dict[k]        
    content = property(
        fget=_get_content,
        fset=_set_content
    )

    def __repr__(self):
        return ".{}".format(self.name)

    @property
    def children(self):
        """
        Return a set of tuples: (connected nodes, None)
        """
        ch = []
        for edge in self.edges:
            n = extract_nodes(edge)
            n.remove(self)
            ch.append((n.pop(), None))
        return set(ch)

    @property
    def deg(self):
        """
        Node degree (number of incident edges)
        """
        return len(self.children) # Because this is always non-multi graph
    
    def grow(self, node, weight=None):
        """
        Add an edge to `node` and return it.
        
        `weight` is ignored for this case.
        """
        if node in self.children:
            return None
        e = Edge(frozenset((self, node)), w=None)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)
        return e

    def drop(self, edge):
        """
        Removes the `edge` and unpair node and child.
        """
        if edge in self.edges:
            self.edges.remove(edge)
            node = edge.nodes - set((self,))
            if node:
                node.pop().edges.remove(edge)

    def links(self, node):
        """returns list of edges linking to the `node`."""
        links = []
        for e in self.edges:
            if set((self, node)) ==  e.nodes:
                links.append(e)
        return links


class UNode(Node):
    """
    A node in unoriented graph.

    Can be weighted, allow multi graph junctions and loops.
    """
    def __init__(self, name=None, children=[],
            multi=False, content=None):
        # UNode is a successor of simple Node
        Node.__init__(self, name=name, content=content)
        self.multi = multi
        self.edges = []
        for node, w in children:
            self.grow(node, w)

    def __repr__(self):
        return "<>{}".format(self.name)

    @property
    def children(self):
        """Returns list of tuples for
        all connected nodes and their weights."""
        ch = []
        for e in self.edges:
            n = extract_nodes(e)
            n.remove(self)
            ch.append((
                n.pop(),
                e.w
            ))
        return ch

    @property
    def deg(self):
        """
        Returns degree of the node:

        deg(v) = sum(w(e | e is incident to v))
        """
        return reduce(
            lambda x, y: x + y[1],
            self.children, 0)

    def grow(self, node, weight=1):
        """
        Addes edge to `node` with `weight`. If `node` is already linked
        does nothing, unless you are in multigraph mode.

        Return edge created.
        """
        if not self.multi and node in map(lambda x: x[0], self.children):
            return None
        e = Edge(set((self, node)), weight)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)
        return e


class ONode(Node):
    """
    A node in oriented graph.
    """
    def __init__(self, name=None, children=[],
            multi=False, content=None):
        Node.__init__(self, name=name, content=content)
        self.multi = multi
        self.edges = []
        for node, w in children:
            self.grow(node, w)

    def __repr__(self):
        return ">>{}".format(self.name)

    @property
    def children(self):
        """Returns list of tuples for
        all child nodes and their weights."""
        ch = []
        for e in self.edges:
            if e.start is self:
                ch.append((
                    e.end,
                    e.w)
                )
        return ch

    @property
    def parents(self):
        """Returns list of tuples for
        all parent nodes and their weights."""
        p = []
        for e in self.edges:
            if e.end is self:
                p.append((
                    e.start,
                    e.w)
                )
        return p

    @property
    def deg(self):
        """
        Returns degree of the node:

        deg(v) = sum(w(e | e is incident to v))
        """
        return reduce(lambda x, y: x + y[1],
                      self.children, 0)

    def grow(self, node, weight=1):
        """
        Addes edge to `node` with `weight`. If `node` is already linked
        does nothing, unless you are in multigraph mode.
        """
        if not self.multi and node in map(lambda x: x[0], self.children):
            return None
        e = Arrow(self, node, weight)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)
        return e

    def drop(self, arrow):
        if arrow in self.edges:
            self.edges.remove(arrow)
            if arrow.end is not self:
                arrow.end.edges.remove(arrow)

    def links(self, node):
        """
        Returns list of arrows heading to the `node`
        
        `self` -> `node` only
        """
        links = []
        for a in self.edges:
            if self is a.start and node is a.end:
                links.append(a)
        return links


if __name__ == '__main__':
    # Some demo
    a = ONode('a')
    b = ONode('b')
    print(b.children)

    c = ONode('c', [(a, 5), (b, 1), (a, 4)])
    b.grow(c, 3)
    print(c.edges)
    c.drop(c.links(a)[0])
    print(c.edges)
    print(a.edges)
    
    """
    """
    aa = Node('A')
    ab = Node('B')
    ac = Node('C', [aa, ab, aa, aa])
    print(ac.children)
    print(ac.edges)
    print(ac.links(aa))
