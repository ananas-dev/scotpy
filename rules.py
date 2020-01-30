#File --rules.py--

import config

# Number of turn algorithm:

#(The number of turn is set to the number of nodes of the graph)
def setturns():
    turns = len(config.graph["nodes"])
    return(turns)

