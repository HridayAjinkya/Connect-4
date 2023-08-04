import numpy as np

class Position:
    WIDTH = 7 # Width of board
    HEIGHT = 6 # Height of board

    def __init__(self):
        self.board = np.zeros((self.HEIGHT, self.WIDTH), dtype = int)
        self.height = np.zeros(self.WIDTH, dtype = int)
        self.moves = 0
    
    def canPlay(self, col):
        return self.height[col] < self.HEIGHT
    
    def play(self, col):
        self.board[(self.HEIGHT - 1) - self.height[col]][col] = self.moves % 2 + 1
        self.height[col] += 1
        self.moves += 1

    def playSeq(self, seq):
        for i in range(len(seq)):
            col = int(seq[i]) - 1
            if col < 0 or col>= self.WIDTH or not self.canPlay(col) or self.isWinningMove(col):
                return i
            self.play(col)
        return len(seq)
    
    def isWinningMove(self, col):
        currPlayer = 1 + self.moves%2
        temp = np.copy(self.board)
        temp[(self.HEIGHT - 1) - self.height[col]][col] = currPlayer
        # Horizontal
        for i in range(7):
            for row in range(6):
                moveWindow = list(temp[row][i:i+4])
                if moveWindow.count(currPlayer) == 4:
                    return True
        # Vertical
        for i in range(self.WIDTH):
            window = [c[i] for c in temp]
            for row in range(self.HEIGHT-3):
                moveWindow = window[row:row+4]
                if moveWindow.count(currPlayer) == 4:
                    return True
        # Pos Diagonal
        for i in range(4):
            for row in range(3, 6):
                window = [temp[row][i], temp[row-1][i+1], temp[row-2][i+2], temp[row-3][i+3]]
                if window.count(currPlayer) == 4:
                    return True
        # Neg Diagonal
        for i in range(4):
            for row in range(3):
                window = [temp[row][i], temp[row+1][i+1], temp[row+2][i+2], temp[row+3][i+3]]
                if window.count(currPlayer) == 4:
                    return True
        return False
    
    def nbMoves(self):
        return self.moves
