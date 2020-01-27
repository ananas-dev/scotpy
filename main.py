# ,______, ,______, ,______, ,_______, ,______, ,-, ,_,
# | ,____| | ,____| | ,__, | |__, ,__| | ,__, | | |_| |
# | |____, | |      | |  | |    | |    | |__| | |_, ,_|
# |____  | | |      | |  | |    | |    | ,____|   | |
# ,____| | | |____, | |__| |    | |    | |        | | 
# |______| |______| |______|    |_|    |_|        |_|
# by Lucien Fiorini & Alexander Letourneur
# v0.1

# File --main.py--

import config # Located in dir/config.py
import ia # Located in dir/ia.py

# Main
def main():    
    tlocation = ia.tspawn()
    clocation = ia.cspawn(tlocation)
    while True:
        clocation = ia.cmove(clocation, tlocation)
        print("thief location:", tlocation)
        print("cops location:", clocation)
        if clocation == tlocation:
            print("cops win")
            break

main()


# Tests

print(config.cnum)

