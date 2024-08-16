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
        #Test 1: testing moving up and to the right
        self.board.place_piece(White_Knight('WN'), 1, 4)
        from_x, from_y = 1, 4
        to_x, to_y = 2, 6
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 1 for WN_move passed")

        # Test 2: testing moving up and to the left
        self.board.place_piece(White_Knight('WN'), 1, 1)
        from_x, from_y = 1, 1
        to_x, to_y = 0, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 2 for WN_move passed")

        # Test 3: Testing if piece can move down and to the right
        self.board.place_piece(White_Knight('WN'), 2, 3)
        from_x, from_y = 2, 3
        to_x, to_y = 3, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 3 for WN_move passed")

        # Test 4: Testing if piece can move down and to the left
        self.board.place_piece(White_Knight('WN'), 5, 5)
        from_x, from_y = 4, 3
        to_x, to_y = 4, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 4 for WN_move passed")


        # Test 5: Testing if piece can move 2 to the right and up
        self.board.place_piece(White_Knight('WN'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 6, 5
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 5 for WN_move passed")

        # Test 6:Testing if piece can move 2 to the right and down
        self.board.place_piece(White_Knight('WN'), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 5, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 6 for WN_move passed")


if __name__ == '__main__':
    unittest.main()
