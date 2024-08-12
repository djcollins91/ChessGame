from board import Board
from piece import Piece
board_width = range(Board.getWIDTH())

#creates the pawns
def pawns(board, board_width):
    # Create white and black pawns with specific classes
    white_pawns = [Piece('WP') for _ in board_width]
    black_pawns = [Piece('BP') for _ in board_width]

    #places the white_pawns
    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)

    #places the black_pawns
    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)

# creates the rooks
def rooks(board, board_width):
    # Create white and black rooks with specific classes
    white_rooks = [Piece('WR') for _ in board_width]
    black_rooks = [Piece('BR') for _ in board_width]

    #places the white_rooks
    for i, rook in enumerate(white_rooks):
        if(i == 0) or (i == 7):
            board.place_piece(rook, i, 0)
            
    #places the black_rooks
    for i, rook in enumerate(black_rooks):
        if (i == 0) or (i == 7):
            board.place_piece(rook, i, 7)

#creates the kings
def kings(board, board_width):
    # Create white and black queens with specific classes
    white_kings = [Piece('WK') for _ in board_width]
    black_kings = [Piece('BK') for _ in board_width]

    #places the white_kings
    for i, king in enumerate(white_kings):
        if(i == 4):
            board.place_piece(king, i, 0)
            
    #places the black_kings
    for i, king in enumerate(black_kings):
        if (i == 4):
            board.place_piece(king, i, 7)

#creates the queenss
def queens(board, board_width):
    # Create white and black queens with specific classes
    white_queens = [Piece('WQ') for _ in board_width]
    black_queens = [Piece('BQ') for _ in board_width]

    #places the white_queens
    for i, queen in enumerate(white_queens):
        if(i == 3):
            board.place_piece(queen, i, 0)
            
    #places the black_queens
    for i, queen in enumerate(black_queens):
        if (i == 3):
            board.place_piece(queen, i, 7)

#creates the bishops
def bishops(board, board_width):
    # Create white and black bishops with specific classes
    white_bishops = [Piece('WB') for _ in board_width]
    black_bishops = [Piece('BB') for _ in board_width]

    #places the white_bishops
    for i, bishop in enumerate(white_bishops):
        if(i == 2) or (i == 5):
            board.place_piece(bishop, i, 0)
            
    #places the black_bishops
    for i, bishop in enumerate(black_bishops):
        if (i == 2) or (i == 5):
            board.place_piece(bishop, i, 7)

#creates the knights
def knights(board, board_width):
    # Create white and black rooks with specific classes
    white_knights = [Piece('WN') for _ in board_width]
    black_knights = [Piece('BN') for _ in board_width]

    #places the white_knights
    for i, knight in enumerate(white_knights):
        if(i == 1) or (i == 6):
            board.place_piece(knight, i, 0)
            
    #places the black_kings
    for i, knight in enumerate(black_knights):
        if (i == 1) or (i == 6):
            board.place_piece(knight, i, 7)

            
# puts each piece on the board
def initialize_pieces(board, board_width):
    pawns(board, board_width)
    rooks(board, board_width)
    kings(board, board_width)
    queens(board, board_width)
    bishops(board, board_width)
    knights(board, board_width)

    