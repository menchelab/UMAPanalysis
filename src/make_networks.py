import sys
import pandas as pd
import networkx as nx
import numpy as np


from UMAP_analysis.core import umap_network, scaled_transition, eigenvalues, largest_connected_component


dataset = sys.argv[1]
n = int(sys.argv[2])


df = pd.read_csv(f"data/intermediate/{dataset}/features.csv", index_col=0)
deviations = df.std()


G = umap_network(df, n)
nx.write_gml(G,f"networks/{dataset}/nearest_neighbors_{n}.gml")


nodes = largest_connected_component(G)
transition = scaled_transition(G, nodes)
evecs = eigenvalues(transition, nodes)
evecs.to_csv( f"networks/{dataset}/eigenvectors/nearest_neighbors_{n}.csv")
