import unittest
from board import Board


from pawn import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        white_pawns = [Pawn('WP') for _ in range(8)]
        black_pawns = [Pawn('BP') for _ in range(8)]

        for i, pawn in enumerate(white_pawns):
            board.place_piece(pawn, i, 1)

        for i, pawn in enumerate(black_pawns):
            board.place_piece(pawn, i, 6)

    def test_valid_move_forward(self):
        # Test 1: Move pawn testing if take piece is working correctly
        self.board.place_piece(Pawn('BP'), 2, 2)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        result = Pawn.take_piece_wp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the white pawn.")
        print("Test 1 for WP_take_piece Passed")

        # Test 2: Now on the other side
        self.board.place_piece(Pawn('BP'),3, 2)
        from_x, from_y = 4, 1
        to_x, to_y = 3, 2
        result = Pawn.take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the white pawn.")
        print("Test 2 for WP_take_piece Passed")

        # Test 3: Makes sure you can't take piece from behind
        self.board.place_piece(Pawn('WP'), 2, 2)
        self.board.place_piece(Pawn('BP'),1, 1)
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        result = Pawn.take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the white pawn.")
        print("Test 3 for WP_take_piece Passed")

        # Test 4: Now the other side from behind
        self.board.place_piece(Pawn('WP'), 6, 6)
        self.board.place_piece(Pawn('BP'),5, 5)
        from_x, from_y = 6, 6
        to_x, to_y = 5, 5
        result = Pawn.take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the white pawn.")
        print("Test 4 for WP_take_piece Passed")

        # Test 5: Tests to make sure we can't take piece that's not there
        self.board.place_piece(Pawn('WP'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        result = Pawn.take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WP', "Target position should have the white pawn.")
        print("Test 5 for WP_take_piece Passed")


if __name__ == '__main__':
    unittest.main()
