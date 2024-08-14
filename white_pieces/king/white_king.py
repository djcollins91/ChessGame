from piece import Piece

class White_King(Piece):
    STARTING_PIECES = 1
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'WK':
            # Ensure it's a valid move
            if (from_y == 1 and to_y in [2, 3]) or (from_y != 1 and to_y == from_y + 1):
                if from_x == to_x and board.grid[to_y][to_x] is None:
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()
    
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    