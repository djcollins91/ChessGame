from pawn import Pawn


def initialize_pieces(board):
    white_pawns = [Pawn('WP') for _ in range(8)]
    black_pawns = [Pawn('BP') for _ in range(8)]

    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)

    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)