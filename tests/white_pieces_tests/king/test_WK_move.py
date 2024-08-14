import unittest
from board import Board
from helper import kings, board_width
from white_pieces.king.white_king import White_King
from white_pieces.pawn.white_pawn import White_Pawn


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        kings(board, board_width)
        

    def test_valid_move_forward(self):
        #Test 1: testing moving up
        from_x, from_y = 0, 1
        to_x, to_y = 1, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the white Piece.")
        print("Test 1 for WK_move passed")

        # Test 2: Testing if can move right
        self.board.place_piece(White_King('WK'), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 0, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the white Piece.")
        print("Test 2 for WK_move passed")

        # Test 3: Testing if piece can move left
        self.board.place_piece(White_King('WK'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 2, 1
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the white Piece.")
        print("Test 3 for WK_move passed")

        # Test 4: Testing if piece can move backwards
        self.board.place_piece(White_King('WK'), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 5
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should have the white Piece.")
        print("Test 4 for WK_move passed")

        
        # Test 5: Testing to see piece can't move diagonal
        self.board.place_piece(White_King('WK'), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 5 
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNone(self.board.grid[to_y][to_x], "Target position should be empty.")
        print("Test 5 for WK_move passed")

        # Test 6: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(White_King('WK'), 3, 3)
        self.board.place_piece(White_King('WK'), 3, 2)  # Place another white Piece in front
        from_x, from_y = 3, 3
        to_x, to_y = 3, 2  # Invalid move as the spot is occupied
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WK', "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should still have the white Piece.")
        print("Test 6 for WK_move passed")


        # Test 7: Testing if piece can't move two spot
        self.board.place_piece(White_King('WK'), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 5, 7  # Invalid move as the spot is occupied
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        self.assertIsNotNone(self.board.grid[from_y][from_x], "Original position should still have the Piece.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should still have the other Piece.")
        self.assertEqual(str(self.board.grid[from_y][from_x]), 'WK', "Original position should still have the white Piece.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WK', "Target position should still have the white Piece.")
        print("Test 7 for WK_move passed")

if __name__ == '__main__':
    unittest.main()
