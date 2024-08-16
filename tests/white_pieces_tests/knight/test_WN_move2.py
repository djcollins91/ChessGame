import unittest
from Pieces.knights.white.white_knight import White_Knight
from board import Board
from helper import board_width, knights

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        knights(board, board_width)
        
    def test_valid_move_forward(self):
        # Test 7:Testing if piece can move 2 to the left and up
        self.board.place_piece(White_Knight('WN'), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 1, 4
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 7 for WN_move passed")

         # Test 8:Testing if piece can move 2 to the left and down
        self.board.place_piece(White_Knight('WN'), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 3, 4
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 8 for WN_move passed")


if __name__ == '__main__':
    unittest.main()