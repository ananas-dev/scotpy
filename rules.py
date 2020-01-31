#File --rules.py--

import config

# Number of turn algorithm:
# The number of turn is set to the number of nodes of the graph
def setturns():
    turns = len(config.graph["nodes"])
    return(turns)

# Algorithm to check all spawn possibilities:
# (players^number of nodes - number of nodes to get the number of possiblities)
def spawns():
    nodes = config.graph["nodes"]
    all_spawns = []
    for i in nodes:
        Tposs = []
        for y in nodes:
            if y != i:
                Tposs.append(y) # Gets all the possibilities of spawn in each cops spawns
        for z in Tposs:
            all_spawns.append([i, z]) # Returns a list of each spawn possible [cops, thief]
#    all_spawns_num = 2^len(nodes)-len(nodes)
    return(all_spawns)

#def percent_of_win(Cwin):
#    all_spawns_num  = rules.spawn()
#    Cwin_percent = (100/all_spawn_num)*Cwin
#    return(Cwin_percent)

# Check if the cops win algorithm:

# It checks if alls the nodes adjacent to the thief are the same
# then the nodes ajacent to the cops or their position

#def checkifwin():
#    Cadj_loc_list = ia.Cstats()
#    Tadj_list = ia.Tstats()
#    result =  any(elem in Cadj_loc_list for elem in Tadj_list)
#    if result:
#        print('ok')
#    else:
#        print('pas ok')



