# File --config.py--

##########
# Graphs #
##########

# The names of the nodes of the graphs follows this logic:
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

# Cube
cube = {
    "name"  : "cube",
    "nodes" : [0, 100, 110, 10,  # Floor 1
               1, 101, 111, 11], # Floor 2
    "edges" : [(0, 100), (100, 110), (110, 10), (10, 0),  # Floor 1
               (1, 101), (101, 111), (111, 11), (11, 1),  # Floor 2
               (0, 1), (100, 101), (110, 111), (10, 11)]  # Links floor 1 to floor 2 
}

# Graph (star, square, cube, triangle)
graph = square 

########
# Cops #
########

# Number of Cops
cnum = 1 # Between 1 and 3
