"""
graph.py module

Implements Graph object based on `nodes` module
"""

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

def find_node(graph, node_name:str):
    """
    Returns the first node object with name specified.
    Otherwise raises `StopIteration` exception.
    """
    return next((u for u in graph.nodes if u.name == node_name))

class Graph:
    """
    Graph object. Contains set of nodes and list of edges.
    """

    def __init__(self, adjency={}, # Dictionary of node connections
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
        
        # Unweighted graph sould be created implicitly.
        # Adjency dictionary must contain only node names in this case.
        adj_type = tuple if self.weighted else str

        # Determining multi graph mode unless specified
        if multi is None:
            for uname in adjency:
                for child in adjency[uname]:
                    if type(child) is not adj_type:
                        raise ValueError(EDGE_FORMAT_ERROR)
                    if adjency[uname].count(child) != 1:
                        self.multi = True # Otherwise leave it None
            self.multi = False
            # If self.multi is not None, nothing will happen
        
        # Dictionary to Graph
        for uname in adjency:
            if uname not in map(lambda n: n.name, self.nodes):
                # Create and add node of appropriate type
                U = self._nd_type(
                    name=uname,
                    multi=self.multi
                )
                self._nodes.add(U)
            else:
                # Normally there must be only one node with `uname`
                U = find_node(self, uname)

            for child in adjency[uname]:
                # linking children
                if type(child) is not adj_type:
                    raise ValueError(EDGE_FORMAT_ERROR)
                if adjency[uname].count(child) != 1 and\
                        not self.multi:
                    raise ValueError(MULTI_EDGE_ERROR.format(uname, child))
                if self.weighted:
                    ch_name, w = child
                else:
                    ch_name, w = child, None

                # Creating / finding child node
                if ch_name not in map(lambda n: n.name, self.nodes):
                    V = self._nd_type(
                        name=ch_name,
                        multi=self.multi
                    )
                    self._nodes.add(V)
                else:
                    V = find_node(self, ch_name)

                # Setting up the edge
                e = U.grow(node=V, weight=w)
                if e is not None:
                    self._edges.append(e)

    def __str__(self):
        """
        Representation of Graph object
        """
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
        """
        Make an edge with two existing nodes.
        """
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
        """
        Add an existing node without any edges.
        """
        if node.edges:
            raise ValueError(BOUND_NODE_ADD_ERROR)
        if type(self._nd_type()) is not type(node):
            raise TypeError("Inappropriate node type.")
        self.nodes.add(node)

    def new(self, name=None):
        """Wrapper to Graph.add().
        Adds empty node"""
        self.add(self._nd_type(
            name=name,
            multi=self.multi
            )
        )

    def cut(self, edge):
        """
        Removes an `edge` from Graph.
        """
        if edge not in self.edges:
            return None
        parent = nodes.extract_nodes(edge)[0]
        parent.drop(edge)
        self.edges.remove(edge)

    def remove(self, node):
        """
        Removes a `node` with all incident edges from Graph.
        """
        for edge in node.edges:
            self.cut(edge)
        self.nodes.remove(node)

    def disjoin(self, node1, node2):
        """
        Removes all edges between two nodes specified
        """
        for edge in node1.links(node2):
            self.cut(edge)

    def __repr__(self):
        return self.__str__()

    def adj_matrix(self, nlist=[], disjoined=0):
        """
        Returns list of nodes l and adjency matrix A,
        where Aij = w(l[i], l[j])

        disjoined nodes are weighted as specified in
        `disjoined` parameter
        """
        if self.multi:
            raise NotImplementedError(MULTI_MATRIX_ERROR)
        if nlist:
            nodes = nlist
        else:
            nodes = list(self.nodes)
        matrix = np.zeros((len(nodes), len(nodes))) + disjoined
        for i, nd in enumerate(nodes):
            for j, cd in enumerate(nodes):
                es = nd.links(cd)
                if len(es) == 1:
                    s = es[0].w
                    matrix[i, j] = s if s is not None else 1
        return nodes, matrix

    @property
    def as_dict(self):
        """
        Returns dictionary representation of Graph
        """
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