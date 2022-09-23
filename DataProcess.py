import numpy as np
import networkx as nx

npz_file = np.load('./Data/iSTNs_Years_ComCodes.npz')
Years, Hscodes, NotEconomy = npz_file['Years'], npz_file['Hscodes'], npz_file['NotEconomy']


# Hs code of maize seed: 100510, Hs code of rice seed: 100610
def GetGraph(Hscode, years):
    Graph = nx.read_gpickle(f'./Data/iSeedTradeNetwork_{Hscode}_{year}.gpickle')
    GraphNodes = Graph.nodes()
    RemoveNodes = []
    # Remove non-economy nodes
    for NonEcon in NotEconomy:
        if NonEcon in GraphNodes:
            RemoveNodes.append(NonEcon)
    # Remove invalid nodes without trade links
    for Gnode in GraphNodes:
        if nx.degree(Graph, nbunch=Gnode) == 0:
            RemoveNodes.append(Gnode)
    for Gnode in RemoveNodes:
        Graph.remove_node(Gnode)
    return Graph
