import graph
import nodes
import numpy as np
from heapq import heappush

from collections import defaultdict

def bellman_ford(G, node_name, loops=False):
    """
    If `loops`, we cannot stay in our start node
    unless it has loop edge. So path from node A to itself
    will be `([], inf)` if we don't have A -> A edge/arrow.

    Default A -> A path would be `([>>A], 0)` in this case.
    """
    # Initialization
    node = graph.find_node(G, node_name)
    nlist = [node] + sorted(
        list(G.nodes - set((node,))),
        key=lambda n: n.name)
    shape = len(nlist), len(nlist)
    A = np.zeros(shape) + np.inf
    A[0, 0] = 0
    P = np.zeros(shape, dtype=int)
    # Making A matrix (weight by edges)
    for i in range(1, len(nlist)-1):
        for e in G.edges:
            u, v = map(nlist.index, nodes.extract_nodes(e))
            if A[v, i] > A[u, i-1] + e.w:
                #print(i, nlist[u], nlist[v] ,A[v, i], A[u, i-1] + e.w)
                A[v, i] = A[u, i-1] + e.w
                P[v, i] = u
            if not G.oriented:
                v, u = map(nlist.index, nodes.extract_nodes(e))
                if A[v, i] > A[u, i-1] + e.w:
                    #print(i, nlist[u], nlist[v] ,A[v, i], A[u, i-1] + e.w)
                    A[v, i] = A[u, i-1] + e.w
                    P[v, i] = u
    # Path
    path = {}
    for i, nd in enumerate(nlist):
        if nd is node and loops:
            if node.links(node):
                path[nd] = [node], node.links(node)[0].w
            else:
                path[nd] = ([], np.inf)
            continue
        jm = (np.argmin(A[i,:]))
        #print(A[i,jm])
        weight = A[i,jm]
        if weight == np.inf:
            path[nd] = ([], np.inf)
            continue
        p = [None for j in range(jm)]
        for j in range(jm -1, -1, -1):
            p[j] = nlist[i]
            i = P[i, j + 1]
        path[nd] = ([node] + p, weight)
    return path


def dijkstra(G, node_name, loops=False):
    # Check for negative edges
    for e in G.edges:
        if e.w < 0:
            raise ValueError("""
            Graph contains negative edges.
            Dijkstra is impossible.""")
    # Initialization
    node = graph.find_node(G, node_name)
    nlist = [node] + sorted(
        list(G.nodes - set((node,))),
        key=lambda n: n.name)

    def empty_path():
        return np.inf, []    
    d = defaultdict(empty_path)
    d[node] = 0, [node]
  
    # Main iterations
    while nlist:
        nd = nlist.pop(0)
        #print("Node: {}".format(nd))
        for child, w in nd.children:
            if d[child][0] > d[nd][0] + w:
                d[child] = (
                    d[nd][0] + w,
                    d[nd][1] + [child]
                )

    if loops: # Root node loop processing
        lps = sorted(# Start node loop list
            node.links(node),
            key=lambda e: e.w)
        if lps:
            d[node] = lps[0].w, [node]
        else:
            d[node] = empty_path()
    return d


def matrix_to_graph(A, oriented=True, weighted=True, disjoined=0):
    # Matrix test
    if len(A.shape) != 2:
        raise ValueError("Inappropriate matrix dimension.")
    m, n = A.shape
    if m != n:
        raise ValueError("Matrix must be square")

    #Graph init
    G = graph.Graph(
        oriented=oriented,
        weighted=weighted,
        multi=False
    )
    for i in range(n):
        G.new(i)

    def js(i):
        return range(n) if oriented \
            else range(i, n)
    nodes = sorted(
        list(G.nodes),
        key=lambda n: n.name)
    
    for i in range(n):
        for j in js(i):
            if A[i, j] != disjoined:
                G.join(nodes[i], nodes[j], A[i, j])
    
    return G