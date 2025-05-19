import unittest
from Pieces.knights.white.white_knight import White_Knight
from Pieces.empty.empty import Empty_Spot
from board import Board
from place_pieces import place_white_knight


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_white_knight(board)
        
    def test_valid_move_forward(self):
        # Test 1: testing moving up and to the right
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 1, 4)
        from_x, from_y = 1, 4
        to_x, to_y = 2, 6
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 1 for WN_move passed")

        # Test 2: testing moving up and to the left
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 1, 1)
        from_x, from_y = 1, 1
        to_x, to_y = 0, 3
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 2 for WN_move passed")

        # Test 3: Testing if piece can move down and to the right
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 2, 3)
        from_x, from_y = 2, 3
        to_x, to_y = 3, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 3 for WN_move passed")

        # Test 4: Testing if piece can move down and to the left
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 5, 5)
        from_x, from_y = 5, 5
        to_x, to_y = 4, 3
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 4 for WN_move passed")

        # Test 5: Testing if piece can move 2 to the right and up
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 6, 5
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 5 for WN_move passed")

        # Test 6:Testing if piece can move 2 to the right and down
        self.board.place_piece(White_Knight(White_Knight.get_piece_str()), 3, 3)
        from_x, from_y = 3, 3
        to_x, to_y = 5, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, White_Knight)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertIsInstance(self.board.grid[to_y][to_x], White_Knight)
        self.assertEqual(str(self.board.grid[to_y][to_x]), White_Knight.get_piece_str())
        print("Test 6 for WN_move passed")


if __name__ == '__main__':
    unittest.main()
