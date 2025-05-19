from piece import Piece


def direction_to_go(from_y, from_x, to_y, to_x):
    if (from_y == to_y):
        change = from_x
        #checks to see if we increment or decrement
        if (change < to_x):
            value_change = 1
        else:
            value_change = -1
    else:
        change = from_y #will be used to see to head toward to_y
        #checks to see if we increment or decrement
        if (change < to_y):
             value_change = 1
        else:
            value_change = -1
    return  change, value_change


def rook_move(board, from_y, from_x, to_y, to_x, piece_str):
    piece = board.grid[from_y][from_x]
    if piece and str(piece) == piece_str:
        # Rook must move in a straight line
        if (from_x != to_x) and (from_y != to_y):
            return False
        # Determine direction and step
        if from_x == to_x:
            step = 1 if to_y > from_y else -1
            for y in range(from_y + step, to_y, step):
                if str(board.grid[y][from_x]) != "Empty Spot":
                    return False
            # Destination must be empty
            if str(board.grid[to_y][to_x]) == "Empty Spot":
                return True
            else:
                return False
        else:
            step = 1 if to_x > from_x else -1
            for x in range(from_x + step, to_x, step):
                if str(board.grid[from_y][x]) != "Empty Spot":
                    return False
            # Destination must be empty
            if str(board.grid[to_y][to_x]) == "Empty Spot":
                return True
            else:
                return False
    return False


def rook_take_piece(board, from_y, from_x, to_y, to_x, piece_str, target_str, C):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    if piece and str(piece) == piece_str:
        # Rook must move in a straight line
        if (from_x != to_x) and (from_y != to_y):
            return False
        # Determine direction and step
        if from_x == to_x:
            step = 1 if to_y > from_y else -1
            for y in range(from_y + step, to_y, step):
                if str(board.grid[y][from_x]) != "Empty Spot":
                    return False
            # Destination must be opponent's piece
            if target and str(target).startswith(target_str):
                return True
            else:
                return False
        else:
            step = 1 if to_x > from_x else -1
            for x in range(from_x + step, to_x, step):
                if str(board.grid[from_y][x]) != "Empty Spot":
                    return False
            # Destination must be opponent's piece
            if target and str(target).startswith(target_str):
                return True
            else:
                return False
    return False


