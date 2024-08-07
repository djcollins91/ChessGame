import unittest
from board import Board
from white_pieces.pawn.white_pawn import White_Pawn
from black_pieces.pawn.black_pawn import Black_Pawn  # Import specific pawn classes

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        white_pawns = [White_Pawn('BP') for _ in range(8)]
        black_pawns = [Black_Pawn('BP') for _ in range(8)]

        for i, Piece in enumerate(white_pawns):
            board.place_piece(Piece, i, 1)

        for i, Piece in enumerate(black_pawns):
            board.place_piece(Piece, i, 6)

    def test_valid_move_forward(self):
        # Test 1: Move Piece forward by 1 square from initial position
        from_x, from_y = 1, 6
        to_x, to_y = 1, 5
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white Piece.")
        print("Test 1 for bp_move passed")

        # Test 2: Move Piece forward by 2 squares from initial position
        from_x, from_y = 0, 6
        to_x, to_y = 0, 4
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white Piece.")
        print("Test 2 for bp_move passed")

        # Test 3: Move Piece forward by 1 square from non-initial position
        self.board.place_piece(Black_Pawn('BP'), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 5, 4
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white Piece.")
        print("Test 3 for bp_move passed")

        # Test 4: Move Piece forward by 1 square from random position
        self.board.place_piece(Black_Pawn('BP'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 4, 3
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white Piece.")
        print("Test 4 for bp_move passed")

        # Test 5: Move Piece forward by 1 square from initial position (0, 1)
        self.board.place_piece(Black_Pawn('BP'), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 5
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should have the white Piece.")
        print("Test 5 for bp_move passed")


        # Test 6: Move Piece sideways (invalid move)
        self.board.place_piece(Black_Pawn('BP'), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 2, 3  # Invalid move for a Piece
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should be empty.")
        print("Test 6 for bp_move passed")

        # Test 7: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(Black_Pawn('BP'), 4, 4)
        self.board.place_piece(Black_Pawn('BP'), 4, 3)  # Place another white Piece in front
        from_x, from_y = 4, 4
        to_x, to_y = 4, 3  # Invalid move as the spot is occupied
        result = Black_Pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'BP', "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'BP', "Target position should still have the white Piece.")
        print("Test 7 for bp_move passed")

    
        

        

if __name__ == '__main__':
    unittest.main()
