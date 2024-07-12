class Pawn:
    STARTING_PIECES = 8
    taken_pieces_count = 0


    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


    @staticmethod
    def taken_piece():
        Pawn.taken_pieces_count += 1

    @staticmethod
    def getRemainingPieces():
        return Pawn.STARTING_PIECES - Pawn.taken_pieces_count
