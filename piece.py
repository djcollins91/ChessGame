class Piece:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    
    def taken_piece():
        Piece.taken_pieces += 1

   
    def get_remaining_pieces():
        return Piece.STARTING_PIECES - Piece.taken_pieces


    def move(self, board, from_x, from_y, to_x, to_y):
        raise NotImplementedError("This method should be overridden by subclasses")

    def take_piece(self, board, from_x, from_y, to_x, to_y):
        raise NotImplementedError("This method should be overridden by subclasses")

