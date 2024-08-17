from piece import Piece




def knight_move(board,from_y,from_x,to_y,to_x, piece_check):
    piece = board.grid[from_y][from_x]
    if (piece and str(piece) == piece_check) and (board.grid[to_y][to_y] is None):
        # Ensure it's a valid move
        
        if ((to_y - from_y) == 2) and ((to_x - from_x) == 1):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y) 
        #when the x-axis goes left
        elif ((to_y - from_y) == 2) and ((to_x - from_x) == -1):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when the y-axis goes doBN and the x goes right
        elif ((to_y - from_y) == -2) and ((to_x - from_x) == 1):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        
        #when the y-axis goes doBN and the x goes left
        elif ((to_y - from_y) == -2) and ((to_x - from_x) == -1):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when the x-axis goes right 2 and the y goes up 1
        elif ((to_y - from_y) == 1) and ((to_x - from_x) == 2):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when the x-axis goes right 2 and the y goes doBN 1
        elif ((to_y - from_y) == - 1) and ((to_x - from_x) == 2):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when the x-axis goes left 2 and the y goes up 1
        elif ((to_y - from_y) ==  1) and ((to_x - from_x) == -2):
           return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when the x-axis goes left 2 and the y goes doBN 1
        elif ((to_y - from_y) == - 1) and ((to_x - from_x) == -2):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)

    return Piece.invalid_move()