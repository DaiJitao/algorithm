from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root

        res = []
        def preOrder(root:TreeNode):
            if root is None:
                return

            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)


        preOrder(root)
        head = ListNode(res[0])
        h = head
        for i in res[1:]:
            newNode = ListNode(i)
            head.next = newNode
            head = newNode

        return h

if __name__ == '__main__':
    head = ListNode(0)
    h = head
    for i in [1,2,3]:
        newNode = ListNode(i)
        h.next = newNode
        h = newNode

    while head:
        print(head.val)
        head = head.next

