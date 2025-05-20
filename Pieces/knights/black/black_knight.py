from pieces.knights.knight_helper import knight_move, knight_take_piece
from piece import Piece


class Black_Knight(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0
    _piece_str = "BN"
    _target_str = "W"
    _starting_row = 7
    _starting_col_1 = 1
    _starting_col_2 = 6

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def get_starting_row():
        return Black_Knight._starting_row

    @staticmethod
    def get_starting_col_1():
        return Black_Knight._starting_col_1

    @staticmethod
    def get_starting_col_2():
        return Black_Knight._starting_col_2

    @staticmethod
    def get_piece_str():
        return Black_Knight._piece_str

    def get_target_str():
        return Black_Knight._target_str

    # how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        # Try normal move first (to empty spot)
        if knight_move(board, from_y, from_x, to_y, to_x, Black_Knight._piece_str):
            return Piece.valid_move()
        # If not valid, try to capture
        return knight_take_piece(board, from_y, from_x, Black_Knight._piece_str, to_y, to_x, Black_Knight._target_str)

    # how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        return knight_take_piece(board, from_y, from_x, Black_Knight._piece_str, to_y, to_x, Black_Knight._target_str)

