from player import Player


class Human_Player(Player):
    def __init__(self, name, board):  # Accept both name and board as arguments
        self.name = name
        self.board = board  # Initialize the board
        self.selected_piece = None
        self.selected_position = None

    def __str__(self):
        return self.name
    
    def turn(self, row, col):  # Assuming 'row' and 'col' will be passed when making a move
        pass
