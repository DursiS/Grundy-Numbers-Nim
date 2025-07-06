import random

# User picks the pile size
def pile_pick():
    pile = int(input("How big is the pile? (10-20) "))
    while pile < 10 or pile > 20:
        print("Error: Pick in between 10-20")
        pile = int(input("How big is the pile? (10-20) "))
    return pile

# Computer picks either 1 or 2 stones. If the remaining stones is 1 or 2, it'll smartly pick 1 or 2 respectively.
def computer_pick(pile):
    num = random.randint(1,2)
    
    if pile == 1:
        return 1
    elif pile == 2:
        return 2
    else:
        if num == 1:
            return 1
        elif num == 2:
            return 2
    
# User picks either 1 or 2 stones.
def user_pick():
    pick = int(input("How many stones? (1-2) "))
    while pick != 1 and pick != 2:
        print("Error: Pick in between 1-2")
        pick = int(input("How many stones? (1-2) "))
    return pick
    