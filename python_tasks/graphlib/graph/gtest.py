import graph as g
import utils as u
import numpy as np
import datetime
adj = {
    'A': [('A', 1.4), ('B', 2.5), ('C', 0.3)],
    'B': [('A', 2.5), ('A', 1), ('B', 4), ('D', 0.03)],
    'C': [('D', 0.5)],
    'D': [('F', 10.4)],
    'F': [],
    'G': []
}

P = g.Graph(
    adjency=adj,
    weighted=True,
    oriented=True
)
print(P)
print((P.adj_matrix(disjoined=np.inf)))
print(P.as_dict)
print(u.dijkstra(P, 'A'))