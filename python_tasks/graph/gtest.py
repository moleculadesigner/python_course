import graph as g

adj = {
    'A': [('A', 1.4), ('B', -2.5), ('C', 0.3)],
    'B': [('A', 2.5), ('B', 4), ('D', 0.03)],
    'C': [('D', 0.5)],
    'D': [('F', 10.4)],
    'F': []
}
G = g.Graph(adj)

print(G)
print("\n{}\n{}\n".format(*(G.as_adj_matrix)))

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
print(G.as_dict)
print()
print(P.as_dict)