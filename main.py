from PyQt5.QtWidgets import QApplication
import sys
from Pieces.pawns.white.white_pawn import White_Pawn
from game_board import GameBoard
from board import Board
from Pieces.pawns.black.black_pawn import Black_Pawn

def main():
    app = QApplication(sys.argv)
    board = Board()

    # Place black pawns on row 6
    for col in range(8):
        board.place_piece(Black_Pawn("BP"), col, 6)  # columns 0-7, row 6
    # Place black pawns on row 6
    for col in range(8):
        board.place_piece(White_Pawn("WP"), col, 1)  # columns 0-7, row 6

    game = GameBoard(board)
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
