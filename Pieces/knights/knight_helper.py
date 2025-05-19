from piece import Piece

def knight_move(board, from_y, from_x, to_y, to_x, piece_str):
    piece = board.grid[from_y][from_x]
    # GUI-compatible: check for 'Empty Spot' at destination
    if piece and str(piece) == piece_str and str(board.grid[to_y][to_x]) == "Empty Spot":
        dy = to_y - from_y
        dx = to_x - from_x
        if (abs(dy), abs(dx)) in [(2, 1), (1, 2)]:
            return True
    return False


def knight_take_piece(board, from_y, from_x, piece_str, to_y, to_x, target_str):
    piece = board.grid[from_y][from_x]
    target = board.grid[to_y][to_x]
    # GUI-compatible: check for opponent's piece at destination
    if piece and str(piece) == piece_str and target and str(target).startswith(target_str):
        dy = to_y - from_y
        dx = to_x - from_x
        if (abs(dy), abs(dx)) in [(2, 1), (1, 2)]:
            return True
    return False
