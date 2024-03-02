board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(sb):
    # Finding Empty Slot
    find = find_empty_slot(sb)
    if find == None: # If No Slot Found that means, Sudoku is solved as due to backtracking only one possible solution is found
        return True
    else:
        row, col = find

    for i in range(1, 10):
        valid = valid_slot(sb, i, (row, col))
        if valid: # If Number put is valid, Then Put it on The Board
            sb[row][col] = i
            if solve(sb):
                return True
            sb[row][col] = 0 # Reinitializing value to 0 if not valid
    return False


def valid_slot(sb, no, loc):

    # Checking if Column is satisfied
    for i in range(len(sb)):
        if sb[i][loc[1]] == no and loc[0] != i:
            return False

    # Checking if Row is satisfied
    for i in range(len(sb[0])):
        if sb[loc[0]][i] == no and loc[1] != i:
            return False

    # Checking Box
    boxX = loc[1]//3
    boxY = loc[0]//3
    for i in range(boxY*3, (boxY*3) + 3):
        for j in range(boxX*3, (boxX*3)+3):
            if sb[i][j] == no and (i, j) != loc:
                return False

    return True


def print_board(sb):
    for i in range(len(sb)):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(len(sb[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sb[i][j])
            else:
                print(str(sb[i][j]) + " ", end="")


def find_empty_slot(sb):
    for i in range(len(sb)):
        for j in range(len(sb[0])):
            if sb[i][j] == 0:
                return (i, j)
    return None


solve(board)
print_board(board)