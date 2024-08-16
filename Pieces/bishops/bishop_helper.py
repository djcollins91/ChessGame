from Pieces.piece_helpers.helpers import check_to_see_direction_Q_B
from piece import Piece


def bishop_move(board,from_y,from_x,to_y,to_x, piece_str):
    piece = board.grid[from_y][from_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    
    if piece and str(piece) == piece_str:
        # Ensure it's a valid move
        if (from_y != to_y) and (from_x != to_x) and (board.grid[to_y][to_x] is None):
            while (change_y != to_y) or (change_x != to_x):
                change_y += value_change_y
                change_x += value_change_x
                if (board.grid[change_y][change_x]) is not None:
                    return Piece.invalid_move()
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()
    
def bishop_take_piece(board,from_y,from_x,to_y,to_x, piece_str, target_str):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    
    if piece and str(piece) == piece_str:
        # Ensure it's a valid move
        if (from_y != to_y) and (from_x != to_x) and (target is not None) and (str(target).startswith(target_str)):
            while (change_y != to_y) or (change_x != to_x):
                change_y += value_change_y
                change_x += value_change_x
                if ((board.grid[change_y][change_x]) is not None):
                    #ensures we can't run into our own piece
                    if (str(board.grid[change_y][change_x]).startswith(target_str)):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
                    else:
                        return Piece.invalid_move()   
        return Piece.invalid_move()

