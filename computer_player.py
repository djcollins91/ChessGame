from player import Player


class Computer_Player(Player):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def turn(self):
        pass