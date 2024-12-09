from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return root

        que = [root]

        count = 0
        while que:
            size = len(que)
            for index in range(size):
                currNode = que.pop()
                if size == 1:
                    currNode.next = None
                if index == 0:
                    preNode = currNode
                else:
                    preNode.next = currNode
                    preNode = currNode

                if currNode.left is not None:
                    que.insert(0, currNode.left)
                if currNode.right is not None:
                    que.insert(0, currNode.right)

            count += 1

        return root


if __name__ == '__main__':
    root = Node(1)

    node2 = Node(2)
    node3 = Node(3)

    root.left = node2
    root.right = node3

    node2.left = Node(4)
    node3.right = Node(7)

    Solution().connect(root)
