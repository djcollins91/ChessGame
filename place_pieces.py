from Pieces.bishops.black.black_bishop import Black_Bishop
from Pieces.bishops.white.white_bishop import White_Bishop
from Pieces.kings.black.black_king import Black_King
from Pieces.kings.white.white_king import White_King
from Pieces.knights.black.black_knight import Black_Knight
from Pieces.knights.white.white_knight import White_Knight
from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.queens.black.black_queen import Black_Queen
from Pieces.queens.white.white_queen import White_Queen
from Pieces.rooks.black.black_rook import Black_Rook
from Pieces.rooks.white.white_rook import White_Rook


LOOP_SIZE = 8
def place_black_pawn(board):
    # Place black pawns on row 6
    for col in range(LOOP_SIZE):
        board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), col, Black_Pawn.get_starting_row())  # columns 0-7, row 6
    
def place_white_pawn(board):
    for col in range(LOOP_SIZE):
        board.place_piece(White_Pawn(White_Pawn.get_piece_str()), col, White_Pawn.get_starting_row())  # columns 0-7, row 6

#place for black rooks
def place_black_rook(board):
    for col in range(LOOP_SIZE):
        if col == Black_Rook.get_starting_col_1() or col == Black_Rook.get_starting_col_2():
            board.place_piece(Black_Rook(Black_Rook.get_piece_str()), col, Black_Rook.get_starting_row())
            
#place for white rooks
def place_white_rook(board): 
    for col in range(LOOP_SIZE):
        if col == White_Rook.get_starting_col_1() or col == White_Rook.get_starting_col_2():
            board.place_piece(White_Rook(White_Rook.get_piece_str()), col, White_Rook.get_starting_row())

#place for black bishops
def place_black_bishop(board):
    for col in range(LOOP_SIZE):
        if col == Black_Bishop.get_starting_col_1() or col == Black_Bishop.get_starting_col_2():
            board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), col, Black_Bishop.get_starting_row())

#place for white bishops
def place_white_bishop(board):
    for col in range(LOOP_SIZE):
        if col == White_Bishop.get_starting_col_1() or col == White_Bishop.get_starting_col_2():
            board.place_piece(White_Bishop(White_Bishop.get_piece_str()), col, White_Bishop.get_starting_row())
    
#place for black knights
def place_black_knight(board):
    for col in range(LOOP_SIZE):
        if col == Black_Knight.get_starting_col_1() or col == Black_Knight.get_starting_col_2():
            board.place_piece(Black_Knight(Black_Knight.get_piece_str()), col, Black_Knight.get_starting_row())

#place for white knights
def place_white_knight(board):
    for col in range(LOOP_SIZE):
        if col == White_Knight.get_starting_col_1() or col == White_Knight.get_starting_col_2():
            board.place_piece(White_Knight(White_Knight.get_piece_str()), col, White_Knight.get_starting_row())

#place for black king
def place_black_king(board):
    for col in range(LOOP_SIZE):
        if col == Black_King.get_starting_col():
            board.place_piece(Black_King(Black_King.get_piece_str()), col, Black_King.get_starting_row())

#place for white king
def place_white_king(board):
    for col in range(LOOP_SIZE):
        if col == White_King.get_starting_col():
            board.place_piece(White_King(White_King.get_piece_str()), col, White_King.get_starting_row())
    
#place for black queen
def place_black_queen(board):
    for col in range(LOOP_SIZE):
        if col == Black_Queen.get_starting_col():
            board.place_piece(Black_Queen(Black_Queen.get_piece_str()), col, Black_Queen.get_starting_row())

#place for white queen
def place_white_queen(board):
    for col in range(LOOP_SIZE):
        if col == White_Queen.get_starting_col():
            board.place_piece(White_Queen(White_Queen.get_piece_str()), col, White_Queen.get_starting_row())