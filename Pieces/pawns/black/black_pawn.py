from Pieces.empty.empty import Empty_Spot
from piece import Piece

class Black_Pawn(Piece):
    STARTING_PIECES = 8
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    _piece_str = "BP"
    _target_str = "W"
    def get_piece_str():
        return Black_Pawn._piece_str
    
    def get_target_str():
        return Black_Pawn._target_str
    #overidden function for moving the Black_Pawn
    def move(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == Black_Pawn._piece_str:
            # Ensure it's a valid move
            if (from_y == 6 and to_y in [4, 5]) or (from_y != 6 and to_y == from_y - 1):
                if (from_x == to_x) and (str(board.grid[to_y][to_x]) == Empty_Spot.get_piece_str()) :
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()
    
    def take_piece(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        # Ensure the piece is a black White_Pawn
        if piece and str(piece) == Black_Pawn._piece_str:
            # Check if the move is a valid diagonal move
            if (abs(from_x - to_x) == 1 and from_y - to_y == 1):
                # Ensure there is a white piece to capture
                if target and str(target).startswith(Black_Pawn._target_str):
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)           
        return Piece.invalid_move()
