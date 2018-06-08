#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
nodes = nx.eigenvector_centrality(G)
f = open('eigenvector_centrality.txt', 'w')
for i in nodes:
    f.write(str(i) + ' ' + str(nodes[i]) +  '\n')
f.close()