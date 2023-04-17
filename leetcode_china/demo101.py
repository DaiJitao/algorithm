from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        que = [root]

        while que:
            res = []
            for _ in range(len(que)):
                node = que.pop()
                if node is None:
                    res.append(None)
                else:
                    res.append(node.val)

                if node is None or (node.left is None and node.right is None):
                    continue
                else:
                    que.insert(0, node.left)
                    que.insert(0, node.right)

            print(res)
            if len(res) > 1:
                half = int(len(res) / 2)
                interval = len(res) - 1
                for i in range(half):
                    endIndex = interval - i
                    if res[i] != res[endIndex]:
                        return False

        return True


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        que = []
        que.insert(0, root.left)
        que.insert(0, root.val)
        while que:
            leftnode = que.pop()
            rightnode = que.pop()
            if leftnode is None and rightnode is None:
                continue

            if leftnode is not None or rightnode is not None or rightnode.val != leftnode.val:
                return False

            que.insert(0, leftnode.left)
            que.insert(0, rightnode.right)
            que.insert(0, leftnode.right)
            que.insert(0, rightnode.left)
        return True
