import Picking
import Pile

# Deciding and printing the starting pile 
pile = Picking.pile_pick()
print(f"\nOkay, there is {pile} stones in the pile:")
Pile.starting_pile(pile)
print("")

# Simulates each round until the pile is empty
turn = True
while pile > 0:
    
    # User's turn
    if turn == True:
        user_remove = Picking.user_pick()
        pile -= user_remove
        turn == False
        
    # Computer's turn
    elif turn == False:
        computer_remove = Picking.computer_pick(pile)
        if pile == 1 or pile == 2:
            print(f"The Computer picked the {computer_remove} remaining.")
        else:
            print(f"The Computer picked {computer_remove}.")
        pile -= computer_remove
    
    Pile.starting_pile(pile)
    print("")
    turn = not turn 

# Computes the winner
if turn == True:
    print("LOSE.")
elif turn == False:
    print("WIN.")
    
    
