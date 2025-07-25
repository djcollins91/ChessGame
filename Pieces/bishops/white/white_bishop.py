from pieces.bishops.bishop_helper import bishop_move, bishop_take_piece
from piece import Piece

class White_Bishop(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0
    _piece_str = "WB"
    _target_str = "B"
    _starting_row = 0
    _starting_col_1 = 2
    _starting_col_2 = 5
    

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    @staticmethod
    def get_starting_row():
        return White_Bishop._starting_row
    @staticmethod
    def get_starting_col_1():
        return White_Bishop._starting_col_1
    @staticmethod
    def get_starting_col_2():
        return White_Bishop._starting_col_2
    @staticmethod
    def get_piece_str():
        return White_Bishop._piece_str
    
    def get_target_str():
        return White_Bishop._target_str
    #how the piece move located in bsishop_helper
    def move(self, board, from_x, from_y, to_x, to_y):
        # Try normal move first
        move_result = bishop_move(board, from_y, from_x, to_y, to_x, White_Bishop._piece_str)
        if move_result:
            return move_result
        # If not a normal move, try to take a piece
        return bishop_take_piece(board, from_y, from_x, to_y, to_x, White_Bishop._piece_str, White_Bishop._target_str)
    
    #how the piece can take a piece located in bsishop_helper
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        return bishop_take_piece(board,from_y,from_x,to_y,to_x, White_Bishop._piece_str, White_Bishop._target_str)