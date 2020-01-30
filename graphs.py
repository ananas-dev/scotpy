# File --graphs.py--

import networkx as nx
import config

# Sets nodes and egdes of choosen graph
nodes = config.graph["nodes"]
edges = config.graph["edges"]


# Make the graph
def mkgraph(nodes, edges):
    g=nx.Graph() 
    g.add_nodes_from(nodes) # Adds nodes
    g.add_edges_from(edges) # Adds edges
    return(g)

