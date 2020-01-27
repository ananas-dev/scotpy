# File --ia.py--

import networkx as nx
import random
import config
import graphs

g = graphs.mkgraph(graphs.nodes, graphs.edges) # Makes the graph
cnum = config.cnum # Gets the number of cops

def tspawn():
    tlocation = random.choice(graphs.nodes)
    return(tlocation)

def cspawn(tlocation): 
    while True:
        clocation = random.choice(graphs.nodes)
        if clocation != tlocation:
            break
    return(clocation)

def tmove(tlocation, clocation):    
    tadj = g[tlocation].keys()
    for x in tadj:
        tpaths = nx.shortest_path(g)[x][clocation]
        print(tpaths)

def cmove(clocation, tlocation):
    cops_path = nx.shortest_path(g)[clocation][tlocation]
    clocation = cops_path[1] 
    return(clocation)
