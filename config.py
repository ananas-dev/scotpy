# File --config.py--

# Star
star = {
    "nodes" : [0, 1, 2, 3, 5, 6, 8, 9],
    "edges" : [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (8, 9), (9, 0),
        (1, 3), (3, 5), (5, 7), (7, 9), (9, 1)]
}

# Square
square = {
    "nodes" : [0, 1, 2, 3],
    "edges" : [(0, 1), (1, 2), (2, 3), (3, 0)]
}

# Graph (star, square)
graph = star

# Number of Cops
cnum = 1 # Between 1 and 3
