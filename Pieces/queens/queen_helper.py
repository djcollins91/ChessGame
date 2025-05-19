from Pieces.piece_helpers.helpers import check_to_see_direction_Q_B
from piece import Piece


def queen_move(board, from_y, from_x, to_y, to_x, piece_str):
    piece = board.grid[from_y][from_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    # GUI-compatible: check for 'Empty Spot' at destination
    if piece and str(piece) == piece_str and str(board.grid[to_y][to_x]) == "Empty Spot":
        # Check path is clear
        y, x = change_y, change_x
        while (y != to_y) or (x != to_x):
            y += value_change_y
            x += value_change_x
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]) != "Empty Spot":
                return Piece.invalid_move()
        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
    return Piece.invalid_move()


def queen_take_piece(board, from_y, from_x, to_y, to_x, piece_str, target_str, C):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    change_y, change_x, value_change_y, value_change_x = check_to_see_direction_Q_B(from_x, from_y, to_x, to_y)
    # GUI-compatible: check for opponent's piece at destination
    if piece and str(piece) == piece_str and target and str(target).startswith(target_str):
        # Check path is clear (no own pieces in the way)
        y, x = change_y, change_x
        while (y != to_y) or (x != to_x):
            y += value_change_y
            x += value_change_x
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]) != "Empty Spot":
                return Piece.invalid_move()
            if (y, x) != (to_y, to_x) and str(board.grid[y][x]).startswith(C):
                return Piece.invalid_move()
        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
    return Piece.invalid_move()