import unittest
from board import Board
from helper import rooks, board_width
from white_pieces.rook.white_rook import White_Rook
from black_pieces.rook.black_rook import Black_Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        rooks(board, board_width)

    def test_take_BR(self):
        # Test 1: Move Black_Rook testing if it can take White_Rook
        self.board.place_piece(Black_Rook('BR'), 1, 1)
        self.board.place_piece(White_Rook('WR'), 2, 1)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Black Rook should be able to take White Rook.")
        print("Test 1 for BR_take_piece Passed")

        # Test 2: Move White_Rook to an empty space (valid move)
        self.board.place_piece(Black_Rook('BR'), 3, 1)  # Place White Rook at (3, 1)
        self.board.place_piece(White_Rook('WR'), 3, 7)  # Place White Rook at (3, 1)
        from_x, from_y = 3, 1
        to_x, to_y = 3, 7
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        print("Test 2 for WR_take_piece Passed")

        # Test 3: Make sure you can't take piece when one of your pieces is in the way
        self.board.place_piece(Black_Rook('BR'), 4, 4)
        self.board.place_piece(Black_Rook('BR'), 4, 2)
        self.board.place_piece(White_Rook('WR'), 4, 1)
        from_x, from_y = 4, 4
        to_x, to_y = 4, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 3 for BR_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
