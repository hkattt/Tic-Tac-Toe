# Player class file

class Player():
    def __init__(self, cross=True, nought=False):
        self.cross = cross
        self.nought = nought
        if self.cross:
            self.type = "X"
        else:
            self.type = "O"

    def move(self):
        position = input("Select a position to place an {} (0-9): ".format(self.type))