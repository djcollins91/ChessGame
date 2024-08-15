import unittest
from board import Board
from helper import rooks, board_width
from Pieces.rooks.white.white_rook import White_Rook
from Pieces.rooks.black.black_rook import Black_Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        rooks(board, board_width)

    def test_take_WR(self):
        # Test 1: Move White_Rook testing if take White_Rook is working correctly
        self.board.place_piece(White_Rook('WR'), 1, 1)
        self.board.place_piece(Black_Rook('BR'), 2, 1)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Rook after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the White_Rook.")
        print("Test 1 for WR_take_piece Passed")

        # Test 2: Move White_Rook to an empty space (valid move)
        self.board.place_piece(White_Rook('WR'), 3, 1)
        self.board.place_piece(Black_Rook('BR'), 3, 7)
        from_x, from_y = 3, 1
        to_x, to_y = 3, 7
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Rook after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the White_Rook.")
        print("Test 2 for WR_move Passed")

        # Test 3: Make sure you can't take piece when on of your pieces is in the way
        self.board.place_piece(White_Rook('WR'), 4, 4)
        self.board.place_piece(White_Rook('WR'), 4, 2)
        self.board.place_piece(Black_Rook('BR'), 4, 1)
        from_x, from_y = 4, 4
        to_x, to_y = 4, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 3 for WR_take_piece Passed")

        

if __name__ == '__main__':
    unittest.main()
