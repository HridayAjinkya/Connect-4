from position import Position
from solver import Solver

def play_connect4():
    pos = Position()
    sol = Solver()

    print("Welcome to Connect 4!")
    pFirst = False

    while True:
        if pFirst == True:
            p = playerMove(pos)
            if checkBoard(pos, p, True) == 0:
                pos.play(p)
                break
            pos.play(p)
            print("Current board state:")
            print(pos.board)
            print("")
            s = solMove(pos, sol)
            if checkBoard(pos, s, False) == 0:
                pos.play(s)
                break
            pos.play(s)
            print("Current board state:")
            print(pos.board)
            print("")
        else:
            s = solMove(pos, sol)
            if checkBoard(pos, s, False) == 0:
                pos.play(s)
                break
            pos.play(s)
            print("Current board state:")
            print(pos.board)
            print("")
            p = playerMove(pos)
            if checkBoard(pos, p, True) == 0:
                pos.play(p)
                break
            pos.play(p)
            print("Current board state:")
            print(pos.board)
            print("")

    print("Game Over.")
    print(pos.board)
    print(f"Total moves: {pos.nbMoves()}")
    print(f"Solver's node count: {sol.getNodeCount()}")        

def playerMove(pos):
    while True:
        try:
            col = int(input("Your turn! Enter column number (1-7): ")) - 1
            if not pos.canPlay(col):
                print("Invalid move. Column is full.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid column number (1-7).")
    return col
    
def solMove(pos, sol):
    print("Solver's turn...")
    s = sol.solverMove(pos)
    return s

def checkBoard(pos, col, p):
    if pos.isWinningMove(col):
        if p == True:
            print("You have won")
        else:
            print("The solver has won")
        return 0
    if pos.nbMoves() == Position.WIDTH * Position.HEIGHT-1:
        print("It's a draw!")
        return 0
    return 1

play_connect4()