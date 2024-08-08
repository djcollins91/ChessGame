from board import Board
from piece import Piece


def initialize_pieces(board):
    # gets the width of the board from the Board class
    board_width = range(Board.getWIDTH())

    # Create white and black pawns with specific classes
    white_pawns = [Piece('WP') for _ in board_width]
    black_pawns = [Piece('BP') for _ in board_width]

    #places the white_pawns
    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)

    #places the black_pawns
    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)

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