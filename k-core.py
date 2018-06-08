#!/usr/bin/python
from networkx.algorithms import approximation as apxa
import networkx as nx
import random

G1 = nx.read_gexf("graph.gexf")
print("Graph has loaded")
G1.remove_edges_from(nx.selfloop_edges(G1))
G = G1.to_undirected()
k_core = nx.k_core(G, k=2)
print("2-core")
nx.write_gexf(k_core, "2-core.gexf")
print("2-core has written!")
k_core = nx.k_core(G, k=3)
print("3-core")
nx.write_gexf(k_core, "3-core.gexf")
print("3-core has written!")
k_core = nx.k_core(G, k=4)
print("4-core")
nx.write_gexf(k_core, "4-core.gexf")
print("4-core has written!")