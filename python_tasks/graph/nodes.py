from collections import namedtuple
from functools import reduce

Arrow = namedtuple('Arrow', ['start', 'end', 'w'])
Edge = namedtuple('Edge', ['nodes', 'w'])
ARROW = Arrow(None, None, None)
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
            raise ValueError("Invalid edge: {}.".format(edge))
    if type(edge) is type(ARROW):
        return [edge.start, edge.end]


def deprecated(fn):
    """Raises a `NotImplementedError` exception
     while attempting to call decorated function."""
    def wrapper(*args, **kwargs):
        raise NotImplementedError(
        """Function {}({}, {}) have not been implemented yet.
        """.format(fn, args, kwargs))
    return wrapper


class Node:
    """
    A basic type for graph node representation.
    """
    def __init__(self, name=None, children=[], content={}):
        if name:
            self.name = name
        else:
            self.name = str(id(self) % 100000)
        self.edges = []
        for node in set(children):
            self.grow(node)
        self._content = content

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
        ch = []
        for edge in self.edges:
            n = extract_nodes(edge)
            n.remove(self)
            ch.append(n.pop())
        return set(ch)

    @property
    def deg(self):
        return len(self.children)
    
    def grow(self, node, weight=None):
        if node in self.children:
            return None
        e = Edge(frozenset((self, node)), w=None)
        self.edges.append(e)
        if node is not self:
            node.edges.append(e)
        return e

    def drop(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            node = edge.nodes - set((self,))
            if node:
                node.pop().edges.remove(edge)

    def links(self, node):
        """returns list of edges linking to the `node`"""
        links = []
        for e in self.edges:
            if set((self, node)) ==  e.nodes:
                links.append(e)
        return links


class UNode(Node):
    """
    A node in unoriented graph.
    """
    def __init__(self, name=None, children=[],
            multi=False, content=None):
        Node.__init__(self, name=name, content=content)
        self.multi = multi
        self.edges = []
        for node, w in children:
            self.grow(node, w)

    def __repr__(self):
        return "\x1b[33m<>\x1b[0m{}".format(self.name)

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
        return reduce(lambda x, y: x + y[1],
                      self.children, 0)

    def grow(self, node, weight=1):
        """
        Addes edge to `node` with `weight`. If `node` is already linked
        does nothing, unless you are in multigraph mode.
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
        return "\x1b[35m>>\x1b[0m{}".format(self.name)

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
        """returns list of arrows heading to the `node`"""
        links = []
        for a in self.edges:
            if self is a.start and node is a.end:
                links.append(a)
        return links


@deprecated
def merge(edges, method=(lambda x, y: x + y)):
    if not edges:
        return []
    #else:
        #edges = cp.deepcopy(edges)
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
