import copy
import time

from solver import starting, solve, printBoard, isValid


# frontend part.
def main():
    print("Welcome to Sudoku puzzle.\n Here is a puzzle for you to solve.")
    done = 1
    while done:  # keeps going until a suitable board is generated.
        try:
            board = starting()
            cop = copy.deepcopy(board)
            solve(cop, time.process_time())  # makes sure board is easily solvable, also stores it for later
        except:  # this will happen if board isn't solvable, in this case, nothing happens and code tries again.
            pass
        else:
            printBoard(board)
            done = 0
    stat = getStarting(board)  # finds starting values, these are not going to be changed.
    print("Press S to autosolve. Press I to insert something. Press P to print board. Good luck!")
    while not isDone(board):
        com = input("Enter input: ")
        if com == 'S':
            print("Here is the solution\n")
            board = copy.deepcopy(cop)
            printBoard(board)
        elif com == "I":
            print("Notes: base values can't change. x and y is from 0 to 8")
            i1 = input("enter x: ")
            i2 = input("enter y: ")
            i3 = input("enter num desired")
            try:  # converting the string inputs to ints, if it doesnt work, then throws an error
                x = int(i1)
                y = int(i2)
                num = int(i3)
            except ValueError:
                print("invalid input, try again")
            else:
                if (x, y) not in stat and isValid(board, num, (x, y)) and 0 <= x <= 8 and 0 <= y <= 8 and 1 <= num < 9:
                    board[x][y] = num
                    printBoard(board)

                else:
                    print("invalid input, try again")
        elif com == "P":
            printBoard(board)
        else:
            print("invalid input, try again")
    print("Thanks for playing!")


# checks if board is solved
def isDone(board):
    for i in range(9):
        for j in range(9):
            if not isValid(board, board[i][j], (i, j)):
                return False
    return True


# gets initial values, these ones can't be changed.
def getStarting(board):
    ret = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                ret.append((i, j))
    return ret


main()
