from piece import Piece

class White_Pawn(Piece):
    STARTING_PIECES = 8
    taken_pieces = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    _piece_str = "WP"
    _target_str = "B"
    def get_piece_str(self):
        return White_Pawn._piece_str
    
    def get_target_str(self):
        return White_Pawn._target_str
    #how the piece move
    def move(self, board, from_col, from_row, to_col, to_row):
        print(f"White_Pawn.move called with from ({from_col},{from_row}) to ({to_col},{to_row})")

        # Check straight move forward by 1
        if to_col == from_col and to_row == from_row + 1:
            if str(board.grid[to_row][to_col]).startswith("E"):
                print("Valid 1-step forward")
                return True

        # Check 2-square move forward from start
        if from_row == 1 and to_col == from_col and to_row == 3:
            if (str(board.grid[3][to_col]).startswith("E") and
                str(board.grid[2][to_col]).startswith("E")):
                print("Valid 2-step forward from start")
                return True

        print("Invalid black pawn move")
        return False
    
   
    
    #how the piece can take a piece
    def take_piece(self, board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        if piece and str(piece) == White_Pawn._piece_str:
            # Ensure it's a diagonal move and there's a black piece to capture
            if (abs(from_x - to_x) == 1 and to_y - from_y == 1) and target and str(target).startswith(White_Pawn._target_str):
                return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()

    