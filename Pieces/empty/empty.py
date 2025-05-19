from piece import Piece

class Empty_Spot(Piece):
    _empty_spot_str = "Empty Spot"
    def __init__(self, name="Empty Spot"):
        super().__init__(name)

    def __str__(self):
        return "Empty Spot"
    @staticmethod
    def get_str():
        return Empty_Spot._empty_spot_str
