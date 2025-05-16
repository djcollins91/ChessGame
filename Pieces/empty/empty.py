from piece import Piece

class Empty_Spot(Piece):
    def __init__(self, name="Empty Spot"):
        super().__init__(name)

    def __str__(self):
        return "Empty Spot"
