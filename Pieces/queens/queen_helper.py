from pieces.empty.empty import Empty_Spot
from piece import Piece
from pieces.piece_helpers.helpers import check_to_see_direction_Q_B


def queen_move(board, from_y, from_x, to_y, to_x, piece_str):
    piece = board.grid[from_y][from_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    # GUI-compatible: check for 'Empty Spot' at destination
    if piece and str(piece) == piece_str and str(board.grid[to_y][to_x]) == Empty_Spot.get_str():
        # Check path is clear
        y, x = change_y, change_x
        while (y != to_y) or (x != to_x):
            y += value_change_y
            x += value_change_x
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]) != Empty_Spot.get_str():
                return Piece.invalid_move()
        return Piece.valid_move()
    return Piece.invalid_move()


def queen_take_piece(board, from_y, from_x, to_y, to_x, piece_str, target_str, C):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    # GUI-compatible: check for opponent's piece at destination
    if piece and str(piece) == piece_str and target and str(target).startswith(target_str):
        # Check path is clear (no own pieces in the way)
        y, x = change_y, change_x
        LOOP_SIZE = len(board.grid)
        while (y != to_y) or (x != to_x):
            y += value_change_y
            x += value_change_x
            # Bounds check
            if not (0 <= y < LOOP_SIZE and 0 <= x < LOOP_SIZE):
                return Piece.invalid_move()
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]) != Empty_Spot.get_str():
                return Piece.invalid_move()
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]).startswith(C):
                return Piece.invalid_move()
        return Piece.valid_move()
    return Piece.invalid_move()