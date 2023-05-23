from typing import List, Optional


def demo(matrix):
    """
    思路：找出来所有为0的下标
    :param matrix:
    :return:
    """
    if matrix is None:
        return None
    m = len(matrix)
    if m == 0:
        return matrix

    n = len(matrix[0][0])

    flag_col_0 = False
    # 遍历所有行的首列
    for i in range(m):
        if matrix[i][0] == 0:
            flag_col_0 = True

    for j in range(1, n):
        if matrix[i][j] == 0:
            matrix[i][0] = matrix[0][j] = 0

    for i in range(m-1, -1, -1):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
            if flag_col_0:
                matrix[i][0] = 0





