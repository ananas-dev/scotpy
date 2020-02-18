# ,______, ,______, ,______, ,_______, ,______, ,_, ,_,
# | ,____| | ,____| | ,__, | |__, ,__| | ,__, | | |_| |
# | |____, | |      | |  | |    | |    | |__| | |_, ,_|
# |____  | | |      | |  | |    | |    | ,____|   | |
# ,____| | | |____, | |__| |    | |    | |        | |
# |______| |______| |______|    |_|    |_|        |_|
# by Lucien Fiorini
# v0.5

# File --main.py--

from ia import * # Located in engine/ia.py
from graph import * # Located in engine/graph.py
import algorithm # Located in engine/rules.py

## MULTIPLE COPS TEST ##
def test():
    used = []
    tlocation = thief.spawn.random()
    used.append(tlocation)
    c1 = cops.spawn.random(used)
    used.append(c1)
    c2 = cops.spawn.random(used)
    used.append(c2)
    turns = algorithm.setturns()
    for x in range(0, turns):
        tlocation = thief.move.furthest(tlocation, [c1, c2])
        print("\nthief location:", tlocation)
        if tlocation in [c1, c2]: # Check if cops win
            print("\nthe cops win !\n")
            break
        c1 = cops.move.nearest(tlocation, c1)
        c2 = cops.move.nearest(tlocation, c2)
        print("cops location 1:", c1)
        print("cops location 2:", c2)
        if tlocation in [c1, c2]: # Check if cops win
            print("\nthe cops win !\n")
            break
    if tlocation not in [c1, c2]:
        print("\nthe thief wins !\n")


## VISUAL TEST ##
def visual_test():
    # Main title
    print("\n--SCOTPY--")
    # Print graph's info
    print("\ngraph :", graph["name"])
    print("nodes :", graph["nodes"])
    print("edges :", graph["edges"])
    # Set the number of turns
    turns = algorithm.setturns()
    print("\nnumber of turns:", turns)
    # Spawn the cops and the thief
    tlocation = thief.spawn.random()
    clocation = cops.spawn.random(tlocation)
    print("\nthief spawn:", tlocation)
    print("cops spawn:", clocation)
    # Main loop
    for x in range(0, turns):
        tlocation = thief.move.furthest(tlocation, clocation)
        print("\nthief location:", tlocation)
        if clocation == tlocation: # Check if cops win
            print("\nthe cops win !\n")
            break
        clocation = cops.move.nearest(tlocation, clocation)
        print("cops location:", clocation)
        if clocation == tlocation: # Check if cops win
            print("\nthe cops win !\n")
            break
    if clocation != tlocation:
        print("\nthe thief wins !\n")


## TEST OF ALL POSSIBILITIES ##
def all_poss_test():    
    turns = algorithm.setturns()
    all_spawns = algorithm.spawns()
    twin = 0
    cwin = 0
    for spawns in all_spawns:
    # Spawns the cops and the thief
        tlocation = spawns[1]
        clocation = spawns[0]
        #Main loop
        for x in range(0, turns):
            tlocation = thief.move.furthest(tlocation, clocation)
            if clocation == tlocation: #Checks if cops win
                cwin = cwin + 1
                break
            clocation = cops.move.nearest(tlocation, clocation)
            if clocation == tlocation: #Checks if cops win
                cwin = cwin+1
                break
        if clocation != tlocation:
            twin = twin+1
    cwin_percent = algorithm.percent_of_win(cwin, all_spawns)
    print("\nCops win:", cwin)
    print("Thief win:", twin, "\n")
    print("Cops have",cwin_percent,"% chances of win in",graph["name"],"\n")

## MAIN ##
if __name__ == "__main__":
    visual_test() # Choose one of the mains fonctions
