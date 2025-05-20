import unittest
from board import Board
from pieces.rooks.white.white_rook import White_Rook
from pieces.rooks.black.black_rook import Black_Rook
from pieces.empty.empty import Empty_Spot
from place_pieces import place_white_rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_white_rook(board)

    def test_take_BR(self):
        # Test 1: Move Black_Rook testing if it can take White_Rook
        self.board.place_piece(Black_Rook(Black_Rook.get_piece_str()), 1, 1)
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 2, 1)
        from_x, from_y = 2, 1
        to_x, to_y = 1, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a Black_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "White Rook should be able to take White Rook.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Black Rook after capture.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        print("Test 1 for WR_take_piece Passed")

        # Test 2: Move Black_Rook to an empty space (valid move)
        self.board.place_piece(Black_Rook(Black_Rook.get_piece_str()), 3, 1)
        self.board.place_piece(White_Rook(White_Rook.get_piece_str()), 3, 7)
        from_x, from_y = 3, 7
        to_x, to_y = 3, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a Black_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Rook, "Target position should have the Black Rook after move.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot, "Original position should be empty after the move.")
        print("Test 2 for WR_take_piece Passed")

        # Test 3: Make sure you can't take piece when one of your pieces is in the way
        self.board.place_piece(White_Rook(Black_Rook.get_piece_str()), 4, 4)
        self.board.place_piece(White_Rook(Black_Rook.get_piece_str()), 4, 2)
        self.board.place_piece(Black_Rook(White_Rook.get_piece_str()), 4, 1)
        from_x, from_y = 4, 4
        to_x, to_y = 4, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Rook, "Should be a Black_Rook at the starting position.")
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], White_Rook, "Original position should still have the Black Rook.")
        print("Test 3 for WR_take_piece Passed")

if __name__ == '__main__':
    unittest.main()
