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
        print(board)
        
    def test_valid_move_forward(self):
        #Test 1: testing moving up
        self.board.place_piece(White_Knight('WN'), 1, 4)
        from_x, from_y = 1, 4
        to_x, to_y = 0, 6
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 1 for WN_move passed")

        # Test 2: Testing if can move right
        self.board.place_piece(White_Knight('WN'), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 2, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 2 for WN_move passed")

        # Test 3: Testing if piece can move left
        self.board.place_piece(White_Knight('WN'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 0, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the white Piece.")
        print("Test 3 for WN_move passed")


        # Test 4: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(White_Knight('WN'), 3, 3)
        self.board.place_piece(White_Knight('WN'), 4, 4)  # Place another white Piece in front
        self.board.place_piece(White_Knight('WN'), 3, 4)  # Place another white Piece in front
        from_x, from_y = 3, 3
        to_x, to_y = 5, 4  # Invalid move as the spot is occupied
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WN', "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should still have the white Piece.")
        print("Test 4 for WN_move passed")

if __name__ == '__main__':
    unittest.main()
