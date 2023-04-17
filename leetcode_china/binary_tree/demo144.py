from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder(root:TreeNode):
    if root is None:
        return None

    # 前序遍历，用栈来实现
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

if __name__ == '__main__':

