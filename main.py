# ,______, ,______, ,______, ,_______, ,______, ,_, ,_,
# | ,____| | ,____| | ,__, | |__, ,__| | ,__, | | |_| |
# | |____, | |      | |  | |    | |    | |__| | |_, ,_|
# |____  | | |      | |  | |    | |    | ,____|   | |
# ,____| | | |____, | |__| |    | |    | |        | |
# |______| |______| |______|    |_|    |_|        |_|
# by Lucien Fiorini
# v0.2

# File --main.py--

import config # Located in engine/config.py
import ia # Located in engine/ia.py
import graphs # Located in engine/graph.py
import rules # Located in engine/rules.py

# Main
def main():    
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

# For testing x time main()
def test():
    for x in range(0, 1000000):
        # Sets the number of turns
        turns = rules.setturns()
        # Spawns the cops and the thief
        Tlocation = ia.tspawn()
        Clocation = ia.cspawn(Tlocation) 
        #Main loop
        for x in range(0, turns):
            Tlocation = ia.tmove(Tlocation, Clocation)
            if Clocation == Tlocation: #Checks if cops win
                break
            Clocation = ia.cmove(Clocation, Tlocation) # Cops movement
            if Clocation == Tlocation: #Checks if cops win
                break


if __name__ == "__main__":
    main()
