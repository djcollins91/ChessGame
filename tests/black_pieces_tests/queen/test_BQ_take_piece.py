import unittest
from Pieces.queens.black.black_queen import Black_Queen
from Pieces.queens.white.white_queen import White_Queen
from board import Board
from helper import board_width, queens



class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        queens(board, board_width)
        
    def test_take_BQ(self):
        # Test 1: Valid capture of Black_Queen by White_Queen
        self.board.place_piece(Black_Queen('BQ'), 1, 1)
        self.board.place_piece(White_Queen('WQ'), 2, 2)
        
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Queen after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BQ', "Target position should have the White_Queen.")
        print("Test 1 for BQ_take_piece Passed")

        # Test 2: Move White_Queen from behind (valid)
        self.board.place_piece(Black_Queen('BQ'), 2, 2)
        self.board.place_piece(White_Queen('WQ'), 1, 1)
        
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Queen after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BQ', "Target position should have the White_Queen.")
        print("Test 2 for BQ_take_piece Passed")

        # Test 3: Invalid capture (no piece at target)
        self.board.place_piece(Black_Queen('BQ'), 4, 4)
        
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Queen.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should still be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'BQ', "Original position should still have the White_Queen.")
        print("Test 3 for BQ_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
