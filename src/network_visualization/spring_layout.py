import sys
import re
import networkx as nx
import pandas as pd
import numpy as np
from UMAP_analysis.core import make_undirected
import matplotlib.pyplot as plt

path  = sys.argv[1]
m = re.match("networks/(?P<dataset>.*?)/(?P<name>.*?).gml", path)
dataset = m.groupdict()['dataset']
name = m.groupdict()['name']

G = nx.read_gml(path)
G = make_undirected(G)
ev = pd.read_csv(f"networks/{dataset}/eigenvectors/{name}.csv", index_col = 0)
e_values = ev.loc["lambda"]
ev = ev.loc[[i for i in ev.index if i != "lambda"]]

e_1 = sys.argv[2]
e_2 = sys.argv[3]

xy = nx.spring_layout(G, pos = {i:(ev.loc[i,e_1],ev.loc[i,e_2]) for i in G.nodes()})

fig = plt.figure(figsize = [20,20])
ax = fig.add_axes([0,0,1,1])
ax.axis('off')
nx.draw_networkx(G,
                 pos = xy,
                 with_labels = False,
                 node_size = 0,
                 alpha= 0.1,
                 ax = ax
                )

fig.savefig(f"figures/networks/{dataset}/{name}_spring_layout_{ev_1}_{ev_2}.svg")
