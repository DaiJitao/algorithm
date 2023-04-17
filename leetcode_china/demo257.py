from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if root.left is None and root.right is None:
        #     return [str(root.val)]

        stack = [root]
        path_stack = [str(root.val)]
        res = []
        while stack:
            cur = stack.pop()
            path = path_stack.pop()
            if cur.right is None and cur.left is None:
                res.append(path)
                if len(stack) == 0:
                    break
                continue

            if cur.right is not None:
                stack.append(cur.right)
                path_stack.append(path + '->' + str(cur.right.val))

            if cur.left is not None:
                stack.append(cur.left)
                path_stack.append(path + '->' + str(cur.left.val))

        return res


class Solution2:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        res = []
        path = ''
        def dfs(root, path):
            if root is None:
                return

            if root.left is None and root.right is None:
                res.append(path + str(root.val))
                return

            dfs(root.left, path + str(root.val) + '->')
            dfs(root.right, path + str(root.val) + '->')

        dfs(root, path)
        return res









def dfs(root:TreeNode):
    """非递归实现，借助于栈"""