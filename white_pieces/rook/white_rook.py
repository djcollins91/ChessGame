from piece import Piece

class White_Rook(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #how the piece moves
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'WR':
            # Ensure it's a valid move
            if (from_x == to_x or from_y == to_y) and board.grid[to_y][to_x] is None:
                board.grid[to_y][to_x] = piece
                board.grid[from_y][from_x] = None
                return "Valid move"
        return "Invalid move"
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    