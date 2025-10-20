#https://neetcode.io/problems/valid-sudoku

import math
from collections import defaultdict

def isValidSudoku(board):

    sub_box = defaultdict(set)
    row = defaultdict(set)
    column = defaultdict(set)

    for r in range(9):
        zoneY = (r // 3) * 3
        for c in range(9):
            if board[r][c] == ".":
                continue

            #Calculates the dictionary zone
            zoneX = math.ceil((c + 1) / 3)
            zone = zoneY + zoneX

            #Checks number against rules
            if board[r][c] in sub_box[zone] or board[r][c] in row[r] or board[r][c] in column[c]:
                return False
            else:
                sub_box[zone].add(board[r][c])
                row[r].add(board[r][c])
                column[c].add(board[r][c])

    return True

board =[["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board2 =[[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(board))
print(isValidSudoku(board2))