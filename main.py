# ,______, ,______, ,______, ,_______, ,______, ,_, ,_,
# | ,____| | ,____| | ,__, | |__, ,__| | ,__, | | |_| |
# | |____, | |      | |  | |    | |    | |__| | |_, ,_|
# |____  | | |      | |  | |    | |    | ,____|   | |
# ,____| | | |____, | |__| |    | |    | |        | |
# |______| |______| |______|    |_|    |_|        |_|
# by Lucien Fiorini
# v0.5

# File --main.py--

import config # Located in engine/config.py
import ia # Located in engine/ia.py
import graphs # Located in engine/graph.py
import rules # Located in engine/rules.py

# Main
def all_poss_test():    
    turns = rules.setturns()
    all_spawns = rules.spawns()
    Twin = 0
    Cwin = 0
    for spawns in all_spawns:
    # Spawns the cops and the thief
        Tlocation = spawns[1]
        Clocation = spawns[0]
        #Main loop
        for x in range(0, turns):
            Tlocation = ia.Tmove(Tlocation, Clocation)
            if Clocation == Tlocation: #Checks if cops win
                Cwin = Cwin + 1
                break
            Clocation = ia.Cmove(Clocation, Tlocation) # Cops movement
            if Clocation == Tlocation: #Checks if cops win
                Cwin = Cwin+1
                break
            ia.Cstats(Clocation)
        if Clocation != Tlocation:
            Twin = Twin+1
#    Cwin_percent = rules.percent_of_win()
    print("\nCops win:", Cwin)
    print("Thief win:", Twin, "\n")
#    print(Cwin_percent)


def visual_test():    
    print("\n--SCOTPY--")
    # Prints graph's info
    print("\ngraph :", config.graph["name"])
    print("nodes :", config.graph["nodes"])
    print("edges :", config.graph["edges"])
    # Sets the number of turns
    turns = rules.setturns()
    print("\nnumber of turns:", turns)
    # Spawns the cops and the thief
    Tlocation = ia.Tspawn()
    print("\nthief spawn:", Tlocation)
    Clocation = ia.Cspawn(Tlocation) 
    print("cops spawn:", Clocation)
    #Main loop
    for x in range(0, turns):
        Tlocation = ia.Tmove(Tlocation, Clocation)
        print("\nthief location:", Tlocation)
        if Clocation == Tlocation: #Checks if cops win
            print("\nthe cops win !\n")
            break
        Clocation = ia.Cmove(Clocation, Tlocation) # Cops movement
        print("cops location:", Clocation)
        if Clocation == Tlocation: #Checks if cops win
            print("\nthe cops win !\n")
            break
        ia.Cstats(Clocation)
    if Clocation != Tlocation:
        print("\nthe thief wins !\n")

if __name__ == "__main__":
    all_poss_test()
