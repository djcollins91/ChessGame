import unittest
from board import Board
from helper import rooks, board_width
from Pieces.rooks.white.white_rook import White_Rook


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        rooks(board, board_width)

    def test_valid_move_forward(self):
        # Test 7: Makes sure you can't move when piece is in the way
        from_x, from_y = 0, 0
        self.board.place_piece(White_Rook('WR'), 0, 1)
        to_x, to_y = 0, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 7 for WR_move passed")

         # Test 8: Makes sure you can't move when piece is in the way
        from_x, from_y = 7, 0
        self.board.place_piece(White_Rook('WR'), 5, 0)
        to_x, to_y = 4, 0
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 8 for WR_move passed")

if __name__ == '__main__':
    unittest.main()