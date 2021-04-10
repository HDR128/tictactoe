from random import choice

def com_move(available_pos, X_pos_set, O_pos_set):
    """
    Calculates the next best move based on the following concepts:

    # 1. If self is one move away from winning, always make winning move
    # 2. If opponent is one move away from winning, always block opponent
    # 3. If neither, make the next best move

    :param available_pos: List of available positions
    :param X_pos_set: Set of moves X has already made
    :param O_pos_set: Set of moves O has already made (in this case, the computer)
    :return: Integer representing position of move

    """

    # Store winning sets
    winning_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    available_set = set(available_pos)

    # 1. Make a winning move if the opportunity exists
    for sets in winning_sets:
        inter_set_O = O_pos_set.intersection(sets)
        if len(inter_set_O) == 2:
            move = sets.difference(inter_set_O).pop()
            if move in available_pos:
                return move

    # 2. Block opponent from winning
    for sets in winning_sets:
        inter_set_X = X_pos_set.intersection(sets)
        if len(inter_set_X) == 2:
            move = sets.difference(inter_set_X).pop()
            if move in available_pos:
                return move


    # 3. Make the next best move
    if 5 in available_pos:
        return 5
    elif 5 in X_pos_set:
        for i in [1, 3, 7, 9]:
            if i in available_pos:
                return i
            else:
                for sets in winning_sets:
                    inter_set = O_pos_set.intersection(sets)
                    if len(inter_set) == 1:
                        move = sets.difference(inter_set).pop()
                        if move in available_pos:
                            return move

    return choice(available_pos)




