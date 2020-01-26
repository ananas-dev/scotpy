# File --config.py--
import networkx as nx # This program uses networkx 1.11 

# Graph 
nodes = [0, 1, 2, 3, 5, 6, 8, 9]
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (8, 9), (9, 0),
        (1, 3), (3, 5), (5, 7), (7, 9), (9, 1)]
def mkgraph(nodes, edges):
    g=nx.Graph() 
    g.add_nodes_from(nodes) # Adds nodes
    g.add_edges_from(edges) # Adds edges
    return(g)

# Number of Cops
cnum = 13
