from Pieces.knights.knight_helper import  knight_move
from piece import Piece

class Black_Knight(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    _piece_str = "BN"
    _target_str = "W"
    def get_piece_str():
        return Black_Knight._piece_str
    
    def get_target_str():
        return Black_Knight._target_str
    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        return knight_move(board,from_y,from_x,to_y,to_x, piece_check = 'BN')
    
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    