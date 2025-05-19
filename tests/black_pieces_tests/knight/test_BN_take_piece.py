import unittest
from Pieces.knights.black.black_knight import Black_Knight
from Pieces.knights.white.white_knight import White_Knight
from board import Board
from place_pieces import place_black_knight


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_black_knight(board)
        
    def test_take_BN(self):
        from Pieces.empty.empty import Empty_Spot
        # Test 1: Valid capture of White_Knight by Black_Knight (L-shape)
        self.board.place_piece(Black_Knight(Black_Knight.get_piece_str()), 1, 1)
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 2, 3)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 3
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Knight)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_Knight.get_piece_str())
        print("Test 1 for BN_take_piece Passed")

        # Test 2: Valid capture (L-shape)
        self.board.place_piece(Black_Knight(Black_Knight.get_piece_str()), 3, 1)
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 5, 2)
        from_x, from_y = 3, 1
        to_x, to_y = 5, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_Knight)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_Knight.get_piece_str())
        print("Test 2 for BN_take_piece Passed")
        

if __name__ == '__main__':
    unittest.main()
