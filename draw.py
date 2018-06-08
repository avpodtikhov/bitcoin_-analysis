#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf("4-core.gexf")
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()