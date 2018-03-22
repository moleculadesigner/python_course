import nodes
import numpy as np

# Messages
EDGE_FORMAT_ERROR = "Wrong edge format. Must be either srting or tuple \
(str, float)."

MULTI_EDGE_ERROR = "Trying to assign more then one edge connecting nodes \
{} and {} in non-multi graph."

NODE_NOT_IN_GRAPH_ERROR = "Both binding nodes \
must be in graph. Use add(node) method before bininding."

BOUND_NODE_ADD_ERROR = "Only nodes without edges are allowed to add. \
Use bind() method for adding edges."

MULTI_MATRIX_ERROR = "Trying to get adjancy matrix from multigraph. \
This function is not implemented yet due to edge merging ambiguity"

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
            self._nd_type = nodes.ONode
        else:
            self._nd_type = nodes.UNode
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
                U = self._nd_type(
                    name=uname,
                    multi=self.multi
                )
                self._nodes.add(U)
            else:
                U = next((u for u in self._nodes if u.name == uname))

            for child in adjency[uname]:
                if type(child) is not adj_type:
                    raise ValueError(EDGE_FORMAT_ERROR)
                if adjency[uname].count(child) != 1 and\
                        not self.multi:
                    raise ValueError(MULTI_EDGE_ERROR.format(uname, child))
                if self.weighted:
                    ch_name, w = child
                else:
                    ch_name, w = child, None

                if ch_name not in map(lambda n: n.name, self.nodes):
                    V = self._nd_type(
                        name=ch_name,
                        multi=self.multi
                    )
                    self._nodes.add(V)
                else:
                    V = next((u for u in self._nodes if u.name == ch_name))

                e = U.grow(node=V, weight=w)
                if e is not None:
                    self._edges.append(e)

    def __str__(self):
        nds = ", ".join([str(v) for v in self.nodes])
        eds = ",\n    ".join([str(e) for e in self.edges])
        return "Graph <V, E>:\n   {{{}}}\n   {{{}}}".format(nds, eds)
        
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

    def join(self, snode, enode, weight=None):
        if not (snode in self.nodes and\
                enode in self.nodes):
            raise ValueError(NODE_NOT_IN_GRAPH_ERROR)
        if self.weighted and weight is None:
            e = snode.grow(enode)
        else:
            e = snode.grow(enode, weight)
        if e is not None:
            self.edges.append(e)

    def add(self, node):
        if node.edges:
            raise ValueError(BOUND_NODE_ADD_ERROR)
        if type(self._nd_type()) is not type(node):
            raise TypeError("Inappropriate node type.")
        self.nodes.add(node)

    def cut(self, edge):
        if edge not in self.edges:
            return None
        parent = nodes.extract_nodes(edge)[0]
        parent.drop(edge)
        self.edges.remove(edge)

    def remove(self, node):
        for edge in node.edges:
            parent = nodes.extract_nodes(edge)[0]
            parent.drop(edge)
        self.nodes.remove(node)

    def disjoin(self, node1, node2):
        for edge in node1.links(node2):
            self.cut(edge)

    def __repr__(self):
        return self.__str__()

    @property
    def as_adj_matrix(self):
        if self.multi:
            raise NotImplementedError(MULTI_MATRIX_ERROR)
        nodes = list(self.nodes)
        _matrix = np.zeros((len(nodes), len(nodes)))
        for i, nd in enumerate(nodes):
            for j, cd in enumerate(nodes):
                es = nd.links(cd)
                #print("{} {}: {}".format(nd, cd, es))
                if len(es) == 1:
                    s = es[0].w
                    _matrix[i, j] = s if s is not None else 1
        return nodes, _matrix

    @property
    def as_dict(self):
        d = {}
        for node in self.nodes:
            d[node.name] = []
            for e in node.edges:
                if self.oriented:
                    if e.start is node:
                        d[node.name].append((e.end.name, e.w))
                else:
                    n = nodes.extract_nodes(e)
                    n.remove(node)
                    cd = n[0]
                    d[node.name].append((cd.name, e.w))
        return d


if __name__ == '__main__':
    print("node.py module implements Graph() object.")