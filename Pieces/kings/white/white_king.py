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
            # Ensure it's a valid move when the Xs are equal
            if (board.grid[to_y][to_x] is None):
                #checks to make sure that the piece can only move one spot
                if (to_y == from_y + 1) or (to_y == from_y - 1) or (to_x == from_x + 1) or (to_x == from_x - 1):
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
                else:
                    return Piece.invalid_move()
            else:#if from_x and from_y are occupied return invalid
                return Piece.invalid_move()    
        
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]

        if piece and str(piece) == 'WK':
            # Ensure it's a valid move when the Xs are equal
            if (board.grid[to_y][to_x] is not None):
                #checks to make sure that the piece can only move one spot
                if (str(target).startswith('B')):
                    if ((to_y == from_y + 1) or (to_y == from_y - 1) or (to_x == from_x + 1) or (to_x == from_x - 1)):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
                    else:
                        return Piece.invalid_move()
            else:#if from_x and from_y are occupied return invalid
                return Piece.invalid_move()    
        
        
    