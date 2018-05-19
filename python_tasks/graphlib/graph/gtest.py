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
"""
A = np.around(2 * (np.random.sample((20, 20))))
t0 = datetime.datetime.now()
G = u.matrix_to_graph(A)
t1 = datetime.datetime.now()
print(t0,t1,(t1-t0).seconds)

u.dijkstra(G, 1)
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
    adjency=adj,
    weighted=True,
    oriented=True
)
"""
print(P)
print((P.adj_matrix(disjoined=np.inf)))
print(P.as_dict)
"""
print(u.dijkstra(P, 'A'))