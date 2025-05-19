import unittest
from Pieces.knights.white.white_knight import White_Knight
from board import Board
from place_pieces import place_white_knight

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_white_knight(board)
        
    def test_valid_move_forward(self):
        from Pieces.empty.empty import Empty_Spot
        # Test 7: Testing if piece can move 2 to the left and up
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 1, 4
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 7 for WN_move passed")

        # Test 8: Testing if piece can move 2 to the left and down
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 3, 4
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 8 for WN_move passed")


if __name__ == '__main__':
    unittest.main()