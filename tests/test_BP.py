import unittest
from board import Board

from pawn import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        white_pawns = [Pawn('BP') for _ in range(8)]
        black_pawns = [Pawn('BP') for _ in range(8)]

        for i, pawn in enumerate(white_pawns):
            board.place_piece(pawn, i, 1)

        for i, pawn in enumerate(black_pawns):
            board.place_piece(pawn, i, 6)

    def test_valid_move_forward(self):
        # Test 1: Move pawn forward by 1 square from initial position
        from_x, from_y = 1, 6
        to_x, to_y = 1, 5
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white pawn.")
        print("Test 1 for BP Passed")

        # Test 2: Move pawn forward by 2 squares from initial position
        from_x, from_y = 0, 6
        to_x, to_y = 0, 4
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white pawn.")
        print("Test 2 for BP Passed")

        # Test 3: Move pawn forward by 1 square from non-initial position
        self.board.place_piece(Pawn('BP'), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 5, 4
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white pawn.")
        print("Test 3 for BP Passed")

        # Test 4: Move pawn forward by 1 square from random position
        self.board.place_piece(Pawn('BP'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 4, 3
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white pawn.")
        print("Test 4 for BP Passed")

        # Test 5: Move pawn forward by 1 square from initial position (0, 1)
        self.board.place_piece(Pawn('BP'), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 5
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the pawn after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white pawn.")
        print("Test 5 for BP Passed")


        # Test 6: Move pawn sideways (invalid move)
        self.board.place_piece(Pawn('BP'), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 2, 3  # Invalid move for a pawn
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the pawn.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should be empty.")
        print("Test 6 for BP Passed")

        # Test 7: Move pawn to an occupied spot (invalid move)
        self.board.place_piece(Pawn('BP'), 4, 4)
        self.board.place_piece(Pawn('BP'), 4, 3)  # Place another white pawn in front
        from_x, from_y = 4, 4
        to_x, to_y = 4, 3  # Invalid move as the spot is occupied
        result = Pawn.move_bp(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the pawn.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other pawn.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'BP', "Original position should still have the white pawn.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the white pawn.")
        print("Test 7 for BP Passed")

    
        

        

if __name__ == '__main__':
    unittest.main()
