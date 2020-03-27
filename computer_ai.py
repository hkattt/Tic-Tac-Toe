# AI class file

import copy

class AI():
    def __init__(self, game, cross=False, nought=True):
        self.game = game
        self.cross = cross
        self.nought = nought

    def minimax(self, state, isMaximizing):
        """ Performs the minimax algorithm to determine the best move """
        # AI won
        if self.current_state(state) == "O":
            return 1, None
        # Human won
        elif self.current_state(state) == "X":
            return -1, None
        # Draw
        elif self.current_state(state) == 0:
            return 0, None

        # AI move
        if isMaximizing:
            best = (-2, None)
            for x in range(len(state)):
                for y in range(len(state[x])):
                    if state[x][y] == "   ":
                        state_new = copy.deepcopy(state)
                        state_new[x][y] = " O "
                        value = self.minimax(state_new, False)[0]
                        if value > best[0]:
                            best = (value, (x, y))
            return best

        # Human move
        else:
            best = (2, None)
            for x in range(len(state)):
                for y in range(len(state[x])):
                    if state[x][y] == "   ":
                        state_new = copy.deepcopy(state)
                        state_new[x][y] = " X "
                        value = self.minimax(state_new, True)[0]
                        if value < best[0]:
                            best = (value, (x, y))
            return best
                
    def move(self):
        X, Y = (self.minimax(self.game.board, True))[1]
        self.game.board[X][Y] = " O "
        return X, Y
        
    def current_state(self, state):
        draw = True
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == "   ":
                    draw = False
        if draw:
            return 0

        # checks vertical
        if state[0][0] == state[0][1] == state[0][2] and state[0][0] != "   ":
            return state[0][0]
        if state[1][0] == state[1][1] == state[1][2] and state[1][0] != "   ":
            return state[1][0] 
        if state[2][0] == state[2][1] == state[2][2] and state[2][0] != "   ":
            return state[2][0]

        # checks horizontals
        if state[0][0] == state[1][0] == state[2][0] and state[0][0] != "   ":
            return state[0][0]
        if state[0][1] == state[1][1] == state[2][1] and state[0][1] != "   ":
            return state[0][1] 
        if state[0][2] == state[1][2] == state[2][2] and state[0][2] != "   ":
            return state[0][2]

        # checks diagonals
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] != "   ":
            return state[0][0]
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] != "   ":
            return state[0][2]

        return None