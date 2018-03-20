import nodes
import numpy as np

# Utilities
EDGE_FORMAT_ERROR = "Wrong edge format. Must be either srting or tuple \
(str, float)."

MULTI_MODE_ERROR = "Trying to assign more then one edge connecting nodes \
{} and {} in non-multi graph."

class Graph:
    """
    """

    def __init__(self, adjency={},
            oriented=True, weighted=True, multi=None):
        self._multi = multi
        self._oriented = oriented
        self._weighted = weighted
        self._nodes = set()
        self._edges = []

        if self.oriented:
            nd_type = nodes.ONode
        else:
            nd_type = nodes.UNode
        adj_type = tuple if self.weighted else str

        if multi is None:
            for uname in adjency:
                for child in adjency[uname]:
                    if type(child) is not adj_type:
                        raise ValueError(EDGE_FORMAT_ERROR)
                    if adjency[uname].count(child) != 1:
                        self.multi = True
            self.multi = False
        
        for uname in adjency:
            if uname not in map(lambda n: n.name, self.nodes):
                U = nd_type(
                    name=uname,
                    multi=self.multi
                )
            for child in adjency[uname]:
                if type(child) is not adj_type:
                    raise ValueError(EDGE_FORMAT_ERROR)
                if adjency[uname].count(child) != 1 and\
                        not self.multi:
                    raise ValueError(MULTI_MODE_ERROR.format(uname, child))
                if self.weighted:
                    pass
        
    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    # multi attribute properties
    def get_multi(self):
        return self._multi

    def set_multi(self, value):
        if type(value) is not bool:
            raise ValueError(
                "Reiqured True or False implicitly instead of {}.".format(value))
        if (self._multi is None):
            self._multi = value
        else:
            print("\x1b[31mWarning\x1b[0m" +
                  ": Converting graph multiness is restricted.")
        
    multi = property(
        fget=get_multi,
        fset=set_multi,
        doc="Multigraph property handilng."
    )

    @property
    def oriented(self):
        return self._oriented

    @property
    def weighted(self):
        return self._weighted

    def bind(self, n1, n2):
        pass

    def add(self, node):
        pass

    def __repr__(self):
        pass

    @property
    def matrix(self):
        pass


if __name__ == '__main__':
    G = Graph(multi=True)
    I = Graph(multi=False)
    H = Graph()
    G.multi = False
    print(H.multi)
