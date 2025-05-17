
from Pieces.empty.empty import Empty_Spot
from piece import Piece


class Black_Pawn(Piece):
    _piece_str = "BP"
    _target_str = "W"
    STARTING_PIECES = 8
    taken_pieces = 0
    _starting_row = 6

    def __init__(self, name):
        super().__init__(name)
 
    def get_target_str():
        return Black_Pawn._target_str
    @staticmethod
    def get_piece_str():
        return Black_Pawn._piece_str
    
    @staticmethod
    def get_starting_row():
        return Black_Pawn._starting_row
    

    def move(self, board, from_x, from_y, to_x, to_y):
        # Normal forward move (one square forward: y decreases by 1)
        if from_x == to_x and to_y == from_y - 1:
            if isinstance(board.grid[to_y][to_x], Empty_Spot):
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        # Two squares forward from starting position
        if from_x == to_x and from_y == 6 and to_y == 4:
            if (isinstance(board.grid[5][to_x], Empty_Spot) and
                isinstance(board.grid[4][to_x], Empty_Spot)):
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        # Try capturing diagonally forward only
        return self.take_piece(board, from_x, from_y, to_x, to_y)

    def take_piece(self, board, from_x, from_y, to_x, to_y):
        dx = abs(to_x - from_x)
        dy = to_y - from_y
        target = board.grid[to_y][to_x]

        print(f"take_piece called: from ({from_x},{from_y}) to ({to_x},{to_y}) dx={dx}, dy={dy}, target={target}")

        # For black pawns, capture direction must be forward (dy == -1)
        if dx == 1 and dy == -1:
            if not isinstance(target, Empty_Spot) and str(target).startswith("W"):
                print("Valid capture")
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        print("Invalid capture")
        return Piece.invalid_move()

