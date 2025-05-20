from pieces.empty.empty import Empty_Spot
from pieces.piece_helpers.helpers import check_to_see_direction_Q_B
from piece import Piece


def bishop_move(board,from_y,from_x,to_y,to_x, piece_str):
    piece = board.grid[from_y][from_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    if piece and str(piece) == piece_str:
        # Ensure it's a valid move
        if (from_y != to_y) and (from_x != to_x) and str(board.grid[to_y][to_x]) == Empty_Spot.get_str():
            temp_y, temp_x = change_y, change_x
            while (temp_y != to_y) or (temp_x != to_x):
                temp_y += value_change_y
                temp_x += value_change_x
                if (temp_y == to_y and temp_x == to_x):
                    break
                if str(board.grid[temp_y][temp_x]) != Empty_Spot.get_str():
                    return Piece.invalid_move()
            return Piece.valid_move()
        return Piece.invalid_move()
    
def bishop_take_piece(board,from_y,from_x,to_y,to_x, piece_str, target_str):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    if piece and str(piece) == piece_str:
        # Ensure it's a valid diagonal move and the target is an opponent's piece
        if (from_y != to_y) and (from_x != to_x) and str(target).startswith(target_str):
            temp_y, temp_x = change_y, change_x
            while (temp_y != to_y) or (temp_x != to_x):
                temp_y += value_change_y
                temp_x += value_change_x
                if (temp_y == to_y and temp_x == to_x):
                    break
                # If any piece (not an Empty Spot) is in the way, invalid
                if str(board.grid[temp_y][temp_x]) != Empty_Spot.get_str():
                    return Piece.invalid_move()
            return Piece.valid_move()
    return Piece.invalid_move()

