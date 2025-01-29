from piece import Piece

class Empty_Spot(Piece):
     def __init__(self, name):
        self.name = name

     def __str__(self):
        return self.name
     _piece_str = "E"

     def get_piece_str():
      return Empty_Spot._piece_str