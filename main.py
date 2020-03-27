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
        self.player_symbols = [" X ", " O "]
        self.app = SimpleApp_tk(None)
        self.app.title("Tic Tac Toe")
        self.app.write("TIC TAC TOE")
        self.app.write("")

    def new(self):
        """ Creates a new game """
        try:
            self.app.write("GAME MODES: ")
            self.app.write("1 - Single Player (Against the AI) ")
            self.app.write("2 - Multiplayer (With a friend) ")
            self.app.write("")
            self.app.wait_variable(self.app.inputVariable)
            decision = int(self.app.inputVariable.get().strip()) # single player or multiplayer
            self.app.write("")
            # checks if the input was valid
            if decision != 1 and decision != 2:
                raise InputError
            # singleplayer 
            if decision == 1:
                self.crosses = Player(self)
                self.noughts = AI(self)
            # multiplayer
            else:
                self.crosses = Player(self)
                self.noughts = Player(self, False, True)
                
        # invalid input
        except InputError:
            self.app.write("Make sure you enter the correct value!! (1 or 2)")
            self.app.write("")
            self.new()
        self.run()
    
    def run(self):
        """ creates a game loop (this runs inside the main loop) """
        self.playing = True
        self.draw()
        while self.playing:
            # crosses move
            previous_x, previous_y = self.crosses.move()
            self.draw()
            # checks if crosses won
            if self.win(previous_x, previous_y):
                self.victory_screen("X")
                self.playing = False
                break
            elif self.tie():
                self.draw_screen()
                self.playing = False
                break
            # noughts move
            previous_x, previous_y = self.noughts.move()
            self.draw()
            # checks if noughts won
            if self.win(previous_x, previous_y):
                self.victory_screen("O")
                self.playing = False
                break
            elif self.tie():
                self.draw_screen()
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

    def win(self, X, Y):
        """ Checks if the game was won by either player """
        # horizontal direction
        if self.board[0][Y] in self.player_symbols and self.board[0][Y] == self.board[1][Y] == self.board[2][Y]:
            return True
        # vertical direction
        elif self.board[X][0] in self.player_symbols and self.board[X][0] == self.board[X][1] == self.board[X][2]:
            return True
        # diagonal 1
        elif self.board[0][0] in self.player_symbols and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        # diagonal 2
        elif self.board[0][2] in self.player_symbols and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def tie(self):
        """ Checks if the game is tied """
        # cycles through the entire board, returns true if none of the elements are empty
        for column in self.board:
            for symbol in column:
                if symbol == "   ":
                    return False
        return True

    def victory_screen(self, winner):
        """ Victroy message """
        self.app.write("")
        self.app.write(winner + "'s WON!!")
        self.app.write("")

    def draw_screen(self):
        """ Draw message """
        self.app.write("")
        self.app.write(" THE GAME ENDED IN A DRAW!!")
        self.app.write("")

    def end_game(self):
        """ Displayed after a game is finished """
        self.app.write("")
        try:
            self.app.write("Do you want to play again? (Y / N) ")
            self.app.wait_variable(self.app.inputVariable)
            decision = self.app.inputVariable.get() 
            self.app.write("")
            # checks if the input was valid
            if decision != "Y" and decision != "y" and decision != "N" and decision != "n":
                raise InputError
            # do not want to play again
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