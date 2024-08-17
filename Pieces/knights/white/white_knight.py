from Pieces.knights.knight_helper import knight_move
from piece import Piece

class White_Knight(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    _piece_str = "WN"
    _target_str = "B"
    def get_piece_str():
        return White_Knight._piece_str
    
    def get_target_str():
        return White_Knight._target_str
    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        return knight_move(board,from_y,from_x,to_y,to_x, piece_check = 'WN')
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    