from typing import List, Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # if root.left is None and root.right is None:
        #     return [str(root.val)]
        if root is None:
            return False

        stack = [root]
        path_stack = [root.val]
        while stack:
            cur = stack.pop()
            path = path_stack.pop()
            if cur.right is None and cur.left is None:
                if path == targetSum:
                    return True

                continue

            if cur.right is not None:
                stack.append(cur.right)
                path_stack.append(path + cur.right.val)

            if cur.left is not None:
                stack.append(cur.left)
                path_stack.append(path + cur.left.val)

        return False