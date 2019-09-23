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

""" print the board in the familiar sudoku layout """

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------------------")

        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j])+ " ", end=" ")

"""
find the next not filled in location on the board,
and return the row and collum
"""

def find_clear_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

""" check if the wanted move is a valid move """

def check_valid(board, row, col, num):
    if not check_row(board, row, num):
        return False
    elif not check_col(board, col, num):
        return False
    #elif not check_square(board, row, col, num):
    #    return False
    else:
        return True


def check_col(board, col, num):
    for i in range(len(board)):
        if board[i][col] == num:
            return False
    return True

def check_row(board, row, num):
    for i in range(len(board[row])):
        if board[row][i] == num:
            return False
    return True

#def check_square(board, row, col, num):



def solve():
    row, col = find_clear_spot(board)
    if row != row and col != col:
        return true

    for i in range(1,10):
        print(check_valid(board, row, col, i))

solve()
