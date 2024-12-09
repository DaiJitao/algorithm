from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root

        que = [root]
        while que:
            length = len(que)
            tmp = []
            for i in range(length):
                currNode = que.pop()
                if i == length-1:
                    currNode.next = None
                else:
                    currNode.next = que[-1]
                if currNode.left != None:
                    que.insert(0, currNode.left)
                if currNode.right != None:
                    que.insert(0, currNode.right)


        return root