# ,______, ,______, ,______, ,_______, ,_,      ,______, ,_,  ,_, ,_____,
# | ,____| | ,____| | ,__, | |__, ,__| | |      | ,__, | |  \ | | | ,___ \
# | |____, | |      | |  | |    | |    | |      | |__| | |   \| | | |   \ |
# |____  | | |      | |  | |    | |    | |      | ,__, | | |\ \ | | |   | |
# ,____| | | |____, | |__| |    | |    | |____, | |  | | | | \  | | |___/ |
# |______| |______| |______|    |_|    |______| |_|  |_| |_|  \_| |______/
# by Lucien Fiorini & Alexander Letourneur
# v0.1

# File --main.py--

import networkx as nx
import random
import config

# ABCD square
g=nx.Graph()
g.add_nodes_from(config.nodes)
g.add_edges_from(config.edges)

def thief_spawn():
    thief_location = random.choice(config.nodes)
    print("thief spawn:",thief_location)
    return thief_location

def cops_spawn(thief_location):
    while True:
        cops_location = random.choice(config.nodes)
        if cops_location != thief_location:
            break
    print("cops spawn:",cops_location)
    return cops_location

def thief_move(thief_location, cops_location):    
    thief_adjacent = g[cops_location].keys()
    thief_possible_paths = []
    thief_possible_paths_gen = nx.all_pairs_dijkstra_path(g)
   #thief_possible_paths = thief_possible_paths_gen[cops_location](thief_possible_paths()) 
    map(thief_possibles_paths
    print(thief_adjacent)
    print(thief_possible_paths)

def cops_move(cops_location):
    cops_path_gen = nx.all_pairs_dijkstra_path(g)
    cops_path = cops_path_gen[cops_location][thief_location]
    cops_location = cops_path[1] 
    return cops_location

# Main
thief_location = thief_spawn()
cops_location = cops_spawn(thief_location)
while True:
    cops_location = cops_move(cops_location)
    print("thief location:", thief_location)
    print("cops location:", cops_location)
    if cops_location == thief_location:
        print("cops win")
        break
