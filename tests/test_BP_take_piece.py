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

    def test_take_bp(self):
        # Test 1: Move pawn and capture piece
        self.board.place_piece(Pawn('WP'), 2, 2)
        self.board.place_piece(Pawn('BP'), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 2, 2
        result = Pawn.take_piece_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the black pawn.")
        print("Test 1 for BP_take_piece Passed")

        # Test 2: Moving black pawn but no white piece to capture
        self.board.place_piece(Pawn('BP'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 3, 3
        result = Pawn.take_piece_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the pawn.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should be empty.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'BP', "Original position should still have the black pawn.")
        print("Test 2 for BP_take_piece Passed")

        # Test 3: Make sure you can't take a piece from behind
        self.board.place_piece(Pawn('WP'), 2, 2)
        self.board.place_piece(Pawn('BP'), 3, 3)
        from_x, from_y = 2, 2
        to_x, to_y = 3, 3
        result = Pawn.take_piece_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the pawn.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other pawn.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WP', "Original position should still have the white pawn.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the black pawn.")
        print("Test 3 for BP_take_piece Passed")

        # Test 4: Black pawn moving from behind but valid capture
        self.board.place_piece(Pawn('WP'), 5, 5)
        self.board.place_piece(Pawn('BP'), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 5, 5
        result = Pawn.take_piece_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the black pawn.")
        print("Test 4 for BP_take_piece Passed")

        

if __name__ == '__main__':
    unittest.main()
