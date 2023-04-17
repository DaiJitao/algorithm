from typing import List
from typing import Optional
from collections import deque


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        que = deque([root])
        while que:
            size = len(que)
            temp = []
            for _ in range(size):
                node = que.popleft()
                temp.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)

            results.append(temp)

        return results


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        results = []
        que = [root]
        while len(que) != 0:
            size = len(que)
            temp = []
            for _ in range(size):
                node = que.pop(-1)
                temp.append(node.val)
                if node.left is not None:
                    que.insert(0, node.left)
                if node.right is not None:
                    que.insert(0, node.right)

            results.append(temp)

        return results


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        que = [root]
        temp = []
        res = []
        while que:
            temp = []
            for _ in range(len(que)):
                node = que.pop()
                temp.append(node.val)
                if node.left is not None:
                    que.insert(0, node.left)

                if node.right is not None:
                    que.insert(0, node.right)

            res.append(temp[:])


if __name__ == '__main__':
    pass
