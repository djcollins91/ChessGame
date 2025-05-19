from PyQt5.QtWidgets import QApplication
import sys
from game_board import GameBoard
from board import Board
from place_pieces import place_black_bishop, place_black_king, place_black_knight, place_black_pawn, place_black_queen, place_black_rook, place_white_bishop, place_white_king, place_white_knight, place_white_pawn, place_white_queen, place_white_rook
LOOP_SIZE = 8
def main():
    app = QApplication(sys.argv)
    board = Board()
    
    # place_black_pawn(board)
    # place_white_pawn(board)
    # place_black_bishop(board)
    # place_white_bishop(board)
    # place_black_rook(board)
    # place_white_rook(board)
    place_black_knight(board)
    place_white_knight(board)
    # place_black_king(board)
    # place_white_king(board)
    # place_black_queen(board)
    # place_white_queen(board)
    


    game = GameBoard(board)
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
