# Player class file

from errors import *

class Player():
    """ Player (user) class """
    def __init__(self, game, cross=True, nought=False):
        self.game = game
        self.cross = cross
        self.nought = nought
        # determines what symbol the player is using
        if self.cross:
            self.type = "X"
        else:
            self.type = "O"

    def move(self):
        """ Places a nought or cross on the board """
        try:
            self.game.app.write("Select a position to place an {} (X, Y): ".format(self.type))
            self.game.app.wait_variable(self.game.app.inputVariable)
            X, Y = self.game.app.inputVariable.get().strip().split()
            X, Y = int(X) - 1, int(Y) - 1
            # Checks if the given input is a legal move
            if self.valid_move(X, Y):
                self.game.board[X][Y] = " " + "{}".format(self.type) + " "
            else:
                raise InvalidMoveError
        # Input value is too large
        except IndexError:
            self.game.app.write("Your input must be between 1 and 3!!")
            self.game.app.write("")
            self.move()
        # Move is illegal
        except InvalidMoveError:
            self.game.app.write("You cannot place a {} on a taken square!!".format(self.type))
            self.game.app.write("")
            self.move()
        return X, Y

    def valid_move(self, X, Y):
        """ Checks if the chosen move is legal """
        if self.game.board[X][Y] == "   ":
            return True
        return False