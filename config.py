# File --config.py--
import networkx as nx # This program uses networkx 1.11 

# Graph 
nodes = ([1, 2, 3, 4])
edges =([(1, 2), (2, 3), (3, 4), (4, 1)])
def mkgraph(nodes, edges):
    g=nx.Graph() 
    g.add_nodes_from(nodes) # Adds nodes
    g.add_edges_from(edges) # Adds edges
    return(g)
