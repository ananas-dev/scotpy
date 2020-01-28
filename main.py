# ,______, ,______, ,______, ,_______, ,______, ,_, ,_,
# | ,____| | ,____| | ,__, | |__, ,__| | ,__, | | |_| |
# | |____, | |      | |  | |    | |    | |__| | |_, ,_|
# |____  | | |      | |  | |    | |    | ,____|   | |
# ,____| | | |____, | |__| |    | |    | |        | |
# |______| |______| |______|    |_|    |_|        |_|
# by Lucien Fiorini
# v0.2

# File --main.py--

import config # Located in dir/config.py
import ia # Located in dir/ia.py

# Main
def main():    
    print("--SCOTPY--")
    # Prints graph's info
    print("\ngraph :", config.graph["name"])
    print("nodes :", config.graph["nodes"])
    print("edges :", config.graph["edges"])
    # Spawns the cops and the thief
    tlocation = ia.tspawn()
    print("\nthief spawn:", tlocation)
    clocation = ia.cspawn(tlocation) 
    print("cops spawn:", clocation)
    #Main loop
    for x in range(0, 30):
        tlocation = ia.tmove(tlocation, clocation)
        print("\nthief location:", tlocation)
        if clocation == tlocation: #Checks if cops win
            print("\nthe cops win !")
            break
        clocation = ia.cmove(clocation, tlocation) # Cops movement
        print("cops location:", clocation)
        if clocation == tlocation: #Checks if cops win
            print("\nthe cops win !")
            break
    if clocation != tlocation:
        print("\nthe thief win !")
if __name__ == "__main__":
    main()
