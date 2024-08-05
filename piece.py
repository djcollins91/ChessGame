class Piece:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def move(self, board, from_x, from_y, to_x, to_y):
        raise NotImplementedError("This method should be overridden by subclasses")

    def take_piece(self, board, from_x, from_y, to_x, to_y):
        raise NotImplementedError("This method should be overridden by subclasses")
