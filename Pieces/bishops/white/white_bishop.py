from Pieces.bishops.bishop_helper import check_to_see_direction
from piece import Piece

class White_Bishop(Piece):
    STARTING_PIECES = 1
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        change_x = from_x
        change_y = from_y
        
        value_change_y, value_change_x = check_to_see_direction(change_x, change_y,to_x, to_y)
        
        if piece and str(piece) == 'WB':
            # Ensure it's a valid move
            if (from_y != to_y) and (from_x != to_x) and (board.grid[to_y][to_x] is None):
                while (change_y != to_y) or (change_x != to_x):
                    change_y += value_change_y
                    change_x += value_change_x
                    if (board.grid[change_y][change_x]) is not None:
                       return Piece.invalid_move()
                return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
            return Piece.invalid_move()
       
    
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    