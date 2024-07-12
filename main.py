from board import Board
from pieces import Pawn

def move_wp(board, from_x, from_y, to_x, to_y):
    piece = board.grid[from_y][from_x]
    if piece and str(piece) == 'WP':
        if (from_y == 1 and to_y in [2, 3]) or (from_y != 1 and to_y == from_y + 1):
            if board.grid[to_y][to_x] is None:
                board.grid[to_y][to_x] = piece
                board.grid[from_y][from_x] = None
                return "Valid move"
    return "Invalid move"

def initialize_pieces(board):
    white_pawns = [Pawn('WP') for _ in range(8)]
    black_pawns = [Pawn('BP') for _ in range(8)]

    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)

    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)

def main():
    # Create a board
    board = Board()

    # Initialize and place pieces on the board
    initialize_pieces(board)

    # Print the board
    print(board)

if __name__ == '__main__':
    main()
