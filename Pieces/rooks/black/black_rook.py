from Pieces.rooks.rooks_helper import direction_to_go, rook_move, rook_take_piece
from piece import Piece

class Black_Rook(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0
    _piece_str = "BR"
    _target_str = "W"
    _starting_row = 7
    _starting_col_1 = 0
    _starting_col_2 = 7

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_piece_str():
        return Black_Rook._piece_str
    @staticmethod
    def get_starting_row():
        return Black_Rook._starting_row
    @staticmethod
    def get_starting_col_1():
        return Black_Rook._starting_col_1
    @staticmethod
    def get_starting_col_2():
        return Black_Rook._starting_col_2
    def get_target_str():
        return Black_Rook._target_str
    #how the piece moves
    def move(self, board, from_x, from_y, to_x, to_y):
        # Try normal move first (to empty spot)
        if rook_move(board, from_y, from_x, to_y, to_x, Black_Rook._piece_str):
            return True
        # If not valid, try to capture
        return rook_take_piece(board, from_y, from_x, to_y, to_x, Black_Rook._piece_str, Black_Rook._target_str, C='B')

    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        return rook_take_piece(board, from_y, from_x, to_y, to_x, Black_Rook._piece_str, Black_Rook._target_str, C='B')