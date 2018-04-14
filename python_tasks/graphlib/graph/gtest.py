import graph as g
import utils as u
import numpy as np

adj = {
    'A': [('A', 1.4), ('B', 2.5), ('C', 0.3)],
    'B': [('A', 2.5), ('A', 1), ('B', 4), ('D', 0.03)],
    'C': [('D', 0.5)],
    'D': [('F', 10.4)],
    'F': [],
    'G': []
}
G = g.Graph(
    adjency=adj,
    oriented=True,
    multi=True
)

print(G)
try:
    print("\n{}\n{}\n".format(*(G.adj_matrix(disjoined=np.inf))))
except NotImplementedError:
    pass
"""
uwadj = {
    'A': ['A', 'B', 'C'],
    'B': ['A', 'B', 'D'],
    'C': ['D'],
    'D': ['F']
}
P = g.Graph(
    adjency=uwadj,
    weighted=False,
    oriented=False
)

print(P)
print("\n{}\n{}\n".format(*(P.as_adj_matrix)))
print(P.as_dict)
"""
print("{}".format(u.dijkstra(G, "B", True)))