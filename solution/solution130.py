from typing import List
import queue

import collections


def top(i, j, m, n):
    '''

    :param i:
    :param j:
    :param m: 行
    :param n: 列
    :return:
    '''
    if i == 0 and 0 <= j < n:
        return True


def bottom(i, j, m, n):
    '''

    :param i:
    :param j:
    :param m: 行
    :param n: 列
    :return:
    '''
    if i == (n - 1) and 0 <= j < n:
        return True


def left(i, j, m, n):
    '''

    :param i:
    :param j:
    :param m: 行
    :param n: 列
    :return:
    '''
    if 0 < i < m and j == 0:
        return True


def right(i, j, m, n):
    '''

    :param i:
    :param j:
    :param m: 行
    :param n: 列
    :return:
    '''
    if 0 < i < m and j == (n - 1):
        return True


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if (not 0 <= x < m) or (not 0 <= y < n):
                return
            if board[x][y] != 'O':
                return

            board[x][y] = 'A'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)


        for i in range(m):
            for j in range(n):
                e = board[i][j]
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(b[1][2])
    Solution().solve(b)
    print(b)
