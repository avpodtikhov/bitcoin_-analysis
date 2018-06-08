#!/usr/bin/python
import networkx as nx

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
G = G.to_undirected()
largest_cc = max(nx.connected_components(G))
f = open('max_connected_comp.txt', 'w')
for i in largest_cc:
    f.write(str(i) + '\n')
f.close()