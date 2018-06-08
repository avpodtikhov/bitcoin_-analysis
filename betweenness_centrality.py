#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
nodes = nx.betweenness_centrality(G, k = 5000)
f = open('betweeness_centrality.txt', 'w')
for i in nodes:
    f.write(str(i) + ' ' + str(nodes[i]) +  '\n')
f.close()