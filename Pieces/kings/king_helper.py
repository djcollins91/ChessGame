from piece import Piece


def king_move(board,from_y,from_x,to_y,to_x, piece_str):
    piece = board.grid[from_y][from_x]
    if piece and str(piece) == piece_str:
        # Ensure it's a valid move when the Xs are equal
        if (board.grid[to_y][to_x] is None):
            #checks to make sure that the piece can only move one spot
            if (to_y == from_y + 1) or (to_y == from_y - 1) or (to_x == from_x + 1) or (to_x == from_x - 1):
                return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
            else:
                return Piece.invalid_move()
        else:#if from_x and from_y are occupied return invalid
            return Piece.invalid_move()
        

def king_take_piece(board,from_y,from_x,to_y,to_x,piece_str,target_str):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]

    if piece and str(piece) == piece_str:
        # Ensure it's a valid move when the Xs are equal
        if (board.grid[to_y][to_x] is not None):
            #checks to make sure that the piece can only move one spot
            if (str(target).startswith(target_str)):
                if ((to_y == from_y + 1) or (to_y == from_y - 1) or (to_x == from_x + 1) or (to_x == from_x - 1)):
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
                else:
                    return Piece.invalid_move()
        else:#if from_x and from_y are occupied return invalid
            return Piece.invalid_move()    

