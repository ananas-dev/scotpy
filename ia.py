# File --ia.py--

import networkx as nx
import random
import config
import graphs

g = graphs.mkgraph(graphs.nodes, graphs.edges) # Make the graph
cnum = config.cnum

def tspawn():
    tlocation = random.choice(graphs.nodes)
    print("thief spawn:",tlocation)
    return(tlocation)

def cspawn(tlocation): 
    while True:
        clocation = random.choice(graphs.nodes)
        if clocation != tlocation:
            break
    print("cops spawn:",clocation)
    return(clocation)

def tmove(tlocation, clocation):    
    tadj = g[clocation].keys()
    for x in tadj:
        tpaths = nx.shortest_path(g)[x][clocation]
        map
        print(tpaths)


#map(thief_possibles_paths
#    print(thief_adjacent)
#    print(thief_possible_paths)

def cmove(clocation, tlocation):
    cops_path = nx.shortest_path(g)[clocation][tlocation]
    clocation = cops_path[1] 
    return(clocation)
