import math

N = 8
chessboard = [['|___|' for i in range(N)] for j in range(N)]

def printboard():
    for i in range(N):
        for j in range(N):
            print(chessboard[i][j] , end = " ")
        print()

def ispossiblemove(chessboard, row, col):
    #row check
    for i in range(col):
        if chessboard[row][i] == '| Q |':
            return False
    #diagnoal check
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
        if chessboard[i][j] == '| Q |':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),range(col, -1, -1)):
        if chessboard[i][j] == '| Q |':
            return False

    return True


def solver(chessboard, col):
    if col >= N:
        return True
    for i in range(N):
        if ispossiblemove(chessboard, i, col):
            chessboard[i][col] = '| Q |'
            if solver(chessboard, col + 1) == True:
                return True
            chessboard[i][col] = '|___|'

    return False

while(solver(chessboard,0) == True):
    printboard()



