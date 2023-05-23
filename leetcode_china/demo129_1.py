from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        path = []
        res = []

        def dfs(root:TreeNode):

            path.append(str(root.val))

            if root.left is None and root.right is None:
                res.append(''.join(path[:]))


            if root.left is not None:
                dfs(root.left)

            if root.right is not None:
                dfs(root.right)

            path.pop()

        dfs(root)



if __name__ == '__main__':
    root = TreeNode(1)
    left1 = TreeNode(2)
    right2 = TreeNode(3)
    root.left = left1
    root.right = right2

    left4 = TreeNode(4)
    right5 = TreeNode(5)

    left11 = TreeNode(11)

    left1.left = left4
    left1.right = right5

    right2.left = left11

    res = Solution().sumNumbers(root)
    print(res)
