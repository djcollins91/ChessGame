from board import Board
from helper import initialize_pieces






def main():
    # Create a board
    board = Board()

    # Initialize and place pieces on the board
    initialize_pieces(board)

    # Print the board
    print(board)

if __name__ == '__main__':
    main()
