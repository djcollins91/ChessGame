from Pieces.rooks.rooks_helper import direction_to_go
from piece import Piece

class Black_Rook(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #how the piece moves
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'BR':
            # Ensure it's a valid move
            #makes sure theres not a piece in the way
            if (from_x != to_x) and (from_y != to_y):
                return Piece.invalid_move()
            
            change, value_change = direction_to_go(from_y, from_x, to_y, to_x)

            while (from_x != to_x or from_y != to_y):
                change += value_change
                if (from_y == to_y):
                    if (change == to_x) and (board.grid[to_y][to_x] is None):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)           
                    else:
                        return Piece.invalid_move()
                else:
                    if (change == to_y) and (board.grid[to_y][to_x] is None):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
            
                if (board.grid[change][from_x] is not None) :
                    return Piece.invalid_move()
                
                elif (board.grid[from_y][change] is not None):
                    return Piece.invalid_move()
                   
            return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
            
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        if piece and str(piece) == 'BR':
            # Ensure it's a valid move
            #makes sure theres not a piece in the way
            if (from_x != to_x) and (from_y != to_y):
                return Piece.invalid_move()
            change, value_change = direction_to_go(from_y, from_x, to_y, to_x)
            while (from_x != to_x or from_y != to_y):
                change += value_change
                if (from_y == to_y):   
                    #checking if there if your own piece is in the way
                    if (board.grid[from_y][change]) and (str(board.grid[from_y][change]).startswith('B')):
                        return Piece.invalid_move()
                                                     
                    if (board.grid[to_y][change]) and target and (str(target).startswith('W')):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)           
                else:
                    #checking if there if your own piece is in the way
                    if (board.grid[change][from_x]) and (str(board.grid[change][from_x]).startswith('B')):
                        return Piece.invalid_move()
                    
                    if (board.grid[change][to_x]) and target and (str(target).startswith('W')):
                        return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
       
        return Piece.invalid_move()


    