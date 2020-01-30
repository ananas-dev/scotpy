# File --ia.py--

import networkx as nx

import random
import config
import graphs

g = graphs.mkgraph(graphs.nodes, graphs.edges) # Makes the graph
Cnum = config.Cnum # Gets the number of cops

def Tspawn():
    Tlocation = random.choice(graphs.nodes) # Random spawn
    return(Tlocation)

def Cspawn(Tlocation): 
    while True:
        Clocation = random.choice(graphs.nodes) # Random spawn
        if Clocation != Tlocation: # Repeat if Cspawn = Tspawn
            break
    return(Clocation)

def Tmove(Tlocation, Clocation):
    Tadj = list(g[Tlocation].keys()) # Gets the nodes adjacents to the thief
    Tpaths = []
    # Finds the ajacent node who is the furthest to the policeman
    for x in Tadj:
        Tpaths.append(nx.shortest_path(g)[x][Clocation])
    maxlen = max(map(len, Tpaths))
    result = [x for x in Tpaths if len(x) == maxlen]
    Tpath = []
    for x in result:
        Tpath.append(x[0])
    Tpath_adj = []
    for x in Tpath:
        Tpath_adj.append(list(g[x].keys()))
    choose = Tpath_adj.index(max(Tpath_adj, key=len))
    Tlocation = Tpath[choose]
    return(Tlocation)
    

def Cmove(Clocation, Tlocation):
    # Finds the shortest path to the thief
    Cadj = list(g[Clocation].keys()) # Gets the nodes adjacents to the cops
    Cpaths = []
    # Finds the ajacent node who is the furthest to the thief
    for x in Cadj:
        Cpaths.append(nx.shortest_path(g)[x][Tlocation])
    minlen = min(map(len, Cpaths))
    result = [x for x in Cpaths if len(x) == minlen]
    Cpath = []
    for x in result:
        Cpath.append(x[0])
    Cpath_adj = []
    for x in Cpath:
        Cpath_adj.append(list(g[x].keys()))
    choose = Cpath_adj.index(max(Cpath_adj, key=len))
    Clocation = Cpath[choose]
    return(Clocation)
