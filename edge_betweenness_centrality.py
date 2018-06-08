#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
print(G.number_of_nodes())
print(G.number_of_edges())
nodes = nx.edge_betweenness_centrality(G, k=2000)
f = open('edge_betweenness_centrality.txt', 'w')
for i in nodes:
    f.write(str(i) + ' ' + str(nodes[i]) +  '\n')
f.close()