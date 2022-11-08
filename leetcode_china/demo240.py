def isArea(i, j, m, n):
    """m行n列"""
    if i >= 0 and i < m and j >= 0 and j < n:
        return True
    return False


def demo240(matrix: [], target: int):
    m = len(matrix)  # m行n列
    if m == 0:
        return False

    n = len(matrix[0])
    if n == 0:
        return False

    p1 = (0, 0)
    p2 = (0, n - 1)
    p3 = (m - 1, 0)
    p4 = (m - 1, n - 1)
    min_row, min_col = p1
    max_row, max_col = p4
    while isArea(max_row, max_col, m, n) and isArea(min_row, min_col, m, n) and
