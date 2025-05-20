class Piece:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def valid_move():
        return True

    @staticmethod
    def invalid_move():
        return False
