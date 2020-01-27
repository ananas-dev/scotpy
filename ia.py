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

#def thief_move(thief_location, cops_location):    
#    thief_adjacent = g[cops_location].keys()
#    thief_possible_paths = []
#    thief_possible_paths_gen = nx.all_pairs_dijkstra_path(g)
   #thief_possible_paths = thief_possible_paths_gen[cops_location](thief_possible_paths()) 
#    map(thief_possibles_paths
#    print(thief_adjacent)
#    print(thief_possible_paths)

def cmove(clocation, tlocation):
    cops_path_gen = nx.all_pairs_dijkstra_path(g)
    cops_path = cops_path_gen[clocation][tlocation]
    clocation = cops_path[1] 
    return(clocation)
