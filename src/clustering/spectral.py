import sys
import pandas as pd
import networkx as nx
import numpy as np



dataset = sys.argv[1]
noise_percent = sys.argv[2]


df = pd.read_csv(f"data/intermediate/{dataset}/features.csv", index_col=0)
deviations = df.std()
scaling_factor = int(noise_percent)/100
df = df+scaling_factor*np.random.randn(*df.shape)


import sklearn.cluster
model = sklearn.cluster.SpectralClustering(n_clusters=2)
clusters = model.fit_predict(df)
clusters = pd.Series(clusters, index = df.index)
clusters.to_csv(f"data/processed/clusters/{dataset}/spectral_noise_percent_{noise_percent}.csv")
