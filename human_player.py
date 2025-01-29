from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.pawns.white.white_pawn import White_Pawn
from piece import Piece
from player import Player


class Human_Player(Player):
    def __init__(self, name, board):  # Accept both name and board as arguments
        self.name = name
        self.board = board  # Initialize the board
        self.selected_piece = None
        self.selected_position = None

    def __str__(self):
        return self.name
    
    def turn(self, board, from_x, from_y, to_x, to_y, piece):  # Assuming 'row' and 'col' will be passed when making a move
        if Black_Pawn.move(self.board, from_x, from_y, to_x, to_y) == Piece.invalid_move():
            return True
        else:
            return False
