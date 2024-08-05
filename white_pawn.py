from piece import Piece

class White_Pawn(Piece):
    STARTING_PIECES = 8
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'WP':
            # Ensure it's a valid move
            if (from_y == 1 and to_y in [2, 3]) or (from_y != 1 and to_y == from_y + 1):
                if from_x == to_x and board.grid[to_y][to_x] is None:
                    board.grid[to_y][to_x] = piece
                    board.grid[from_y][from_x] = None
                    return "Valid move"
        return "Invalid move"
    
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        if piece and str(piece) == 'WP':
            # Ensure it's a diagonal move and there's a black piece to capture
            if (abs(from_x - to_x) == 1 and to_y - from_y == 1) and target and str(target).startswith('B'):
                board.grid[to_y][to_x] = piece
                board.grid[from_y][from_x] = None
                return "Valid move"
        return "Invalid move"

    