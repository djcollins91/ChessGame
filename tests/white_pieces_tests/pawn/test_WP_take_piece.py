import unittest
from board import Board
from helper import pawns, board_width
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.pawns.black.black_pawn import Black_Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        pawns(board, board_width)

    def test_take_bp(self):
        # Test 1: Valid capture of Black_Pawn by White_Pawn
        self.board.place_piece(White_Pawn('WP'), 1, 1)
        self.board.place_piece(Black_Pawn('BP'), 2, 2)
        
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the White_Pawn.")
        print("Test 1 for WP_take_piece Passed")

        # Test 2: Invalid capture (not diagonal)
        self.board.place_piece(White_Pawn('WP'), 3, 1)
        self.board.place_piece(Black_Pawn('BP'), 3, 2)
        
        from_x, from_y = 3, 1
        to_x, to_y = 3, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Pawn.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Pawn.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WP', "Original position should still have the White_Pawn.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the Black_Pawn.")
        print("Test 2 for WP_take_piece Passed")

        # Test 3: Move White_Pawn from behind (invalid capture)
        self.board.place_piece(White_Pawn('WP'), 2, 2)
        self.board.place_piece(Black_Pawn('BP'), 1, 1)
        
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Pawn.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Pawn.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WP', "Original position should still have the White_Pawn.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the Black_Pawn.")
        print("Test 3 for WP_take_piece Passed")

        # Test 4: White pawn moving from behind but invalid capture
        self.board.place_piece(White_Pawn('WP'), 6, 6)
        self.board.place_piece(Black_Pawn('BP'), 5, 5)
        
        from_x, from_y = 6, 6
        to_x, to_y = 5, 5
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Pawn.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the Black_Pawn.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WP', "Original position should still have the White_Pawn.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the Black_Pawn.")
        print("Test 4 for WP_take_piece Passed")

        # Test 5: Invalid capture (no piece at target)
        self.board.place_piece(White_Pawn('WP'), 4, 4)
        
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the White_Pawn.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should still be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WP', "Original position should still have the White_Pawn.")
        print("Test 5 for WP_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
