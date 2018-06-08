#!/usr/bin/python
import networkx as nx

G = nx.read_gexf("graph.gexf")
d = G.degree(G.nodes)
f = open('node_degrees.txt', 'w')
for i in d:
    f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
f.close()