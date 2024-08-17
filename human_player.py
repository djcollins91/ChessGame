from player import Player


class Human_Player(Player):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def turn(self):
        pass