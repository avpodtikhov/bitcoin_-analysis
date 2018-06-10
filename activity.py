#!/usr/bin/python
import networkx as nx

print('begin')
G = nx.read_gexf("multig.gexf")
print('graph')
d = G.degree(G.nodes)
print('nodes loaded')
f = open('activity.txt', 'w')
for i in d:
    f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
f.close()
