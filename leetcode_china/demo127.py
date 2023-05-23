from typing import List, Optional

"""
图的广度优先遍历
"""
graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

visited = {}
que = []
start_vector = 'A'
que.insert(0, start_vector)

def BFS(graph):
    while que:
        vector = que.pop()
        if visited.get(vector) is None:
            print(vector)

            visited[vector] = 1

            vs = graph[vector]
            for v in vs:
                que.insert(0, v)
            BFS(graph)

if __name__ == '__main__':
    BFS(graph)