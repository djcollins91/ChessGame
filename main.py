from board import Board
from pieces import Pawn

def initialize_pieces(board):
    # Create 8 pieces of the same type for both sides, for example, pawns
    white_pawns = [Pawn('WP') for _ in range(8)]
    black_pawns = [Pawn('BP') for _ in range(8)]

    # Place the white pawns on the board, in row 2 (index 1)
    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)  # Placing white pawns at (0,1), (1,1), ..., (7,1)

    # Place the black pawns on the board, in row 7 (index 6)
    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)  # Placing black pawns at (0,6), (1,6), ..., (7,6)

def move_wp(board, from_x, from_y, to_x, to_y):
    piece = board.grid[from_y][from_x]
    
    if piece is None or str(piece) != 'WP':
        return "Invalid move"
    
    # Check if the move is within bounds
    if not (0 <= to_x < board.WIDTH and 0 <= to_y < board.LENGTH):
        return "Invalid move"
    
    # Moving up 1 square
    if to_x == from_x and to_y == from_y + 1 and board.grid[to_y][to_x] is None:
        board.grid[to_y][to_x] = piece
        board.grid[from_y][from_x] = None
        return "Valid move"
    
    # Moving up 2 squares from initial position
    if from_y == 0 and to_x == from_x and to_y == from_y + 2 and board.grid[to_y][to_x] is None:
        board.grid[to_y][to_x] = piece
        board.grid[from_y][from_x] = None
        return "Valid move"

    return "Invalid move"



def main():
    # Create a board
    board = Board()

    # Initialize and place pieces on the board
    initialize_pieces(board)

    # Print the initial board
    print("Initial board:")
    print(board)

    # Highlight possible moves for a white pawn at (1,1)
    highlighted_grid = board.highlight_moves(0, 0)
    print("Possible moves for white pawn at (0,0):")
    board.print_highlighted_grid(highlighted_grid)

    # # Move a white pawn
    # move_wp(board, 1, 1, 1, 2)

    # # Print the board after the move
    # print("Board after moving white pawn from (1,1) to (1,2):")
    # print(board)

if __name__ == '__main__':
    main()
