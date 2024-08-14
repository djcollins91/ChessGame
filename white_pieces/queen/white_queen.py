from piece import Piece

class White_Queen(Piece):
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
        #if we don't move on the x cordinate
        value_change_x = 0
        change_y = from_y
        #if we don't move on the y cordinate
        value_change_y = 0

        #when we do move on the spefic coordinates
        if (change_x < to_x):
            value_change_x = 1

        if (change_x > to_x):
            value_change_x = -1

        if change_y < to_y:  
            value_change_y = 1

        if (change_y > to_y):
            value_change_y = -1

        if piece and str(piece) == 'WQ':
            if (board.grid[to_y][to_x] is None):
                #checks to make sure there isn't a piece in the way
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

    