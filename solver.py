import time
from random import randint


# This finds the next empty spot on the board. 0 is considered empty
def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# makes sure the current board is a valid one. Also used for checking for correct solution
def isValid(board, num, pos):
    if num == 0:
        return False
    x, y = pos
    # checking column
    for i in range(9):
        if i != x and board[i][y] == num:
            return False
    # checking row
    for j in range(9):
        if j != y and board[x][j] == num:
            return False

    # checking box
    boxX = int(x / 3)
    boxY = int(y / 3)
    for i in range(boxX * 3, boxX * 3 + 3):
        for j in range(boxY * 3, boxY * 3 + 3):
            if board[i][j] == num and (i != x or j != y):
                return False
    return True


# recursive algorithm for solving it.
def solve(board, start):
    # this is to make sure the puzzle is easily solvable, otherwise will not use that puzzle
    if time.process_time() - start > 1.00:
        raise Exception("Too complicated")
    coord = findEmpty(board)
    if coord is None:  # means that we've solved the puzzle, is base case
        return True
    else:
        x, y = coord
    for i in range(1, 10):
        if isValid(board, i, (x, y)):  # checks to make sure that it's a valid space
            board[x][y] = i
            if solve(board, start):  # calls the algorithm recursion.
                return True
            board[x][y] = 0
    return False  # other base case, if there's no possible way for the number to work, therefore backtracking


# prints board into a 2d array, with lines seperating each 3x3 box
def printBoard(board):
    for i in range(9):
        if i in [3, 6]:
            print("-------------------------")
        for j in range(9):
            if j in [3, 6]:
                print("| ", end=" ")
            print((board[i][j]), end=" ")
        print()
        if i == 8:
            print("-------------------------")

# makes a random array with 19 starting values. Does its best to keep it evenly distributed using weights.
def starting():
    board = [[0] * 9 for a in range(9)]
    total = 81
    goal = 20
    for i in range(9):
        for j in range(9):
            weight = randint(1, total) # goal of this is to try and evenly spread the numbers
            if weight < goal:
                insert = 1
                while insert:
                    num = randint(1, 9)
                    if isValid(board, num, (i, j)): # makes sure that the array is a valid one.
                        board[i][j] = num
                        goal -= 1
                        insert = 0
            total -= 1

    return board
