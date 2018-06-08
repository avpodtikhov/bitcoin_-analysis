#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
G1 = G.to_undirected()
k = nx.average_clustering(G1)
f = open('cluster_index.txt', 'w')
f.write(str(k) + '\n')
f.close()
