import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from copy import deepcopy

A = np.around(0.75*(np.random.sample((8, 8))))
W = A + A.T - 2 * np.diag(A.diagonal())
U = deepcopy(W)
W[np.where(W == 0)] = np.inf
np.fill_diagonal(W, 0)

def bellman_ford(W, debug=False):
    As = list()
    Ps = list()
    for s in range(W.shape[0]):
        #print("v = {}".format(v))
        As.append(np.zeros(W.shape) + np.inf)
        #print("Init:\n{}".format(As[v]))
        Ps.append(np.zeros(W.shape, dtype=int))
        As[s][s, 0] = 0
        for i in range(W.shape[0]):
            #print("i = {}".format(i))
            for u, v in ((u, v) for u in range(W.shape[0])\
                for v in range(W.shape[0])):
                #print("u, w = {}".format((u,w)))
                if W[u, v] != np.inf:
                    if As[s][v, i] > As[s][u, i - 1] + W[u, v]:
                        #print("Matrix:\n{}\nW[u, w] = {}\n".format(As[v], W[u, w]))
                        As[s][v, i] = As[s][u, i - 1] + W[u, v]
                        Ps[s][v, i] = u
                    else:
                        #print("As[v][w, i] < As[v][u, i - 1] + W[u, w]")
                        pass
                else:
                    #print("inf")
                    pass
        if debug:
            print("s = {}".format(s))
            print("A\n{}\nP\n{}\n".format(As[s], Ps[s]))
    return list(zip(As, Ps))

def path_BF(W, s, i):
    A, P = bellman_ford(W)[s]
    jm = (np.argmin(A[i,:]))
    p = [0 for j in range(jm)]
    for j in range(jm -1, -1, -1):
        p[j] = i
        i = P[i, j]
    return p

print("W:\n{}\n".format(W))
bellman_ford(W)
s = []
for i, j in [(i, j) for i in range(W.shape[0]) for j in range(W.shape[0])]:
    s.append("({}, {}): {}".format(i, j, path_BF(W, i, j)))
print('=========\n\n')
print("\n".join(s))

def main():
    G = nx.from_numpy_matrix(U)
    nx.draw(G, with_labels=True)
    plt.show()
    return 0

if __name__ == '__main__':
    main()