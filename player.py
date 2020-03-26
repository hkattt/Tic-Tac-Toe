# Player class file

class Player():
    def __init__(self, game, cross=True, nought=False):
        self.cross = cross
        self.nought = nought
        self.game = game
        if self.cross:
            self.type = "X"
        else:
            self.type = "O"

    def move(self):
        try: 
            position = int(input("Select a position to place an {} (0-9): ".format(self.type)))
            self.game.board[position] = " " + "{}".format(self.type) + " "
        except IndexError:
            print("Your input must be between 0 and 9!!")
            print("")
            self.move()