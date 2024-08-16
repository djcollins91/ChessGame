from piece import Piece


def exploration(first_option1,first_option2,second_option1,second_option2,piece,board,from_x,from_y,to_x,to_y):
    if (first_option1 is None) or (first_option2 is None):
        #investigating first option 1
        if (first_option1 is None):
            if (second_option1 is None): #it's a valid move
                return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        #when firstoption_1 doesn't workout 
        elif (first_option2 is None):
            if (second_option2 is None):
                return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)