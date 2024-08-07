import unittest
from board import Board
from white_pieces.rook.White_Rook import White_Rook
from black_pieces.rook.Black_Rook import Black_Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        # Create white and black rooks with specific classes
        white_rooks = [White_Rook('WR') for _ in range(8)]
        black_rooks = [Black_Rook('BR') for _ in range(8)]

        for i, rook in enumerate(white_rooks):
            board.place_piece(rook, i, 1)

        for i, rook in enumerate(black_rooks):
            board.place_piece(rook, i, 6)

    def test_valid_move_forward(self):
        # Test 1: Move Piece forward by 1 square from initial position
        from_x, from_y = 1, 1
        to_x, to_y = 1, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the white Piece.")
        print("Test 1 for WR_move passed")

        # Test 2: Move Piece forward by 2 squares from initial position
        from_x, from_y = 0, 1
        to_x, to_y = 0, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the white Piece.")
        print("Test 2 for WR_move passed")

        # Test 3: Move Piece forward by 1 square from non-initial position
        self.board.place_piece(White_Rook('WR'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 2, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the white Piece.")
        print("Test 3 for WR_move passed")

        # Test 4: Move Piece forward by 1 square from random position
        self.board.place_piece(White_Rook('WR'), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 7
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the white Piece.")
        print("Test 4 for WR_move passed")

        # Test 5: Move Piece forward by 1 square from initial position (0, 1)
        self.board.place_piece(White_Rook('WR'), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 0, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should have the white Piece.")
        print("Test 5 for WR_move passed")

        # Test 6: Move Piece sideways (invalid move)
        self.board.place_piece(White_Rook('WR'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 4  # Invalid move for a Piece
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should be empty.")
        print("Test 6 for WR_move passed")

        # Test 7: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(White_Rook('WR'), 4, 4)
        self.board.place_piece(White_Rook('WR'), 4, 5)  # Place another white Piece in front
        from_x, from_y = 4, 4
        to_x, to_y = 4, 5  # Invalid move as the spot is occupied
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WR', "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WR', "Target position should still have the white Piece.")
        print("Test 7 for WR_move passed")

if __name__ == '__main__':
    unittest.main()
