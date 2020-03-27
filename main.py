# Tic Tac Toe Main File (Run to play)

# importing other files
from player import *
from gui import *
from computer_ai import *
import time

class Board():
    """ Main board / game class """
    def __init__(self):
        self.running = True
        self.board = [["   " for i in range(3)], ["   " for i in range(3)], ["   " for i in range(3)]]
        self.player_symbols = [" X ", " Y "]
        self.app = SimpleApp_tk(None)
        self.app.title("Tic Tac Toe")
        self.app.write("TIC TAC TOE")
        self.app.write("")

    def new(self):
        """ Creates a new game """
        try:
            self.app.write("Do you want to play with a friend? (Y / N) ")
            self.app.wait_variable(self.app.inputVariable)
            decision = self.app.inputVariable.get().strip() # single player or multiplayer
            self.app.write("")
            # Checks if the input was valid
            if decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                raise InputError
            # multiplayer 
            if decision == "Y" or decision == "y":
                self.crosses = Player(self)
                self.noughts = Player(self, False, True)
            else:
                self.crosses = Player(self)
                self.noughts = AI(self)
        # invalid input
        except InputError:
            self.app.write("Make sure you enter the correct value!! (Y / N)")
            self.app.write("")
            self.new()
        self.run()
    
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
        self.app.write("   |   |   ")
        self.app.write(self.board[0][0] + "|" + self.board[1][0] + "|" + self.board[2][0])
        self.app.write("   |   |   ")
        self.app.write("-----------")
        self.app.write("   |   |   ")
        self.app.write(self.board[0][1] + "|" + self.board[1][1] + "|" + self.board[2][1])
        self.app.write("   |   |   ")
        self.app.write("-----------")
        self.app.write("   |   |   ")
        self.app.write(self.board[0][2] + "|" + self.board[1][2] + "|" + self.board[2][2])
        self.app.write("   |   |   ")
        self.app.write("")

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
        self.app.write("")
        self.app.write(winner + "'s WON!!")
        self.app.write("")

    def end_game(self):
        """ Displayed after a game is finished """
        self.app.write("")
        try:
            self.app.write("Do you want to play again? (Y / N) ")
            self.app.wait_variable(self.app.inputVariable)
            decision = self.app.inputVariable.get() 
            self.app.write("")
            # Checks if the input was valid
            if decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                raise InputError
            # Do not want to play again
            if decision == "N" or decision == "n":
                self.running = False
                self.app.write("THANKS FOR PLAYING!!")
                self.app.write("")
                time.sleep(1.5)
        # invalid input 
        except InputError:
            self.app.write("Make sure you enter the correct value!! (Y / N)")
            self.app.write("")
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