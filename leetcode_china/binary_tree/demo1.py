from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrder(root:TreeNode):
    res = []
    def frontTravel(root:TreeNode):
        if root is None:
            return

        res.append(root.val)
        frontTravel(root.left)
        frontTravel(root.right)

    frontTravel(root)
    return res

# 后续遍历，基于递归实现
def lastOrder(root: TreeNode):
    res = []

    def frontTravel(root: TreeNode):
        if root is None:
            return


        frontTravel(root.left)
        frontTravel(root.right)
        res.append(root.val)

    frontTravel(root)
    return res

#前序遍历，基于迭代实现
def preOrder(root: TreeNode):
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return res

#后前序遍历，基于迭代实现
def preOrder(root: TreeNode):
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)

    return res


def middleOrder(root: TreeNode):
    if root is None:
        return []
