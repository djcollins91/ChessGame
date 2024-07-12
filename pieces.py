class Pawn:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    STARTING_PIECES = 8
    taken_pieces = 0

    @staticmethod
    def taken_piece():
        Pawn.taken_pieces += 1

    @staticmethod
    def getRemaining_pieces():
        return Pawn.STARTING_PIECES - Pawn.taken_pieces
