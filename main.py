# Tic Tac Toe Main File (Run to play)

from player import *

class Board():
    def __init__(self):
        self.board = ["   " for i in range(9)]

    def new(self):
        decision = input("Do you want to play with a friend? (Y / N) ")
        if decision == "Y" or decision == "y":
            self.crosses = Player()
            self.noughts = Player(False, True)
    
    def run(self):
        self.crosses.move()
        self.draw()
        self.noughts.move()
        self.draw()

    def draw(self):
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
b.new()
b.run()
