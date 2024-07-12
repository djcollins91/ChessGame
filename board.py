class Board:
    WIDTH = 8
    LENGTH = 8

    def __init__(self):
        # Initialize the board with None to indicate empty cells
        self.grid = [[None for _ in range(Board.WIDTH)] for _ in range(Board.LENGTH)]

    @staticmethod
    def getWIDTH():
        return Board.WIDTH

    @staticmethod
    def getLENGTH():
        return Board.LENGTH

    def place_piece(self, piece, x, y):
        if 0 <= x < self.WIDTH and 0 <= y < self.LENGTH:
            self.grid[y][x] = piece
        else:
            raise ValueError("Position out of bounds")

    def move_piece(self, from_x, from_y, to_x, to_y):
        if 0 <= to_x < self.WIDTH and 0 <= to_y < self.LENGTH:
            piece = self.grid[from_y][from_x]
            self.grid[from_y][from_x] = None
            self.grid[to_y][to_x] = piece
        else:
            raise ValueError("Move out of bounds")

    def highlight_moves(self, x, y):
        # Make a copy of the current grid to mark possible moves
        highlighted_grid = [row[:] for row in self.grid]

        # Define the possible moves for a white pawn
        possible_moves = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]

        for move in possible_moves:
            to_x, to_y = move
            if 0 <= to_x < self.WIDTH and 1 <= to_y < self.LENGTH:
                if self.grid[to_y][to_x] is None:  # Empty square
                    highlighted_grid[to_y][to_x] = '*'
                elif str(self.grid[to_y][to_x]).startswith('B'):  # Capturable piece
                    highlighted_grid[to_y][to_x] = '*'

        return highlighted_grid

    def __str__(self):
        board_str = ""
        for row in self.grid:
            board_str += " ".join([str(cell) if cell else '.' for cell in row]) + "\n"
        return board_str

    def print_highlighted_grid(self, highlighted_grid):
        board_str = ""
        for row in highlighted_grid:
            board_str += " ".join([str(cell) if cell else '.' for cell in row]) + "\n"
        print(board_str)
