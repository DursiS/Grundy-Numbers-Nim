import Picking

full_pile = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]

# Returns the amount of stones depending on the size of the pile
def starting_pile(pile):
    starting_pile = []
    for stones in full_pile[0:pile]:
        starting_pile.append(stones)
    return print((' ').join(starting_pile))


