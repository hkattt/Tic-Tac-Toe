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
            # Checks if the input was valid
            if decision != "Y" and decision != "y":
                raise InputError
            # multiplayer 
            if decision == "Y" or decision == "y":
                self.crosses = Player(self)
                self.noughts = Player(self, False, True)
            self.run()
        # invalid input
        except InputError:
            print("Make sure you enter the correct value!! (Y / N)")
            print("")
            self.new()
    
    def run(self):
        # creates a game loop (this runs inside the main loop)
        self.playing = True
        self.draw()
        while self.playing:
            # crosses move
            previous_x, previous_y = self.crosses.move()
            self.draw()
            # checks if crosses won
            if self.game_over(previous_x, previous_y):
                self.victory("X")
                self.playing = False
                break
            # noughts move
            previous_x, previous_y = self.noughts.move()
            self.draw()
            # checks if noughts won
            if self.game_over(previous_x, previous_y):
                self.victory("X")
                self.playing = False
                break
                 
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
        # Horizontal direction
        if self.board[0][Y] in self.player_symbols and self.board[0][Y] == self.board[1][Y] == self.board[2][Y]:
            return True
        # Vertical direction
        elif self.board[X][0] in self.player_symbols and self.board[X][0] == self.board[X][1] == self.board[X][2]:
            return True
        # Diagonal 1
        elif self.board[0][0] in self.player_symbols and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        # Diagonal 2
        elif self.board[0][2] in self.player_symbols and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def victory(self, winner):
        """ Victroy message """
        print("")
        print(winner + "'s WON!!")
        print("")

    def end_game(self):
        """ Displayed after a game is finished """
        print("")
        try: 
            decision = input("Do you want to play again? (Y / N) ")
            # Checks if the input was valid
            if decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                raise InputError
            # Do not want to play again
            if decision == "N" or decision == "n":
                self.running = False
                print("THANKS FOR PLAYING!!")
                print("")
        # invalid input 
        except InputError:
            print("Make sure you enter the correct value!! (Y / N)")
            print("")
            self.end_game()

    def reset(self):
        """ Resets the game attributes """
        self.board = self.board = [["   " for i in range(3)], ["   " for i in range(3)], ["   " for i in range(3)]]

# creates game object (the board)
game = Board()
# main loop
while game.running:
    game.new()
    game.end_game()
    game.reset()