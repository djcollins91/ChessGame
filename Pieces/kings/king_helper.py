from piece import Piece

def king_move(board, from_y, from_x, to_y, to_x, piece_str):
    piece = board.grid[from_y][from_x]
    # GUI-compatible: check for 'Empty Spot' at destination
    if piece and str(piece) == piece_str and str(board.grid[to_y][to_x]) == "Empty Spot":
        if abs(to_y - from_y) <= 1 and abs(to_x - from_x) <= 1 and (to_y != from_y or to_x != from_x):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
    return Piece.invalid_move()


def king_take_piece(board, from_y, from_x, to_y, to_x, piece_str, target_str):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    # GUI-compatible: check for opponent's piece at destination
    if piece and str(piece) == piece_str and target and str(target).startswith(target_str):
        if abs(to_y - from_y) <= 1 and abs(to_x - from_x) <= 1 and (to_y != from_y or to_x != from_x):
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
    return Piece.invalid_move()

