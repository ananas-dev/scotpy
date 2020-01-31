#File --rules.py--

import config

# Number of turn algorithm:

# The number of turn is set to the number of nodes of the graph
def setturns():
    turns = len(config.graph["nodes"])
    return(turns)

# Check if the cops win algorithm:

# It checks if alls the nodes adjacent to the thief are the same
# then the nodes ajacent to the cops or their position

#def checkifwin:

