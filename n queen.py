def isSafe (board, row, col):
    # check left row
    for y in range(col):
        if board[row][y] == 1:
            return False
    # check diagonal left top
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    # check diagonal left bottom
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True

def generateSolution(board, col):
    # terminating condition
    # all columns covered
    global N
    if col >= N:
        return True
    # loop over all the rows
    for i in range(N):
        if isSafe(board, i, col) == True:
            board[i][col] = 1
            # recursively place other queens
            if generateSolution(board, col + 1) == True:
                return True
            # unmark queen spot
            board[i][col] = 0
    # backtrack
    return False
def printboard(b):
    for i in range(len(b)):
        for j in range(len(b)):
            print(b[i][j], end=' ')
        print(' ')


N = int(input("give a size: "))
startCol = 0
board = [[0 for i in range(N)] for j in range(N)]
# print(board)

if generateSolution(board, startCol) == False:
    print("No Solution Exists")
else:
    print("Solution exists")
    printboard(board)