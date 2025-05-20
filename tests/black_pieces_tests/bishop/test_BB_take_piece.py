import unittest
from pieces.bishops.black.black_bishop import Black_Bishop
from pieces.bishops.white.white_bishop import White_Bishop
from board import Board
from place_pieces import place_black_bishop

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_black_bishop(board)

    def test_take_BB(self):
        from pieces.empty.empty import Empty_Spot
        # Test 1: Valid capture of White_Bishop by Black_Bishop (diagonal)
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 1, 1)
        self.board.place_piece(White_Bishop(White_Bishop.get_piece_str()), 2, 2)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(self.board.grid[from_y][from_x], to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Bishop, "Target position should have the Black_Bishop after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_Bishop.get_piece_str(), "Target position should have the Black_Bishop.")
        print("Test 1 for BB_take_piece Passed")

        # Test 2: Invalid capture (not diagonal)
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 3, 1)
        self.board.place_piece(White_Bishop(White_Bishop.get_piece_str()), 3, 2)
        from_x, from_y = 3, 1
        to_x, to_y = 3, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        print("Test 2 for BB_take_piece Passed")

        # Test 3: Valid capture in reverse diagonal
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 2, 2)
        self.board.place_piece(White_Bishop(White_Bishop.get_piece_str()), 1, 1)
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(self.board.grid[from_y][from_x], to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        print("Test 3 for BB_take_piece Passed")

        # Test 4: Valid long diagonal capture
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 6, 6)
        self.board.place_piece(White_Bishop(White_Bishop.get_piece_str()), 3, 3)
        from_x, from_y = 6, 6
        to_x, to_y = 3, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(self.board.grid[from_y][from_x], to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        print("Test 4 for BB_take_piece Passed")

        # Test 5: Invalid capture (no piece at target)
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Black_Bishop, "Original position should still have the Black_Bishop.")
        self.assertTrue(isinstance(self.board.grid[to_y][to_x], Empty_Spot) or self.board.grid[to_y][to_x] is None, "Target position should still be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), Black_Bishop.get_piece_str(), "Original position should still have the Black_Bishop.")
        print("Test 5 for BB_take_piece Passed")

        # Test 6: Invalid capture (blocked by another piece)
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 4, 4)
        self.board.place_piece(Black_Bishop(Black_Bishop.get_piece_str()), 5, 3)
        self.board.place_piece(White_Bishop(White_Bishop.get_piece_str()), 6, 2)
        from_x, from_y = 4, 4
        to_x, to_y = 6, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        print("Test 6 for BB_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
