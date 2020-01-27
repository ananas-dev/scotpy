# File --config.py--

##########
# Graphs #
##########

# Star
star = {
    "name"  : "star", 
    "nodes" : [0, 1, 2, 3, 5, 6, 8, 9],
    "edges" : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (8, 9), (9, 0),
               (1, 3), (3, 5), (5, 7), (7, 9), (9, 1)]
}

# Square
square = {
    "name"  : "square",
    "nodes" : [0, 1, 2, 3],
    "edges" : [(0, 1), (1, 2), (2, 3), (3, 0)]
}

# Cube
cube = {
    "name"  : "cube",
    "nodes" : [0, 4, 6, 2,  # Floor 1
               1, 5, 7, 3], # Floor 2
    "edges" : [(0, 4), (4, 6), (6, 2), (2, 0),  # Floor 1
               (1, 5), (5, 7), (7, 3), (3, 1),  # Floor 2
               (0, 1), (4, 5), (6, 7), (2, 3)]  # Links floor 1 to floor 2 
}

# Graph (star, square, cube)
graph = square

########
# Cops #
########

# Number of Cops
cnum = 1 # Between 1 and 3
