import unittest
from board import Board
from pieces.rooks.white.white_rook import White_Rook
from pieces.empty.empty import Empty_Spot
from place_pieces import place_white_rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_white_rook(board)
        
    def test_valid_move_forward(self):
        # Test 1: Move Piece forward by 1 square from initial position
        from_x, from_y = 0, 0
        to_x, to_y = 0, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Rook.get_piece_str(), "Target position should have the white Piece.")
        print("Test 1 for WR_move passed")

        # Test 2: Move Piece forward by 1 square from non-initial position
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 2, 7
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Rook.get_piece_str(), "Target position should have the white Piece.")
        print("Test 2 for WR_move passed")

        # Test 3: Move Piece forward by 1 square from random position
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 0
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Rook.get_piece_str(), "Target position should have the white Piece.")
        print("Test 3 for WR_move passed")

        # Test 4: Move Piece forward by 1 square from initial position (0, 1)
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 0, 0
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Rook.get_piece_str(), "Target position should have the white Piece.")
        print("Test 4 for WR_move passed")

        # Test 5: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 4, 4)
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 4, 5)  # Place another white Piece in front
        from_x, from_y = 4, 4
        to_x, to_y = 4, 5  # Invalid move as the spot is occupied
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], White_Rook, "Original position should still have the Piece.")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), White_Rook.get_piece_str(), "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Rook.get_piece_str(), "Target position should still have the white Piece.")
        print("Test 5 for WR_move passed")

        # Test 6: Checks to see rook can't move diagonal
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 4, 3)
        from_x, from_y = 4, 3
        to_x, to_y = 5, 4 
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], White_Rook, "Original position should still have the Piece.")
        print("Test 6 for WR_move passed")

if __name__ == '__main__':
    unittest.main()
