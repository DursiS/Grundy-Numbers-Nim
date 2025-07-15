def find_best_move(pile):
    for move in [1, 2]:
        if pile >= move:
            new_grundy = (pile - move) % 3
            if new_grundy == 0:  # Opponent gets worse position
                return move
    return None
 