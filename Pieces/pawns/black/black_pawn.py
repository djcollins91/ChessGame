
from piece import Piece


class Black_Pawn(Piece):
    STARTING_PIECES = 8
    taken_pieces = 0
    _piece_str = "BP"
    _target_str = "W"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def get_piece_str(self):
        return Black_Pawn._piece_str

    def get_target_str(self):
        return Black_Pawn._target_str

    def move(self, board, from_col, from_row, to_col, to_row):
        print(f"Black_Pawn.move called with from ({from_col},{from_row}) to ({to_col},{to_row})")

        # Check straight move forward by 1
        if to_col == from_col and to_row == from_row - 1:
            if str(board.grid[to_row][to_col]).startswith("E"):
                print("Valid 1-step forward")
                return Piece.valid_move(self, board, from_col, from_row, to_col, to_row)

        # Check 2-square move forward from start
        if from_row == 6 and to_col == from_col and to_row == 4:
            if (str(board.grid[5][to_col]).startswith("E") and
                str(board.grid[4][to_col]).startswith("E")):
                print("Valid 2-step forward from start")
                return Piece.valid_move(self, board, from_col, from_row, to_col, to_row)

        print("Invalid black pawn move")
        return Piece.invalid_move()

    def take_piece(self, board, from_x, from_y, to_x, to_y):
        target = board.grid[to_y][to_x]
        if str(self) == Black_Pawn._piece_str:
            if abs(from_x - to_x) == 1 and from_y - to_y == 1:
                if target and str(target).startswith(Black_Pawn._target_str):
                    return Piece.valid_move(self, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()
