import unittest
from board import Board
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.empty.empty import Empty_Spot

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        # Place white pawns on row 1 (y=1)
        for col in range(8):
            board.place_piece(White_Pawn("WP"), col, 1)

    def move_and_check(self, from_x, from_y, to_x, to_y):
        pawn = self.board.grid[from_y][from_x]
        self.assertIsInstance(pawn, White_Pawn, f"Expected a White_Pawn at ({from_x}, {from_y})")
        self.assertIsInstance(self.board.grid[to_y][to_x], Empty_Spot, f"Target ({to_x}, {to_y}) should be empty")

        can_move = pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(can_move, f"Move from ({from_x}, {from_y}) to ({to_x}, {to_y}) should be valid")

        if can_move:
            self.board.place_piece(pawn, to_x, to_y)
            self.board.place_piece(Empty_Spot("Empty Spot"), from_x, from_y)

        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Start square should be empty after move")
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Pawn, "Target square should have White_Pawn")
        self.assertEqual(str(self.board.grid[to_y][to_x]), "WP")

    def test_move_forward_1_square(self):
        self.move_and_check(from_x=1, from_y=1, to_x=1, to_y=2)

    def test_move_forward_2_squares_from_start(self):
        self.move_and_check(from_x=0, from_y=1, to_x=0, to_y=3)

    def test_second_move_forward_1_square(self):
        self.board.grid[2][2] = White_Pawn("WP")  # manually place on 2,2
        self.board.grid[3][2] = Empty_Spot("Empty Spot")
        self.move_and_check(from_x=2, from_y=2, to_x=2, to_y=3)

    def test_another_forward_move(self):
        self.board.grid[4][4] = White_Pawn("WP")  # manually place WP at 4,4
        self.board.grid[5][4] = Empty_Spot("Empty Spot")
        self.move_and_check(from_x=4, from_y=4, to_x=4, to_y=5)

    def test_invalid_move_over_piece(self):
        # Try moving a pawn forward into a square occupied by another piece
        pawn = self.board.grid[1][6]
        self.assertTrue(
            pawn.move(self.board, 6, 1, 6, 2),
            "Should not be able to move into a square occupied by another pawn"
        )

if __name__ == "__main__":
    unittest.main()
