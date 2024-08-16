from Pieces.knights.knight_helper import exploration
from piece import Piece

class White_Knight(Piece):
    STARTING_PIECES = 2
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #how the piece move
    def move(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if (piece and str(piece) == 'WN') and (board.grid[to_y][to_y] is None):
            # Ensure it's a valid move
            #when the piece moves on the y-axis 2
            if (abs(to_y - from_y) == 2) and (abs(to_x - from_x) == 1):
                if ((to_y - from_y) == 2) and ((to_x - from_x) == 1):
                    #checking the first move possible move
                    first_option1 = board.grid[from_y + 1][from_x]
                    second_option1 = board.grid[from_y + 2][from_x]
                    first_option2 = board.grid[from_y][from_x +1]
                    second_option2 = board.grid[from_y+1][from_x + 1]
                    return exploration(first_option1,first_option2,second_option1,second_option2,piece,board,from_x,from_y,to_x,to_y)
                #when the x-axis goes left
                elif ((to_y - from_y) == 2) and ((to_x - from_x) == -1):
                    #checking the first move possible move
                    first_option1 = board.grid[from_y + 1][from_x]
                    second_option1 = board.grid[from_y + 2][from_x]
                    first_option2 = board.grid[from_y][from_x -1]
                    second_option2 = board.grid[from_y+1][from_x - 1]
                    #exploring all the possible options
                    return exploration(first_option1,first_option2,second_option1,second_option2,piece,board,from_x,from_y,to_x,to_y)
                #when the y-axis goes down and the x goes right
                elif ((to_y - from_y) == -2) and ((to_x - from_x) == 1):
                    #checking the first move possible move
                    first_option1 = board.grid[from_y - 1][from_x]
                    second_option1 = board.grid[from_y - 2][from_x]
                    first_option2 = board.grid[from_y][from_x +1]
                    second_option2 = board.grid[from_y-1][from_x + 1]
                    #exploring all the possible options
                    return exploration(first_option1,first_option2,second_option1,second_option2,piece,board,from_x,from_y,to_x,to_y)


        return Piece.invalid_move()
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        pass

    