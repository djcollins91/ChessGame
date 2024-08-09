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
            #makes sure theres not a piece in the way
            if (from_x != to_x) and (from_y != to_y):
                return "Invalid move"
            if (from_y == to_y):
                x_or_y = from_x != to_x
                change = from_x
                #checks to see if we increment or decrement
                if (change < to_x):
                    value_change = 1
                else:
                    value_change = -1
            else:
                x_or_y = from_y != to_y
                change = from_y #will be used to see to head toward to_y
                #checks to see if we increment or decrement
                if (change < to_y):
                    value_change = 1
                else:
                    value_change = -1
            while (from_x != to_x or from_y != to_y):
                change += value_change
                if (from_y == to_y):
                    if (change == to_x) and (board.grid[to_y][to_x] is None):
                        board.grid[to_y][to_x] = piece
                        board.grid[from_y][from_x] = None
                        return "Valid move"
                        
                    else:
                        return "Invalid move"
                else:
                    if (change == to_y) and (board.grid[to_y][to_x] is None):
                        board.grid[to_y][to_x] = piece
                        board.grid[from_y][from_x] = None
                        return "Valid move"
                    
                    
                if (board.grid[change][from_x] is not None) :

                    return "Invalid move"
                
                elif (board.grid[from_y][change] is not None):
                    return "Invalid move"
                

            board.grid[to_y][to_x] = piece
            board.grid[from_y][from_x] = None
            return "Valid move"   
            
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    