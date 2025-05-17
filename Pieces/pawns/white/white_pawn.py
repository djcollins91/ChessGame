from Pieces.empty.empty import Empty_Spot
from piece import Piece

class White_Pawn(Piece):
    STARTING_PIECES = 8
    taken_pieces = 0
    _starting_row = 1

    def __init__(self, name):
        super().__init__(name)

    _piece_str = "WP"
    _target_str = "B"
    @staticmethod
    def get_piece_str():
        return White_Pawn._piece_str

    def get_target_str(self):
        return White_Pawn._target_str
    @staticmethod
    def get_starting_row():
        return White_Pawn._starting_row

    def move(self, board, from_x, from_y, to_x, to_y):
        print(f"White_Pawn.move called with from ({from_x},{from_y}) to ({to_x},{to_y})")

        # Move forward by 1 square
        if from_x == to_x and to_y == from_y + 1:
            if isinstance(board.grid[to_y][to_x], Empty_Spot):
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        # Move forward by 2 squares from starting row (y == 1)
        if from_x == to_x and from_y == 1 and to_y == 3:
            if isinstance(board.grid[2][to_x], Empty_Spot) and isinstance(board.grid[3][to_x], Empty_Spot):
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        # Try capture
        return self.take_piece(board, from_x, from_y, to_x, to_y)

    def take_piece(self, board, from_x, from_y, to_x, to_y):
        dx = abs(to_x - from_x)
        dy = to_y - from_y
        target = board.grid[to_y][to_x]

        print(f"take_piece called: from ({from_x},{from_y}) to ({to_x},{to_y}) dx={dx}, dy={dy}, target={target}")

        # White captures diagonally forward (upward) → dy == -1 and dx == 1
        if dx == 1 and dy == -1:
            if not isinstance(target, Empty_Spot) and str(target).startswith("B"):
                print("Valid capture")
                return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)

        print("Invalid capture")
        return Piece.invalid_move()

