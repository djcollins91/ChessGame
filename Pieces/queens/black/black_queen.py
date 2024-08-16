from Pieces.piece_helpers.helpers import check_to_see_direction_Q_B
from Pieces.queens.queen_helper import queen_move, queen_take_piece
from piece import Piece

class Black_Queen(Piece):
    STARTING_PIECES = 1
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    _piece_str = "BQ"
    _target_str = "W"
    def get_piece_str():
        return Black_Queen._piece_str
    
    def get_target_str():
        return Black_Queen._target_str
    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        return queen_move(board,from_y,from_x,to_y,to_x, Black_Queen._piece_str)
    
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        return queen_take_piece(board,from_y,from_x,to_y,to_x, Black_Queen._piece_str, Black_Queen._target_str, C = 'B')

    