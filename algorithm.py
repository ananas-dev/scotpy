#File --algorithm.py--

from fractions import Fraction
from graph import *

# Number of turn algorithm:
# The number of turn is set to the number of nodes of the graph
def setturns():
    turns = len(nodes)
    return(turns)

# Algorithm to check all spawn possibilities:
# ((number of nodes^entities) - number of nodes to get the number of possiblities)
def spawns():
    all_spawns = []
    for i in nodes:
        tposs = []
        for y in nodes:
            if y != i:
                tposs.append(y) # Gets all the possibilities of spawn in each cops spawns
        for z in tposs:
            all_spawns.append([i, z]) # Returns a list of each spawn possible [cops, thief]
    return(all_spawns)
    
def percent_of_win(cwin, all_spawns):
    all_spawns_num = len(all_spawns)
    cwin_percent = (100/all_spawns_num)*cwin
    return(cwin_percent)

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
