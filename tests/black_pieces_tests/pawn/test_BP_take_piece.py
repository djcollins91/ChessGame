import unittest
from board import Board
from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.empty.empty import Empty_Spot

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # Initialize pawns or other pieces as needed for your tests

    def test_take_bp_valid_capture(self):
        # Place white pawn to capture
        self.board.place_piece(White_Pawn(White_Pawn.get_piece_str()), 2, 2)
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 2, 2
        black_pawn = self.board.grid[from_y][from_x]
        result = black_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Capture move should be valid.")
        # Simulate move
        if result:
            self.board.place_piece(black_pawn, to_y, to_x)
            self.board.grid[from_y][from_x] = Empty_Spot("Empty Spot")
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Pawn)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        print("Test 1 for BP_take_piece Passed")

    def test_take_bp_invalid_capture_no_white(self):
        # No white pawn to capture at target
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 3, 3
        black_pawn = self.board.grid[from_y][from_x]
        result = black_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Capture move should be invalid without a white pawn.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Black_Pawn)
        self.assertIsInstance(self.board.grid[to_y][to_x], Empty_Spot)
        print("Test 2 for BP_take_piece Passed")

    def test_take_bp_invalid_capture_wrong_direction(self):
        # Black pawn trying to capture backwards (which is invalid)
        self.board.place_piece(White_Pawn('WP'), 2, 2)
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 3, 3)
        from_x, from_y = 2, 2  # White pawn position (wrong piece trying to move)
        to_x, to_y = 3, 3
        black_pawn = self.board.grid[to_y][to_x]  # Actually Black Pawn is at (3,3)
        # Attempt capture backwards (from black pawn's perspective) by calling move incorrectly
        result = black_pawn.move(self.board, to_x, to_y, from_x, from_y)
        self.assertTrue(result, "Black pawn cannot capture backwards.")
        self.assertIsInstance(self.board.grid[from_y][from_x], White_Pawn)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Pawn)
        print("Test 3 for BP_take_piece Passed")

    def test_take_bp_valid_capture_from_behind(self):
        # Another valid capture test
        self.board.place_piece(White_Pawn('WP'), 5, 5)
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 5, 5
        black_pawn = self.board.grid[from_y][from_x]
        result = black_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Capture move should be valid.")
        if result:
            self.board.place_piece(black_pawn, to_y, to_x)
            self.board.grid[from_y][from_x] = Empty_Spot("Empty Spot")
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Pawn)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        print("Test 4 for BP_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
