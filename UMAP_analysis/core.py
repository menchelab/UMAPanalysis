import sys
import umap
import numpy as np
import pandas as pd
import networkx as nx
import scipy.sparse


def umap_network(df, nn, metric = 'manhattan'):
    """ """
    rndstate = np.random.RandomState()
    knn_net = umap.umap_.fuzzy_simplicial_set(df.values, nn, rndstate, metric)
    G = nx.from_numpy_array(knn_net[0].toarray(), create_using = nx.DiGraph)
    num_to_id = dict(enumerate(df.index))
    return nx.relabel_nodes(G, num_to_id.get)

def scaled_transition(G, nodes = None):
    if nodes == None:
        nodes = list(G.nodes())
    else:
        G = G.subgraph(nodes)

    A = nx.adjacency_matrix(G)
    temp = G.out_degree(weight = 'weight')
    degree = [temp[i] for i in nodes]
    scaling =  scipy.sparse.diags([1/i if i!=0 else 0 for i in degree])
    scaled = scaling * A
    return scaled

def eigenvalues(scaled, nodes, k = 10):
    eval_, evec = scipy.sparse.linalg.eigs(scaled, k = k)

    eval_ = np.real(eval_)
    evec = np.real(evec)

    evec = pd.DataFrame(evec)
    evec.index = nodes
    evec.loc["lambda",:] = eval_
    evec[np.argsort(eval_)[::-1]]
    return evec

def make_undirected(G):
    out = []
    G_u = G.to_undirected()
    for edge in G_u.edges():
        i,j = edge
        try:
            w = G[(j,i)]['weight']
            G_u[(i,j)]['weight'] += w
        except KeyError:
            pass
    return G_u

def propagate(propagator, nodes, labels):
    out = []
    out_time = []
    for i,x in enumerate(labels.columns):
        start = time.time()
        v = scipy.sparse.csc_matrix(labels.loc[list(nodes), x].values.reshape(-1, 1))
        temp = pd.Series((propagator * v).toarray().ravel())
        temp.name = x
        out.append(temp)
        stop = time.time()
        out_time.append(stop-start)

    df = pd.concat(out, axis=1)
    df.index = nodes
    df_time = pd.Series(out_time, name="Time", index=labels.columns)

    return df, df_time


def nearest_neighbor(G,labels):
    out = {}
    for node in G.nodes():
        neighbors = list(G[node].keys())
        neighbor_labels = labels.loc[neighbors]

        if len(neighbors) > 0:
            nearest_neighbor = max(neighbors, key=lambda x: G[node][x]['weight'])
            prediction = labels.loc[nearest_neighbor]
        else:
            prediction = 0
        out[node] = prediction
    return out

def largest_connected_component(G):
    l = nx.weakly_connected_components(G)
    return max(l,key=lambda x:len(x))

