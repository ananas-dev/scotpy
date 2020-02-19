# File --ia.py--

import random
from graph import *

## TEST ##

class thief(): 
    class spawn():
        def random():
            tlocation = random.choice(nodes) # Random spawn
            return(tlocation)
    class move():
        # Random move
        def random(tlocation):
            adj = list(g[tlocation].keys()) # Gets the nodes adjacents to the thief
            tlocation = random.choice(adj)
            return(tlocation)
        # Go to the furthest node to the cops
        def furthest(tlocation, clocation):
            ## TEST ##
            #adj = list(g[tlocation].keys()) # Gets the nodes adjacents to the thief
            #clocation = [6, 9]
            #paths = []
            #for x in clocation:
            #    for y in adj:
            #        paths.append(nx.shortest_path(g)[x][y])
            #print(paths)
            ##------##
            adj = list(g[tlocation].keys()) # Gets the nodes adjacents to the thief
            #paths = [[(nx.shortest_path(g)[x][clocation]) for x in adj] for clocation in clocation]
            #tlocation = paths[0]
            # Finds the ajacent node who is the furthest to the policeman
            paths = [(nx.shortest_path(g)[x][clocation]) for x in adj]
            maxlen = max(map(len, paths))
            result = [x for x in paths if len(x) == maxlen]
            path = [x[0] for x in result]
            path_adj = [list(g[x].keys()) for x in path]
            choose = path_adj.index(max(path_adj, key=len))
            tlocation = path[choose]
            return(tlocation)
 
class cops():
    class spawn():
        def random(used):
            try:
                tlocation = int(used)
                while True:
                    clocation = random.choice(nodes)
                    if clocation != tlocation:
                        break
            except:
                while True:
                    rand = random.choice(nodes)
                    if rand not in used:
                        clocation = rand
                        break
            return(clocation)
    class move():
        def nearest(tlocation, clocation):
            # Finds the shortest path to the thief
            adj = list(g[clocation].keys()) # Gets the nodes adjacents to the cops
            # Finds the ajacent node who is the furthest to the thief
            paths = [nx.shortest_path(g)[x][tlocation] for x in adj]
            minlen = min(map(len, paths))
            result = [x for x in paths if len(x) == minlen]
            path = [x[0] for x in result]
            path_adj = [list(g[x].keys()) for x in path]
            choose = path_adj.index(max(path_adj, key=len))
            clocation = path[choose]
            return(clocation)

#def Cstats(Clocation):
#    Cadj_list = list(g[Clocation].keys())
#    Cadj_loc_list = list(g[Clocation].keys())
#    Cadj_loc_list.append(Clocation)
#    return(Cadj_list, Cadj_loc_list)
#
#def Tstats(Tlocation):
#    Tadj_list = list(g[Tlocation].keys())
#    return(Tadj_list)

#def logs(Tlocation, Clocation):
#    logs = pd.Dataframe({'Voleur', 'Policier',
#        'Graphe'})
#    logs = logs.append({'Voleur':Tlocation,'Policier':Clocation,
#        'Graphe':config.graph['name']})
#    logs.to_csv('logs.csv')
