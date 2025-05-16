import unittest
from board import Board
from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.empty.empty import Empty_Spot

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        # Place black pawns on row 6 (y=6)
        for col in range(8):
            board.place_piece(Black_Pawn("BP"), col, 6)

    def move_and_check(self, from_x, from_y, to_x, to_y):
        pawn = self.board.grid[from_y][from_x]
        self.assertIsInstance(pawn, Black_Pawn, f"Expected a Black_Pawn at ({from_x}, {from_y})")
        self.assertIsInstance(self.board.grid[to_y][to_x], Empty_Spot, f"Target ({to_x}, {to_y}) should be empty")

        can_move = pawn.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(can_move, f"Move from ({from_x}, {from_y}) to ({to_x}, {to_y}) should be valid")

        if can_move:
            self.board.place_piece(pawn, to_x, to_y)
            self.board.place_piece(Empty_Spot("Empty Spot"), from_x, from_y)

        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Start square should be empty after move")
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Pawn, "Target square should have Black_Pawn")
        self.assertEqual(str(self.board.grid[to_y][to_x]), "BP")

    def test_move_forward_1_square(self):
        self.move_and_check(from_x=6, from_y=6, to_x=6, to_y=5)

    def test_move_forward_2_squares_from_start(self):
        self.move_and_check(from_x=0, from_y=6, to_x=0, to_y=4)

    def test_second_move_forward_1_square(self):
        self.board.grid[4][6] = Black_Pawn("BP")  # Setup manually for test
        self.board.grid[5][6] = Empty_Spot("Empty Spot")
        self.move_and_check(from_x=6, from_y=4, to_x=6, to_y=3)

    def test_another_forward_move(self):
        self.board.grid[4][4] = Black_Pawn("BP")
        self.board.grid[5][4] = Empty_Spot("Empty Spot")
        self.move_and_check(from_x=4, from_y=4, to_x=4, to_y=3)

    def test_invalid_move_over_piece(self):
        # Try moving a pawn forward where another piece blocks it
        pawn = self.board.grid[6][6]
        blocked = not pawn.move(self.board, 6, 6, 6, 5)  # There's already a pawn at (6, 5)
        self.assertFalse(blocked, "Should not be able to move into a square occupied by another pawn")

if __name__ == "__main__":
    unittest.main()