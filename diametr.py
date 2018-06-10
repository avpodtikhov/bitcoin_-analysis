#!/usr/bin/python
import networkx as nx

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
G = G.to_undirected()
largest_cc = list(max(nx.connected_components(G)))
print("Max comp")
g = G.subgraph(largest_cc)
g1 = g.to_undirected()
print(nx.diameter(g1))