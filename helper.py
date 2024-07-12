from pieces import Pawn


def initialize_pieces(board):
    # Create 8 pieces of the same type for both sides, for example, pawns
    white_pawns = [Pawn('wp') for _ in range(8)]
    black_pawns = [Pawn('bP') for _ in range(8)]

    # Place the white pawns on the board, in row 2 (index 1)
    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 0)  # Placing white pawns at (0,1), (1,1), ..., (7,1)

    # Place the black pawns on the board, in row 7 (index 6)
    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 7)  # Placing black pawns at (0,6), (1,6), ..., (7,6)
