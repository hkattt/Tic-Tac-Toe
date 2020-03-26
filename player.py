# Player class file

from errors import *

class Player():
    """ Player (user) class """
    def __init__(self, game, cross=True, nought=False):
        self.cross = cross
        self.nought = nought
        self.game = game
        if self.cross:
            self.type = "X"
        else:
            self.type = "O"

    def move(self):
        """ Places a nought or cross on the board """
        try: 
            X, Y = input("Select a position to place an {} (X, Y): ".format(self.type)).split(" ")
            X, Y = int(X) - 1, int(Y) - 1
            if self.valid_move(X, Y):
                self.game.board[X][Y] = " " + "{}".format(self.type) + " "
            else:
                raise InvalidMoveError
        except IndexError:
            print("Your input must be between 1 and 9!!")
            print("")
            self.move()
        except Invalid_Move:
            print("You cannot place a {} on a taken square!!".format(self.type))
            print("")
            self.move()
        return X, Y

    def valid_move(self, X, Y):
        """ Checks if the chosen move is legal """
        if self.game.board[X][Y] == "   ":
            return True
        return False