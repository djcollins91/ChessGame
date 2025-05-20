import unittest
from board import Board
from pieces.rooks.white.white_rook import White_Rook
from place_pieces import place_white_rook


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_white_rook(board)

    def test_valid_move_forward(self):
        # Test 7: Makes sure you can't move when piece is in the way
        from_x, from_y = 0, 0
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 0, 1)
        to_x, to_y = 0, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        print("Test 7 for WR_move passed")

        # Test 8: Makes sure you can't move when piece is in the way
        from_x, from_y = 7, 0
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 5, 0)
        to_x, to_y = 4, 0
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a White_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        print("Test 8 for WR_move passed")

if __name__ == '__main__':
    unittest.main()