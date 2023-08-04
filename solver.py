from position import Position
import numpy as np

class Solver:
    N_Steps = 8
    def __init__(self):
        self.nodeCount = 0
        self.columnOrder = np.zeros(Position.WIDTH, dtype = int)
        for col in range(Position.WIDTH):
            self.columnOrder[col] = Position.WIDTH // 2 + (1-2*(col % 2))*(col + 1)//2

    def negamax(self, P: Position, alpha, beta, depth):    
        self.nodeCount += 1
        if P.nbMoves() == Position.WIDTH * Position.HEIGHT:
            return 0
        if depth == 0:
            return (Position.WIDTH * Position.HEIGHT + 1 - P.nbMoves()) // 2
        for col in range(Position.WIDTH):
            if P.canPlay(col) and P.isWinningMove(col):
                return (Position.WIDTH * Position.HEIGHT + 1 - P.nbMoves()) // 2
        max = (Position.WIDTH * Position.HEIGHT - 1 - P.nbMoves()) // 2
        if beta > max:
            beta = max
            if alpha >= beta:
                return beta
        for col in range(Position.WIDTH):
            if P.canPlay(self.columnOrder[col]):
                P2 = Position()
                P2.board = np.copy(P.board)
                P2.height = np.copy(P.height)
                P2.moves = P.moves
                P2.play(self.columnOrder[col])
                score = -self.negamax(P2, -beta, -alpha, depth-1)
                if score >= beta:
                    return score
                if score > alpha:
                    alpha = score
        return alpha

    def solve(self, P: Position):
        self.nodeCount = 0
        return self.negamax(P, -Position.WIDTH*Position.HEIGHT // 2, Position.WIDTH*Position.HEIGHT // 2, self.N_Steps)
    
    def solverMove(self, P: Position):
        temp = Position()
        temp.board = np.copy(P.board)
        temp.height = np.copy(P.height)
        temp.moves = P.moves
        best = np.Inf
        c = 0
        for col in range(Position.WIDTH):
            if temp.canPlay(self.columnOrder[col]) and temp.isWinningMove(self.columnOrder[col]):
                return self.columnOrder[col]
        for col in range(Position.WIDTH):
            if temp.canPlay(self.columnOrder[col]):
                temp.play(self.columnOrder[col])
                s = self.solve(temp)
                if s < best:
                    best = s
                    c = self.columnOrder[col]            
            temp.board = np.copy(P.board)
            temp.height = np.copy(P.height)
            temp.moves = P.moves
        return c

    def getNodeCount(self):
        return self.nodeCount