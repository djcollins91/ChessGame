import unittest
from board import Board
from helper import kings, board_width
from white_pieces.king.white_king import White_King
from black_pieces.king.black_king import Black_King

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        kings(board, board_width)
        
    def test_take_BK(self):
        # Test 1: Valid capture of Black_King by White_King
        self.board.place_piece(White_King('WK'), 1, 1)
        self.board.place_piece(Black_King('BK'), 2, 2)
        
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_King after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the White_King.")
        print("Test 1 for WK_take_piece Passed")

        # Test 2: Move White_King from behind (valid)
        self.board.place_piece(White_King('WK'), 2, 2)
        self.board.place_piece(Black_King('BK'), 1, 1)
        
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_King after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the White_King.")
        print("Test 2 for WK_take_piece Passed")

        # Test 3: Invalid capture (no piece at target)
        self.board.place_piece(White_King('WK'), 4, 4)
        
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_King.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should still be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WK', "Original position should still have the White_King.")
        print("Test 3 for WK_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
