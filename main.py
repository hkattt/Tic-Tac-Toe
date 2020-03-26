# Tic Tac Toe Main File (Run to play)

from player import *

class Board():
    """ Main board / game class """
    def __init__(self):
        self.running = True
        self.board = ["   " for i in range(9)]

    def new(self):
        """ Creates a new game """
        decision = input("Do you want to play with a friend? (Y / N) ") # single player or multiplayer
        print("")
        # multiplayer 
        if decision == "Y" or decision == "y":
            self.crosses = Player(self)
            self.noughts = Player(self, False, True)
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.crosses.move()
            self.draw()
            self.noughts.move()
            self.draw()

    def draw(self):
        """ Updates the board """
        print("   |   |   ")
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])
        print("   |   |   ")


b = Board()
while b.running:
    b.new()