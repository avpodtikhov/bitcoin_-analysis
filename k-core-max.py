#!/usr/bin/python
from networkx.algorithms import approximation as apxa
import networkx as nx
import random

G1 = nx.read_gexf("graph.gexf")
print("Graph has loaded")
G1.remove_edges_from(nx.selfloop_edges(G1))
G = G1.to_undirected()
for i in range(100):
    if (i < 2):
        continue
    print(str(i) + " Is counting...")
    k_core = nx.k_core(G, k=i)
    if (k_core.order() == 0):
        break
    else:
        nx.write_gexf(k_core, "max-core.gexf")