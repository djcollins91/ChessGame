import unittest
from Pieces.knights.black.black_knight import Black_Knight
from Pieces.knights.white.white_knight import White_Knight
from board import Board
from helper import knights, board_width



class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        knights(board, board_width)
        print(board)

    def test_take_BN(self):
        # Test 1: Valid capture of Black_Knight by White_Knight
        self.board.place_piece(White_Knight('WN'), 1, 1)
        self.board.place_piece(Black_Knight('BN'), 2, 3)
        
        from_x, from_y = 1, 1
        to_x, to_y = 2, 3
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Knight after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the White_Knight.")
        print("Test 1 for WN_take_piece Passed")

        # Test 2: Invalid capture (not diagonal)
        self.board.place_piece(White_Knight('WN'), 3, 1)
        self.board.place_piece(Black_Knight('BN'), 5, 2)
        
        from_x, from_y = 3, 1
        to_x, to_y = 5, 2
        result = self.board.grid[from_y][from_x].take_piece(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the White_Knight after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WN', "Target position should have the White_Knight.")
        print("Test 2 for WN_take_piece Passed")
        

if __name__ == '__main__':
    unittest.main()
