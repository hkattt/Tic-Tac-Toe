# AI class file

class AI():
    def __init__(self, game, cross=False, nought=True):
        self.game = game
        self.cross = cross
        self.nought = nought

    def minimax(self, isMaximizing):
        pass
                
    def move(self):
        pass

    def valid_move(self, X, Y):
        """ Checks if the chosen move is legal """
        if self.game.board[X][Y] == "   ":
            return True
        return False


