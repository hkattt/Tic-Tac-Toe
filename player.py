# Player class file

from errors import *

class Player():
    """ Player (user) class """
    def __init__(self, game, cross=True, nought=False):
        self.cross = cross
        self.nought = nought
        self.game = game
        # determines what symbol the player is using
        if self.cross:
            self.type = "X"
        else:
            self.type = "O"

    def move(self):
        """ Places a nought or cross on the board """
        try: 
            X, Y = input("Select a position to place an {} (X, Y): ".format(self.type)).strip().split(" ")
            X, Y = int(X) - 1, int(Y) - 1
            # Checks if the given input is a legal move
            if self.valid_move(X, Y):
                self.game.board[X][Y] = " " + "{}".format(self.type) + " "
            else:
                raise InvalidMoveError
        # Input value is too large
        except IndexError:
            print("Your input must be between 1 and 3!!")
            print("")
            self.move()
        # Move is illegal
        except InvalidMoveError:
            print("You cannot place a {} on a taken square!!".format(self.type))
            print("")
            self.move()
        return X, Y

    def valid_move(self, X, Y):
        """ Checks if the chosen move is legal """
        if self.game.board[X][Y] == "   ":
            return True
        return False