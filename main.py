import sys
from board import Board
from game_board import GameBoard
from helper import initialize_pieces, board_width
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel

def main():
    # # Create a board
    # board = Board()
    # # Initialize and place pieces on the board
    # initialize_pieces(board,board_width)
    # app = QApplication(sys.argv)
    # new_board = GameBoard()
    # GameBoard.on_piece_clicked(self, row,col)
    # sys.exit(app.exec_())
    # print(board)
    app = QApplication(sys.argv)
    board = GameBoard()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
