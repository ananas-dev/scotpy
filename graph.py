# File --graphs.py--

import networkx as nx

##########
# Graphs #
##########

# The names of the nodes of the graphs follow this logic:
#
# 01 o-----o 11    01 o-----o 11        
#    |     |          |     |\  
#    |     |          |     | \          
# 00 o-----o 10    00 o-----o--o 02
#                          10
# So 10 -> 10
#    01 -> 01
#    20 -> 20
#    02 -> 02
#
# If the graph has 3 dimensions:
#    
#  101 o-----o 111         So 100 -> 100
# 100->|\o---|\o 110          010 -> 10
#      | |   | |              001 -> 1
#  001 o-|---o\|<-011 
#       \o-----o  
#       000   010 


# The star is the only graph who doesn't use the graph notation method

# Star
star = {
    "name"  : "star", 
    "nodes" : [0, 1, 2, 3, 5, 6, 8, 9],
    "edges" : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0),
               (1, 3), (3, 5), (5, 7), (7, 9), (9, 1)]
}

# Square
square = {
    "name"  : "square",
    "nodes" : [0, 1, 11, 10],
    "edges" : [(0, 1), (1, 11), (11, 10), (10, 0)]
}

# Triangle
triangle = {
    "name"  : "triangle",
    "nodes" : [1, 0, 10],
    "edges" : [(1, 0), (0, 10), (10, 1)]
}

# House

house = {
    "name"  : "house",
    "nodes" : [0, 1, 11, 10, 20],
    "edges" : [(0, 1), (1, 11), (11, 10), (10, 0),
               (0, 20), (20, 10)]
}

# Cube

cube = {
    "name"  : "cube",
    "nodes" : [0, 100, 110, 10,  # Floor 1
               1, 101, 111, 11], # Floor 2
    "edges" : [(0, 100), (100, 110), (110, 10), (10, 0),  # Floor 1
               (1, 101), (101, 111), (111, 11), (11, 1),  # Floor 2
               (0, 1), (100, 101), (110, 111), (10, 11)]  # Links floor 1 to floor 2 
}

# Scotland Yard Junior
sy_junior = {
    "name"  : "scotland yard junior", 
    "nodes" : [10, 20, 1, 11, 21, 12, 22, 32],
    "edges" : [(10, 20),
               (1, 11),
               (12, 22), (22, 32),
               (10, 1), (10, 11), (20, 21), (20, 32),
               (1, 12), (11, 12), (21, 22)]
}


# Graph (star, square, cube, triangle, sy_junior(for Scotland Yard Junior))
graph = star

# Sets nodes and egdes of choosen graph
nodes = graph["nodes"]
edges = graph["edges"]
g=nx.Graph() 
g.add_nodes_from(nodes) # Adds nodes
g.add_edges_from(edges) # Adds edges
