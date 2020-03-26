# Tic Tac Toe Main File (Run to play)

from player import *

class Board():
    """ Main board / game class """
    def __init__(self):
        self.running = True
        self.board = [["   " for i in range(3)], ["   " for i in range(3)], ["   " for i in range(3)]]
        self.player_symbols = [" X ", " Y "]

    def new(self):
        """ Creates a new game """
        try:
            decision = input("Do you want to play with a friend? (Y / N) ") # single player or multiplayer
            print("")
            if decision != "Y" and decision != "Y":
                raise InputError
            # multiplayer 
            if decision == "Y" or decision == "y":
                self.crosses = Player(self)
                self.noughts = Player(self, False, True)
            self.run()
        except InputError:
            print("Make sure you enter the correct value!! (Y / N)")
            print("")
            self.new()
    
    def run(self):
        self.playing = True
        while self.playing:
            previous_x, previous_y = self.crosses.move()
            self.draw()
            if self.game_over(previous_x, previous_y):
                self.victory("X")
                self.playing = False
                break
            previous_x, previous_y = self.noughts.move()
            if self.game_over(previous_x, previous_y):
                self.victory("X")
                self.playing = False
                break
            self.draw()
        
    def draw(self):
        """ Updates the board """
        print("   |   |   ")
        print(self.board[0][0] + "|" + self.board[1][0] + "|" + self.board[2][0])
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(self.board[0][1] + "|" + self.board[1][1] + "|" + self.board[2][1])
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(self.board[0][2] + "|" + self.board[1][2] + "|" + self.board[2][2])
        print("   |   |   ")

    def game_over(self, X, Y):
        """ Checks if the game was won by either player """
        if (self.board[0][Y] in self.player_symbols) and self.board[0][Y] == self.board[1][Y] == self.board[2][Y]:
            return True
        elif self.board[X][0] in self.player_symbols and self.board[X][0] == self.board[X][1] == self.board[X][2]:
            return True
        return False

    def victory(self, winner):
        """ Victroy message """
        print("")
        print(winner + "'s WON!!")
        print("")
        
b = Board()
while b.running:
    b.new()