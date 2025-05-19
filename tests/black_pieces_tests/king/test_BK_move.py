import unittest
from Pieces.kings.black.black_king import Black_King
from Pieces.empty.empty import Empty_Spot
from board import Board
from place_pieces import place_black_king



class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        place_black_king(board)
        
    def test_valid_move_forward(self):
        # Test 1: testing moving up
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 1, 4)
        from_x, from_y = 1, 4
        to_x, to_y = 2, 4
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 1 for BK_move passed")

        # Test 2: Testing if can move right
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 0, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 2 for BK_move passed")

        # Test 3: Testing if piece can move left
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 2, 1
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 3 for BK_move passed")

        # Test 4: Testing if piece can move backwards
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 6, 6)
        from_x, from_y = 6, 6
        to_x, to_y = 6, 5
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 4 for BK_move passed")

        # Test 5: Testing to see piece can move diagonal
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 4, 4)
        from_x, from_y = 4, 4
        to_x, to_y = 5, 5
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertTrue(result, "Move should be identified as valid.")
        self.board.place_piece(piece, to_x, to_y)
        self.board.place_piece(Empty_Spot(Empty_Spot.get_str()), from_x, from_y)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertIsInstance(self.board.grid[from_y][from_x], Empty_Spot)
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 5 for BK_move passed")

        # Test 6: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 3, 3)
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 3, 2)
        from_x, from_y = 3, 3
        to_x, to_y = 3, 2
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        self.assertIsInstance(self.board.grid[from_y][from_x], Black_King)
        self.assertIsInstance(self.board.grid[to_y][to_x], Black_King)
        self.assertEqual(str(self.board.grid[from_y][from_x]), Black_King.get_piece_str())
        self.assertEqual(str(self.board.grid[to_y][to_x]), Black_King.get_piece_str())
        print("Test 6 for BK_move passed")

        # Test 7: Testing if piece can't move two spot
        self.board.place_piece(Black_King(Black_King.get_piece_str()), 1, 5)
        from_x, from_y = 1, 5
        to_x, to_y = 1, 7
        piece = self.board.grid[from_y][from_x]
        self.assertIsInstance(piece, Black_King)
        result = piece.move(self.board, from_x, from_y, to_x, to_y)
        self.assertFalse(result, "Move should be identified as invalid.")
        print("Test 7 for BK_move passed")

if __name__ == '__main__':
    unittest.main()
