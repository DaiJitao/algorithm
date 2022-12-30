'''图的深度优先遍历'''
import pandas as pd

visited = set()


def dfs(x, y):
    if (not 0 <= x < m) or (not 0 <= y < n) or (x, y) in visited:
        return

    visited.add((x, y))
    print(graph[x, y])
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


m, n = 4, 4
graph = range(1, 17)
graph = pd.array(graph).reshape((4, 4))
print(graph)
dfs(0, 0)
