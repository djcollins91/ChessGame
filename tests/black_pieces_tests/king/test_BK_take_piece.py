import unittest
from board import Board
from pieces.kings.white.white_king import White_King
from pieces.kings.black.black_king import Black_King
from place_pieces import place_black_king

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_black_king(board)
        
    def test_take_BK(self):
        from pieces.empty.empty import Empty_Spot
        # Test 1: Valid capture of White_King by Black_King (one square)
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 1, 1)
        self.board.place_piece(White_King(White_King.get_piece_str()), 2, 2)
        from_x, from_y = 1, 1
        to_x, to_y = 2, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 1 for BK_take_piece Passed")

        # Test 2: Valid capture (one square)
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 2, 2)
        self.board.place_piece(White_King(White_King.get_piece_str()), 1, 1)
        from_x, from_y = 2, 2
        to_x, to_y = 1, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 2 for BK_take_piece Passed")

        # Test 3: Invalid capture (no piece at target)
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 3
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Black_King)
        self.assertTrue(isinstance(self.board.grid[to_y][to_x], Empty_Spot) or self.board.grid[to_y][to_x] is None)
        self.assertEqual(str(self.board.grid[from_y][from_x]), Black_King.get_piece_str())
        print("Test 3 for BK_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
