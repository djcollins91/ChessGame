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
    # Create white and black rooks with specific classes
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

def initialize_pieces(board, board_width):
    pawns(board, board_width)
    rooks(board, board_width)
    kings(board, board_width)

    