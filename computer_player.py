from player import Player


class Computer_Player(Player):
    def __init__(self, name, board):  # Accept both name and board as arguments
        self.name = name
        self.board = board  # Initialize the board
        # Any other attributes related to the computer player

    def __str__(self):
        return self.name
    
    def turn(self):
       pass