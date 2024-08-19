import sys
from game_board import GameBoard
from helper import initialize_pieces,board_width
from PyQt5.QtWidgets import QApplication

def main():
    # initialize_pieces(board, board_width)
    app = QApplication(sys.argv)
    board = GameBoard()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
