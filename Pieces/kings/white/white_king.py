from pieces.kings.king_helper import king_move, king_take_piece
from piece import Piece

class White_King(Piece):
    STARTING_PIECES = 1
    taken_pieces = 0
    _piece_str = "WK"
    _target_str = "B"
    _starting_row = 0
    _starting_col = 4
   

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_starting_row():
        return White_King._starting_row
    @staticmethod
    def get_starting_col():
        return White_King._starting_col
    @staticmethod
    def get_piece_str():
        return White_King._piece_str
    
    def get_target_str():
        return White_King._target_str
    #how the piece move
    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        # Try normal move first (to empty spot)
        if king_move(board, from_y, from_x, to_y, to_x, White_King._piece_str):
            return Piece.valid_move()
        # If not valid, try to capture
        return king_take_piece(board, from_y, from_x, to_y, to_x, White_King._piece_str, White_King._target_str)

    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        return king_take_piece(board, from_y, from_x, to_y, to_x, White_King._piece_str, White_King._target_str)