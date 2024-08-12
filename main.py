from board import Board
from helper import initialize_pieces, board_width

def main():
    # Create a board
    board = Board()
    # Initialize and place pieces on the board
    initialize_pieces(board,board_width)
    # Print the board
    print(board)

if __name__ == '__main__':
    main()
