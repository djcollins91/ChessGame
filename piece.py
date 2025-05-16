class Piece:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def valid_move(piece, board, from_x, from_y, to_x, to_y):
        return True

    @staticmethod
    def invalid_move():
        return False
