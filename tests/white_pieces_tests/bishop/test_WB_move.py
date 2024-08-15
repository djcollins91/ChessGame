import unittest
from Pieces.bishops.white.white_bishop import White_Bishop
from board import Board
from helper import  bishops, board_width


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.initialize_pieces(self.board)

    def initialize_pieces(self, board):
        bishops(board, board_width)
        
    def test_valid_move_forward(self):
        #Test 1: testing moving up
        self.board.place_piece(White_Bishop('WB'), 1, 3)
        from_x, from_y = 1, 3
        to_x, to_y = 2,4
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WB', "Target position should have the white Piece.")
        print("Test 1 for WB_move passed")

        # Test 2: Testing if can move right
        self.board.place_piece(White_Bishop('WB'), 0, 1)
        from_x, from_y = 0, 1
        to_x, to_y = 1, 0
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WB', "Target position should have the white Piece.")
        print("Test 2 for WB_move passed")

        # Test 3: Testing if piece can move diagonal
        self.board.place_piece(White_Bishop('WB'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 7, 7
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Valid move", "Move should be identified as valid.")
        self.assertIsNone(self.board.grid[from_y][from_x], "Original position should be empty after the move.")
        self.assertIsNotNone(self.board.grid[to_y][to_x], "Target position should have the Piece after the move.")
        self.assertEqual(str(self.board.grid[to_y][to_x]), 'WB', "Target position should have the white Piece.")
        print("Test 3 for WB_move passed")

        #Test 4: Move Piece to an occupied spot (invalid move)
        self.board.place_piece(White_Bishop('WB'), 3, 3)
        self.board.place_piece(White_Bishop('WB'), 4, 4)  # Place another white Piece in front
        from_x, from_y = 3, 3
        to_x, to_y = 5, 5  # Invalid move as the spot is occupied
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 4 for WB_move passed")


        # Test 5: Testing to see the piece can't move to the side
        self.board.place_piece(White_Bishop('WB'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 2, 4
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 5 for WB_move passed")
        
        # Test 6: Testing to see the piece can't move forward
        self.board.place_piece(White_Bishop('WB'), 2, 2)
        from_x, from_y = 2, 2
        to_x, to_y = 3, 2
        result = self.board.grid[from_y][from_x].move(self.board, from_x, from_y, to_x, to_y)
        self.assertEqual(result, "Invalid move", "Move should be identified as invalid.")
        print("Test 6 for WB_move passed")



if __name__ == '__main__':
    unittest.main()
