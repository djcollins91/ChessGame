import unittest
from Pieces.bishops.black.black_bishop import Black_Bishop
from Pieces.bishops.white.white_bishop import White_Bishop
from board import Board
from helper import bishops, board_width

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        bishops(board, board_width)

    def test_take_BB(self):
        # Test 1: Valid capture of Black_Bishop by White_Bishop
        self.board.place_piece(White_Bishop('WB'), 1, 1)
        self.board.place_piece(Black_Bishop('BB'), 2, 2)
        
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Bishop after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WB', "Target position should have the White_Bishop.")
        print("Test 1 for WB_take_piece Passed")

        # Test 2: Invalid capture (not diagonal)
        self.board.place_piece(White_Bishop('WB'), 3, 1)
        self.board.place_piece(Black_Bishop('BB'), 3, 2)
        
        from_x, from_y = 3, 1
        to_x, to_y = 3, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Bishop.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Bishop.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WB', "Original position should still have the White_Bishop.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BB', "Target position should still have the Black_Bishop.")
        print("Test 2 for WB_take_piece Passed")

        # Test 3: Move White_Bishop from behind (invalid capture)
        self.board.place_piece(White_Bishop('WB'), 2, 2)
        self.board.place_piece(Black_Bishop('BB'), 1, 1)
        
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Bishop.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Bishop.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WB', "Original position should still have the White_Bishop.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BB', "Target position should still have the Black_Bishop.")
        print("Test 3 for WB_take_piece Passed")

        # Test 4: White pawn moving from behind but invalid capture
        self.board.place_piece(White_Bishop('WB'), 6, 6)
        self.board.place_piece(Black_Bishop('BB'), 3, 3)
        
        from_x, from_y = 6, 6
        to_x, to_y = 3, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Bishop.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Bishop.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WB', "Original position should still have the White_Bishop.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BB', "Target position should still have the Black_Bishop.")
        print("Test 4 for WB_take_piece Passed")

        # Test 5: Invalid capture (no piece at target)
        self.board.place_piece(White_Bishop('WB'), 4, 4)
        
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Bishop.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should still be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WB', "Original position should still have the White_Bishop.")
        print("Test 5 for WB_take_piece Passed")

        # Test 6: Invalid capture (no piece at target)
        self.board.place_piece(White_Bishop('WB'), 4, 4)
        self.board.place_piece(White_Bishop('WB'), 5, 3)
        self.board.place_piece(Black_Bishop('BB'), 6, 2)
        
        from_x, from_y = 4, 4
        to_x, to_y = 6, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 6 for WB_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
