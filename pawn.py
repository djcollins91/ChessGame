class Pawn:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    STARTING_PIECES = 8
    taken_pieces = 0
    

    @staticmethod
    def taken_piece():
        Pawn.taken_pieces += 1

    @staticmethod
    def getRemaining_pieces():
        return Pawn.STARTING_PIECES - Pawn.taken_pieces

    def move_wp(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'WP':
            if (from_y == 1 and to_y in [2, 3]) or (from_y != 1 and to_y == from_y + 1):
                if board.grid[to_y][to_x] is None:
                    board.grid[to_y][to_x] = piece
                    board.grid[from_y][from_x] = None
                    return "Valid move"
        return "Invalid move"

    def move_bp(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'BP':
            if (from_y == 6 and to_y in [4,5]) or (from_y != 6 and to_y == from_y - 1):
                if board.grid[to_y][to_x] is None:
                    board.grid[to_y][to_x] = piece
                    board.grid[from_y][from_x] = None
                    return "Valid move"
        return "Invalid move"
    
    def take_piece_wp(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        if piece and str(piece) == 'WP':
            # Ensure it's a diagonal move and there's a black piece to capture
            if (abs(from_x - to_x) == 1 and to_y - from_y == 1) and target and str(target).startswith('B'):
                board.grid[to_y][to_x] = piece
                board.grid[from_y][from_x] = None
                return "Valid move"
        return "Invalid move"
