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
        
    def remove_piece(self, x, y):
        if 0 <= x < self.WIDTH and 0 <= y < self.LENGTH:
            self.grid[y][x] = None
        else:
            raise ValueError("Position out of bounds")

    def __str__(self):
        board_str = ""
        for row in self.grid:
            board_str += " ".join([str(cell) if cell else '.' for cell in row]) + "\n"
        return board_str
