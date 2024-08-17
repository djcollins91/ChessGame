class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def turn(self):
        raise NotImplementedError("This method should be overridden by subclasses")