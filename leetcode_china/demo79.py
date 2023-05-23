from typing import List, Optional


def isValidArea(row, col):
    if m > row >= 0 and n > col >= 0:
        if visted[row][col] == 0:
            return True

    return False


def findAll(i, j, k):
    if board[i][j] != word[k]:
        return False

    if k == len(word) - 1:
        return True

    for x, y in directions:
        i, j = i + x, j + y
        if isValidArea(i, i):
            k += 1
            visted[i][j] = 1
            findAll(i, j, k)

    visted[i][j] = 0
    return False


board = []
word = ''
visted = None
m = len(board)
n = len(board[0])
temp = [0] * n
visted = [temp[:]] * m
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def demo():
    if board is None:
        return 0
    m = len(board)
    n = len(board[0])

    if m == 0 or n == 0:
        return 0
    for i in range(m):
        for j in range(n):
            row, col = i - 1, j  # 上
            row, col = i + 1, j  # 下
            row, col = i, j - 1  # 左
            row, col = i, j + 1  # 右
