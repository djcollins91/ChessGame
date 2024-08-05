import unittest
from board import Board
from white_pawn import White_Pawn
from black_pawn import Black_Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        # Create white and black pawns with specific classes
        white_pawns = [White_Pawn('WP') for _ in range(8)]
        black_pawns = [Black_Pawn('BP') for _ in range(8)]

        for i, pawn in enumerate(white_pawns):
            board.place_piece(pawn, i, 1)

        for i, pawn in enumerate(black_pawns):
            board.place_piece(pawn, i, 6)

    def test_take_bp(self):
        # Test 1: Move White_Pawn testing if take White_Pawn is working correctly
        self.board.place_piece(Black_Pawn('BP'), 2, 2)
        self.board.place_piece(White_Pawn('WP'), 1, 1)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the White_Pawn.")
        print("Test 1 for WP_take_piece Passed")

        # Test 2: Move White_Pawn to an empty space (valid move)
        self.board.place_piece(White_Pawn('WP'), 3, 1)
        from_x, from_y = 3, 1
        to_x, to_y = 3, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the White_Pawn.")
        print("Test 2 for WP_move Passed")

        # Test 3: Make sure you can't take White_Pawn from behind
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

        # Test 5: Tests to make sure we can't take White_Pawn that's not there
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
