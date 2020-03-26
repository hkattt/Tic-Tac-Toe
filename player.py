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
            position = int(input("Select a position to place an {} (1-9): ".format(self.type))) - 1
            if self.valid_move(position):
                self.game.board[position] = " " + "{}".format(self.type) + " "
            else:
                raise Invalid_Move
        except IndexError:
            print("Your input must be between 1 and 9!!")
            print("")
            self.move()
        except Invalid_Move:
            print("You cannot place a {} on a taken square!!".format(self.type))
            print("")
            self.move()

    def valid_move(self, position):
        """ Checks if the chosen move is legal """
        if self.game.board[position] == "   ":
            return True
        return False