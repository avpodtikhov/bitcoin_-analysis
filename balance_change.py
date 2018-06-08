#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("graph.gexf")
print("Graph has loaded")
num = nx.number_of_nodes(G)
v = G.nodes
print(num)
f = open("balance_change.txt", "w")
for i in v:
    out = G.out_edges(nbunch = i, data = True)
    w = 0
    for o in out:
        w -= o[2]['weight']
    inp = G.in_edges(nbunch = i, data = True)
    for j in inp:
        w += j[2]['weight']
    f.write(str(i) + ' ' + str(w) + '\n')
f.close()
