import unittest
from board import Board
from pieces.pawns.black.black_pawn import Black_Pawn
from pieces.pawns.white.white_pawn import White_Pawn
from pieces.empty.empty import Empty_Spot

class TestWhitePawnCapture(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_wp_valid_diagonal_capture_left(self):
        """White pawn captures black pawn diagonally to the left"""
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 3, 3)  # Target
        self.board.place_piece(White_Pawn(White_Pawn.get_piece_str()), 4, 4)  # Attacker

        from_x, from_y = 4, 4
        to_x, to_y = 3, 3
        white_pawn = self.board.grid[from_y][from_x]

        result = white_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "White pawn should capture diagonally left.")

        if result:
            self.board.place_piece(white_pawn, to_x, to_y)
            self.board.grid[from_y][from_x] = Empty_Spot("Empty Spot")

        self.assertIsInstance(self.board.grid[to_y][to_x], White_Pawn)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        print("Test 1 for WP_valid_diagonal_capture_left Passed")

    def test_wp_valid_diagonal_capture_right(self):
        """White pawn captures black pawn diagonally to the right"""
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 5, 3)
        self.board.place_piece(White_Pawn(White_Pawn.get_piece_str()), 4, 4)

        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        white_pawn = self.board.grid[from_y][from_x]

        result = white_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "White pawn should capture diagonally right.")

        if result:
            self.board.place_piece(white_pawn, to_x, to_y)
            self.board.grid[from_y][from_x] = Empty_Spot("Empty Spot")

        self.assertIsInstance(self.board.grid[to_y][to_x], White_Pawn)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        print("Test 2 for WP_valid_diagonal_capture_right Passed")

    def test_wp_invalid_capture_empty(self):
        """White pawn tries to capture on empty square (invalid)"""
        self.board.place_piece(White_Pawn(White_Pawn.get_piece_str()), 4, 4)

        from_x, from_y = 4, 4
        to_x, to_y = 3, 3  # Empty
        white_pawn = self.board.grid[from_y][from_x]

        result = white_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Capture should fail when square is empty.")

        self.assertIsInstance(self.board.grid[from_y][from_x], White_Pawn)
        self.assertIsInstance(self.board.grid[to_y][to_x], Empty_Spot)
        print("Test 3 for WP_invalid_capture_empty Passed")

    def test_wp_invalid_capture_backward(self):
        """White pawn attempts to capture backward (invalid)"""
        self.board.place_piece(Black_Pawn(Black_Pawn.get_piece_str()), 5, 5)
        self.board.place_piece(White_Pawn(White_Pawn.get_piece_str()), 4, 4)

        from_x, from_y = 4, 4
        to_x, to_y = 5, 5  # Backward from White's perspective
        white_pawn = self.board.grid[from_y][from_x]

        result = white_pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "White pawn should not capture backward.")

        self.assertIsInstance(self.board.grid[from_y][from_x], White_Pawn)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Pawn)
        print("Test 4 for WP_invalid_capture_backward Passed")



if __name__ == '__main__':
    unittest.main()
