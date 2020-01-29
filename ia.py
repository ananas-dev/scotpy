# File --ia.py--

import networkx as nx

import random
import config
import graphs

g = graphs.mkgraph(graphs.nodes, graphs.edges) # Makes the graph
Cnum = config.Cnum # Gets the number of cops

def tspawn():
    Tlocation = random.choice(graphs.nodes) # Random spawn
    return(Tlocation)

def cspawn(Tlocation): 
    while True:
        Clocation = random.choice(graphs.nodes) # Random spawn
        if Clocation != Tlocation: # Repeat if Cspawn = Tspawn
            break
    return(Clocation)

def tmove(Tlocation, Clocation):
    Tadj = g[Tlocation].keys() # Gets the nodes adjacents to the thief
    Tpaths = []
    # Finds the ajacent node who is the furthest to the policeman
    for x in Tadj:
        Tpaths.append(nx.shortest_path(g)[x][Clocation])
    Tpath = max(Tpaths, key=len)
    Tlocation = Tpath[0]
    return(Tlocation)
    

def cmove(Clocation, Tlocation):
    # Finds the shortest path to the thief
    Cpath = nx.shortest_path(g)[Clocation][Tlocation]
    Clocation = Cpath[1] 
    return(Clocation)
